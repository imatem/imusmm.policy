# -*- coding: utf-8 -*-
"""Base module for unittesting."""

# from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.testing import z2

import unittest2 as unittest


class PolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import jmsmm.policy
        self.loadZCML(package=jmsmm.policy)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'jmsmm.policy:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'jmsmm.policy')


FIXTURE = PolicyLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="JMSMMPolicyLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="JMSMMPolicyLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """docstring for IntegrationTestCase"""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """docstring for FunctionalTestCase"""

    layer = FUNCTIONAL_TESTING
