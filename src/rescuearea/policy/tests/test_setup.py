# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rescuearea.policy.testing import RESCUEAREA_POLICY_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that rescuearea.policy is properly installed."""

    layer = RESCUEAREA_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if rescuearea.policy is installed."""
        self.assertTrue(self.installer.isProductInstalled("rescuearea.policy"))

    def test_browserlayer(self):
        """Test that IRescueareaPolicyLayer is registered."""
        from rescuearea.policy.interfaces import IRescueareaPolicyLayer
        from plone.browserlayer import utils

        self.assertIn(IRescueareaPolicyLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RESCUEAREA_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["rescuearea.policy"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rescuearea.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("rescuearea.policy"))

    def test_browserlayer_removed(self):
        """Test that IRescueareaPolicyLayer is removed."""
        from rescuearea.policy.interfaces import IRescueareaPolicyLayer
        from plone.browserlayer import utils

        self.assertNotIn(IRescueareaPolicyLayer, utils.registered_layers())
