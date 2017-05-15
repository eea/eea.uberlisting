""" Adapters
"""

from zope.component import adapts
from zope.interface import implements

from eea.uberlisting.browser.app.interfaces import IUberlistingForm, \
    IUberlistingView


class UberlistingAdapter(object):
    """ IUberlistingView adapter
    """
    adapts(IUberlistingView)
    implements(IUberlistingForm)

    def __init__(self, context):
        self.content = context

    def editProperty(self, key, value, value_type='string'):
        """ :param key: property name
            :param value: property value
            :param value_type: property type value
            :return: added or edited property
        """
        if self.content.hasProperty(key):
            self.content.manage_changeProperties({key: value})
        else:
            self.content.manage_addProperty(key, value, value_type)



    def lget(self):
        """ getter
        """
        return self.content.getProperty('noUberlistingTemplateImages', '')

    def lset(self, value):
        """ setter
        """
        self.editProperty('noUberlistingTemplateImages', value, 'boolean')

    listTemplatesAsText = property(lget, lset)

    def dget(self):
        """ getter
        """
        return self.content.getProperty('defaultUberlistingTemplate',
                                        'folder_listing')

    def dset(self, value):
        """ setter
        """
        self.editProperty('defaultUberlistingTemplate', value)

    defaultTemplate = property(dget, dset)

    def eget(self):
        """ getter
        """
        return self.content.getProperty('bannedUberlistingTemplates', '')

    def eset(self, value):
        """ setter
        """
        self.editProperty('bannedUberlistingTemplates', value, 'lines')

    excludedTemplates = property(eget, eset)

    def oget(self):
        """ getter
        """
        return self.content.getProperty('onlyUberlistingTemplateWithImages', '')

    def oset(self, value):
        """ setter
        """
        self.editProperty('onlyUberlistingTemplateWithImages', value,
                          'boolean')

    onlyTemplatesWithIcons = property(oget, oset)
