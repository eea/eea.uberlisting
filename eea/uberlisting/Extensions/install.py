""" Uninstall Profile
"""
from Products.CMFCore.utils import getToolByName
from eea.uberlisting.browser.app.interfaces import IUberlistingView
from zope.interface import noLongerProvides

def uninstall(portal, reinstall=False):
    """ Uninstall profile setup
    """
    if not reinstall:
        setup_tool = getToolByName(portal, 'portal_setup')
        setup_tool.runAllImportStepsFromProfile(
            'profile-eea.uberlisting:uninstall')
        # remove also rolemaps from here and any interfaces from this package
        catalog = getToolByName(portal, 'portal_catalog')
        uberviews = catalog.searchResults(object_provides=
            'eea.uberlisting.browser.app.interfaces.IUberlistingView')
        for uberview in uberviews:
            obj = uberview.getObject()
            # set first available layout as layout after uninstall
            obj.setLayout(obj.getAvailableLayouts()[0][0])
            noLongerProvides(obj, IUberlistingView)
            obj.reindexObject(idxs='object_provides')
        return "Ran all uninstall steps."
