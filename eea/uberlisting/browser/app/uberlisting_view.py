""" Controller
"""
from Products.Five import BrowserView

class UberlistingView(BrowserView):
    """ Returns smartTemplate if present in request
    """

    def getTemplateName(self):
        """ Name
        """
        if 'smartTemplate' in self.request:
            return self.request['smartTemplate']
        elif self.context.hasProperty('defaultSmartTemplate'):
            return self.context.getProperty('defaultSmartTemplate')
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
        views = [view for view in views if view[0] != 'uberlisting_view']
        return views 

    def getListingMacro(self):
        """ Macro
        """
        template = self.getTemplate()
        return template.macros.get('listing')
