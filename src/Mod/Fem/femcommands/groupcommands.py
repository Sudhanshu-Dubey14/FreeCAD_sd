# ***************************************************************************
# *   Copyright (c) 2020 Sudhanshu Dubey <sudhanshu.thethunder@gmail.com>   *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

__title__ = "FreeCAD FEM group command definitions"
__author__ = "Sudhanshu Dubey"
__url__ = "http://www.freecadweb.org"

## @package groupcommands
#  \ingroup FEM
#  \brief FreeCAD FEM group command definitions

import FreeCAD
import FreeCADGui

from PySide.QtCore import QT_TRANSLATE_NOOP

# Python group command definitions
# for C++ command definitions see src/Mod/Fem/Command.cpp
# for python single command definitions see src/Mod/Fem/femcommand/commands.py


class _SolverGroupCommand:

    def GetCommands(self):
        return tuple(['FEM_SolverCalculixCxxtools',
                      'FEM_SolverCalculiX',
                      'FEM_SolverElmer',
                      'FEM_SolverZ88'])

    def GetResources(self):
        return {'MenuText': QT_TRANSLATE_NOOP("FEM_Solver", 'FEM Solvers'),
                'ToolTip': QT_TRANSLATE_NOOP("FEM_Solver", 'FEM Solvers')
                }

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


class _MesherGroupCommand:

    def GetCommands(self):
        return tuple(['FEM_MeshGmshFromShape',
                      'FEM_MeshNetgenFromShape'])

    def GetResources(self):
        return {'MenuText': QT_TRANSLATE_NOOP("FEM_Mesh", 'FEM Meshers'),
                'ToolTip': QT_TRANSLATE_NOOP("FEM_Mesh", 'FEM Meshers')
                }

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


FreeCADGui.addCommand(
    'FEM_Solver',
    _SolverGroupCommand()
)
FreeCADGui.addCommand(
    'FEM_Mesh',
    _MesherGroupCommand()
)
