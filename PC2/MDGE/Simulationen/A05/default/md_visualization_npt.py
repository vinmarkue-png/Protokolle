#
# Copyright (C) 2010-2022 The ESPResSo project
#
# This file is part of ESPResSo.
#
# ESPResSo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ESPResSo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Visualize particle dumbbells in the NpT ensemble (constant temperature,
constant pressure, variable volume).
"""

import numpy as np
import matplotlib.pyplot as plt
import threading

import espressomd
import espressomd.interactions
import espressomd.visualization
#

#######################################################################
#!!!!!!!!!!!!!!!!!!!!  Begin of changes !!!!!!!!!!!!!!!!!!!!!!!!!
#
# Interaction parameters (repulsive Lennard-Jones)
lj_eps = 1.0
lj_sig = 1.0
lj_cut = 3.0 * lj_sig

# Temperature parameters
start_temp = 0.0
end_temp = 10
step_temp = 0.1

# System parameters
box = 10
n_part = 500
pressure=0.1

# Integration parameters
n_cycles=30
n_steps=30

# Warmup and cool parameters
warm_cycles=50
warm_steps=50
cool_cycles=50
cool_steps=500
#
######################  End of changes ###########################
#################################################################

#
#
#
required_features = ["NPT", "LENNARD_JONES"]
espressomd.assert_features(required_features)

system = espressomd.System(box_l=3 * [box])

np.random.seed(seed=42)

visualizer = espressomd.visualization.openGLLive(
    system, background_color=[1, 1, 1], bond_type_radius=[0.2])

system.time_step = 0.0005
system.cell_system.skin = 0.1

system.non_bonded_inter[0, 0].lennard_jones.set_params(
    epsilon=lj_eps, sigma=lj_sig, cutoff=lj_cut, shift="auto")


for i in range(n_part):
    part1 = system.part.add(pos=np.random.random(3) * system.box_l)


# print("E before minimization:", system.analysis.energy()["total"])
system.integrator.set_steepest_descent(f_max=0.0, gamma=30.0,
                                       max_displacement=0.1)
system.integrator.run(100) 

# print("E after minimization:", system.analysis.energy()["total"])

system.integrator.set_isotropic_npt(ext_pressure=pressure, piston=0.01)

n_temp = int((end_temp-start_temp)/step_temp)
tt=np.linspace(start_temp,end_temp,n_temp+1)

temp=0
temp1=0.2
system.thermostat.set_npt(kT=temp1, gamma0=1.0, gammav=0.01, seed=42)
print("moderate warming\n")
for i in range(warm_cycles):
    system.integrator.run(warm_steps)
print("cooling\n")
system.thermostat.set_npt(kT=temp, gamma0=1.0, gammav=0.01, seed=42)
for i in range(cool_cycles):
    system.integrator.run(cool_steps)

def update(temp):
    system.thermostat.set_npt(kT=temp, gamma0=1.0, gammav=0.01, seed=42)
    for i in range(0,n_cycles,1):
        system.integrator.run(n_steps)
        visualizer.update()

def main():
    print("\nStarting heating process.\n")
    for temp in tt:
        update(temp)
        P = system.analysis.pressure()['total']
        print("Temp:", temp.round(4), ", Box:", system.box_l.round(4))


# Start simulation in separate thread
t = threading.Thread(target=main)
t.daemon = True
t.start()
visualizer.start()


