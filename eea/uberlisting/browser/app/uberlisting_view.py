""" Controller
"""
from Products.Five import BrowserView

class UberlistingView(BrowserView):
    """ Returns uberTemplate if present in request
    """

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
        return getattr(self.context, name)

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

    def getListingMacro(self):
        """ Macro
        """
        template = self.getTemplate()
        return template.macros.get('listing')
