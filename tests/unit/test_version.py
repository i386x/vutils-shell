#
# File:    ./tests/unit/test_version.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2024-06-02 11:30:20 +0200
# Project: vutils-shell: Shell utilities
#
# SPDX-License-Identifier: MIT
#
"""Test :mod:`vutils.shell.version` module."""

from vutils.testing.testcase import TestCase

from vutils.shell.version import __version__


class VersionTestCase(TestCase):
    """Test case for version."""

    __slots__ = ()

    def test_version(self):
        """Test if version is defined properly."""
        self.assertIsInstance(__version__, str)
