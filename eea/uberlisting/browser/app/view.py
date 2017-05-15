""" Controller
"""
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from zope.interface import alsoProvides, noLongerProvides
from eea.uberlisting.browser.app.interfaces import IUberlistingView
from eea.uberlisting import EEAMessageFactory as _


def _redirect(self, msg=''):
    """ Redirect
    """
    if self.request:
        if msg:
            IStatusMessage(self.request).addStatusMessage(msg)
        self.request.response.redirect(self.context.absolute_url())
    return msg

class UberlistingView(BrowserView):
    """ Returns uberTemplate if present in request
    """

    def __init__(self, context, request):
        super(UberlistingView, self).__init__(context, request)
        self.context = context
        self.request = request


    def getTemplateName(self):
        """ Name
        """
        # if we are on faceted navigation we will also have uberTemplate[]
        uberTemplate = 'uberTemplate[]' if 'uberTemplate[]' \
                                                    in self.request else ''
        if uberTemplate:
            return self.request[uberTemplate]
        uberTemplate = 'uberTemplate' if 'uberTemplate'\
                                                    in self.request else ''
        if uberTemplate:
            return self.request[uberTemplate]
        elif self.context.hasProperty('defaultUberlistingTemplate'):
            return self.context.getProperty('defaultUberlistingTemplate')
        # return first layout registered for the context
        return self.context.getAvailableLayouts()[0][0]

    def getTemplate(self):
        """ View
        """
        name = self.getTemplateName()
        return getattr(self.context, name, '')

    def getAvailableTemplateNames(self):
        """ Available templates on context minus our listing
        """
        views = self.context.getAvailableLayouts()
        # filter views if the object has a lines property with the id's of
        # the templates that shouldn't be added to the uberlisting_view
        banned_views = list(self.context.getProperty(
                                            'bannedUberlistingTemplates', ''))
        views = [view for view in views if view[0] not in banned_views]
        return views

    def noUberlistingTemplateImages(self):
        """ Don't render template listing with images if we have a certain
            property
        """
        return self.context.getProperty('noUberlistingTemplateImages')

    def onlyUberlistingTemplateWithImages(self):
        """ Render template listing only if they have corresponding images
        """
        return self.context.getProperty('onlyUberlistingTemplateWithImages')

    def enable(self):
        """ Enable uberlisting view by providing IUberlistingView interface
        """
        # enable this listing also for the translation of the context if
        # LinguaPlone is enabled and this context is translated
        try:
            translations = self.context.getTranslations()
            for trans in translations.values():
                trans[0].setLayout('uberlisting_view')
                alsoProvides(trans[0], IUberlistingView)
                trans[0].reindexObject(idxs='object_provides')
        except AttributeError:
            self.context.setLayout('uberlisting_view')
            alsoProvides(self.context, IUberlistingView)
            self.context.reindexObject(idxs='object_provides')

        _redirect(self, _('UberlistingView enabled'))

    def disable(self):
        """ Disable uberlisting view by noLongerProviding IUberlistingView
        interface
        """
        try:
            translations = self.context.getTranslations()
            for trans in translations.values():
                # set as the layout the first available template
                trans[0].setLayout(trans[0].getAvailableLayouts()[0][0])
                noLongerProvides(trans[0], IUberlistingView)
                trans[0].reindexObject(idxs='object_provides')
        except AttributeError:
            self.context.setLayout(self.context.getAvailableLayouts()[0][0])
            noLongerProvides(self.context, IUberlistingView)
            self.context.reindexObject(idxs='object_provides')

        _redirect(self, _('UberlistingView disabled'))
