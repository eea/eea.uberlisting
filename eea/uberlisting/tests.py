""" Test doctests module
"""
import unittest
import eea.uberlisting

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()


class TestCase(ptc.PloneTestCase):
    """ TestSuite
    """
    class layer(PloneSite):
        """ Test layer
        """

        @classmethod
        def setUp(cls):
            """ Setup
            """
            fiveconfigure.debug_mode = True
            ztc.installPackage(eea.uberlisting)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            """ Tear down
            """
            pass


def test_suite():
    """ Suite
    """
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='eea.uberlisting',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='eea.uberlisting.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='eea.uberlisting',
            test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='eea.uberlisting',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
