""" Browser interfaces
"""

from zope.interface import Interface


class IUberlistingView(Interface):
    """Marker interface to indicate that SubFoldersViewlet should be enabled
    """
