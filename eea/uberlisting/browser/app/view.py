""" Controller
"""
from Products.Five import BrowserView
from zope.interface import alsoProvides, noLongerProvides
from eea.uberlisting.browser.app.interfaces import IUberlistingView
from Products.statusmessages.interfaces import IStatusMessage
from eea.uberlisting import EEAMessageFactory as _


class UberlistingView(BrowserView):
    """ Returns uberTemplate if present in request
    """

    def __init__(self, context, request):
        super(UberlistingView, self).__init__(context, request)
        self.context = context
        self.request = request

    def _redirect(self, msg=''):
        """ Redirect
        """
        if self.request:
            if msg:
                IStatusMessage(self.request).addStatusMessage(msg)
            self.request.response.redirect(self.context.absolute_url())
        return msg

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
        return 'folder_listing'

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
        banned_views.append('uberlisting_view')
        views = [view for view in views if view[0] not in banned_views]
        return views 

    def noUberlistingTemplateImages(self):
        """ Don't render template listing with images if we have a certain
            property
        """
        return self.context.getProperty('noUberlistingTemplateImages')

    def getListingMacro(self):
        """ Macro
        """
        template = self.getTemplate()
        if template:
            macro = template.macros.get('listing')
            if macro:
                return macro
        error_view = getattr(self.context, 'macro_error_view')
        return error_view.macros.get('listing')

    def enable(self):
        """ Enable uberlisting view by providing IUberlistingView interface
        """
        translations = self.context.getTranslations()
        for trans in translations.values():
            alsoProvides(trans[0], IUberlistingView)
            trans[0].reindexObject(idxs='object_provides')
        self._redirect(_('UberlistingView enabled'))

    def disable(self):
        """ Disable uberlisting view by noLongerProviding IUberlistingView
        interface
        """
        translations = self.context.getTranslations()
        for trans in translations.values():
            noLongerProvides(trans[0], IUberlistingView)
            trans[0].reindexObject(idxs='object_provides')
        self._redirect(_('UberlistingView disabled'))
