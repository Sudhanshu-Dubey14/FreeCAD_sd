# ***************************************************************************
# *   Copyright (c) 2019 Sudhanshu Dubey <sudhanshu.thethunder@gmail.com>   *
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

__title__ = "FELT Writer"
__author__ = "Sudhanshu Dubey"
__url__ = "http://www.freecadweb.org"

## \addtogroup FEM
#  @{

import FreeCAD
import time
from .. import writerbase as FemInputWriter


class FemInputWriterFELT(FemInputWriter.FemInputWriter):
    def __init__(
        self,
        analysis_obj,
        solver_obj,
        mesh_obj,
        matlin_obj,
        matnonlin_obj,
        fixed_obj,
        displacement_obj,
        contact_obj,
        planerotation_obj,
        transform_obj,
        selfweight_obj,
        force_obj,
        pressure_obj,
        temperature_obj,
        heatflux_obj, initialtemperature_obj,
        beamsection_obj,
        beamrotation_obj,
        shellthickness_obj,
        fluidsection_obj,
        dir_name=None
    ):
        FemInputWriter.FemInputWriter.__init__(
            self,
            analysis_obj,
            solver_obj,
            mesh_obj,
            matlin_obj,
            matnonlin_obj,
            fixed_obj,
            displacement_obj,
            contact_obj,
            planerotation_obj,
            transform_obj,
            selfweight_obj,
            force_obj,
            pressure_obj,
            temperature_obj,
            heatflux_obj,
            initialtemperature_obj,
            beamsection_obj,
            beamrotation_obj,
            shellthickness_obj,
            fluidsection_obj,
            dir_name
        )
        # working dir and input file
        from os.path import join
        # self.main_file_name = self.mesh_object.Name + '.in'
        self.main_file_name = 'beam.flt'
        self.file_name = join(self.dir_name, self.main_file_name)
        FreeCAD.Console.PrintLog('FemInputWriterCcx --> self.dir_name  -->  ' + self.dir_name + '\n')
        FreeCAD.Console.PrintLog('FemInputWriterCcx --> self.main_file_name  -->  ' + self.main_file_name + '\n')
        FreeCAD.Console.PrintMessage('FemInputWriterCcx --> self.file_name  -->  ' + self.file_name + '\n')

    def write_FELT_input_file(self):

        timestart = time.clock()

        inpfile = open(self.file_name, 'w')

        inpfile.write(example_input_file)
        inpfile.close()
        writing_time_string = "Writing time input file: " + str(round((time.clock() - timestart), 2)) + " seconds"
        FreeCAD.Console.PrintMessage(writing_time_string + ' \n\n')
        return self.file_name


example_input_file = '''problem description
title="Beam Sample Problem (Logan #5.5, p.188)"
nodes=3 elements=2

nodes
1  x=0 y=0 z=0 constraint=free force=point_load
2  x=240 y=0 z=0 constraint=roller
3  x=480 y=0 z=0 constraint=fixed

beam elements
1  nodes=[1,2] material=steel
2  nodes=[2,3]

material properties
steel E=3e+07 A=10 Ix=100

constraints
fixed Tx=c Ty=c Tz=u Rx=u Ry=u Rz=c
free Tx=u Ty=u Tz=u Rx=u Ry=u Rz=u
roller Tx=u Ty=c Tz=u Rx=u Ry=u Rz=u

forces
point_load Fy=-1000

end
'''

##  @}
