#-----------------------------------------------------------------------------
# Copyright (c) 2013-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_submodules

hiddenimports = []

# the iminuit package contains tests which aren't needed when distributing
for mod in collect_submodules('iminuit'):
    if not mod.startswith('iminuit.tests'):
        hiddenimports.append(mod)
