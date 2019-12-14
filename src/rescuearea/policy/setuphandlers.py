# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from plone import api
from zope.interface import implementer
from collective.ttwpo import api as poapi


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return ["rescuearea.policy:uninstall"]


def post_install(context):
    """Post install script"""
    if "rescuearea.core" not in poapi.domains():
        poapi.create("rescuearea.core", locales=["fr"])

    api.group.create(
        groupname="ppi_encoder", title="PPI Encoder", roles=["PPI Encoder"]
    )

    api.group.create(
        groupname="ppie_encoder", title="PPIE Encoder", roles=["PPIE Encoder"]
    )


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
