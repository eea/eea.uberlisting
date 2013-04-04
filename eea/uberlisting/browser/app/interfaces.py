""" Browser interfaces
"""

from zope.interface import Interface
from zope import schema
from zope.interface import invariant, Invalid
from eea.uberlisting import EEAMessageFactory as _
from eea.uberlisting.browser.app.vocabularies import available_context_layouts


class IUberlistingView(Interface):
    """ Marker interface to indicate that UberlistingView is enabled
    """


class IPossibleUberlistingView(Interface):
    """ Marker interface to indicate that UberlistingView can be enabled
    """


class IUberlistingForm(Interface):
    """ UberlistingForm Schema information
    """

    defaultTemplate = schema.Choice(
        title=_(u"Default template"),
        description=_(u'If no cookie is present with the name of the '
                      u'default template then this value will be used as '
                      u'default'),
        default=u'folder_listing',
        source=available_context_layouts
    )

    listTemplatesAsText = schema.Bool(
        title=_(u"List templates as text"),
        description=_('If checked templates will be listed with their '
                      'full names instead of any icons listing'),
        default=False
    )

    onlyTemplatesWithIcons = schema.Bool(
        title=_(u"List only templates with icons"),
        description=_('If checked only templates with corresponding icons '
                      'will be displayed'),
        default=False
    )
    excludedTemplates = schema.List(
        title=_(u"Exclude templates"),
        description=_('These templates will not be listed. Useful if a '
                      'template displays an error or it returns no result'),
        unique=True,
        value_type=schema.Choice(
            source=available_context_layouts),
        required=False

    )

    @invariant
    def textListingOrIcon(data):
        """ :param data: form data passed on submit
            :return: error if both listTemplatesAsText and
            onlyTemplatesWithIcons is enabled
        """
        if data.listTemplatesAsText and data.onlyTemplatesWithIcons:
            raise Invalid(_(u"'List templates as text' and 'List only "
                            u"templates with icons' are mutually "
                            u"exclusive"))
