""" Custom vocabularies
"""

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import alsoProvides


def available_context_layouts(context):
    """ :param context: Plone context object
        :return: Available layouts for given object
    """
    terms = []
    layouts = context.getAvailableLayouts()
    for layout in layouts:
        terms.append(SimpleVocabulary.createTerm(layout[0], str(layout[0]),
                                                 layout[1]))

    return SimpleVocabulary(terms)


alsoProvides(available_context_layouts, IContextSourceBinder)
