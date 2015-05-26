# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from Products.CMFCore.utils import getToolByName
from imusmm.policy.testing import IntegrationTestCase
from zope.component import getMultiAdapter

import unittest2 as unittest


class TestsInstall(IntegrationTestCase):
    """Test installation of imusmm.policy into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_product_installed(self):
        """Test if imusmm.policy is installed in portal_quickinstaller."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('imusmm.policy'))

    def test_portal_title(self):
        self.assertEqual(
            self.portal.getProperty('title'),
            "JM SMM")

    def test_portal_description(self):
        self.assertEqual(
            self.portal.getProperty('description'),
            "SMM")

    def test_default_language(self):
        # acording to documentation this must be in afterSetUp()
        ltool = self.portal.portal_languages
        ltool.setLanguageBindings()

        portal_state = getMultiAdapter(
            (self.portal, self.request), name=u'plone_portal_state')
        current_language = portal_state.language()
        self.assertEqual(current_language, 'en')


def test_suite():
    """This """
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
