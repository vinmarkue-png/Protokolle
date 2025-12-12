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
import espressomd
# import espressomd.interactions
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
import pathlib

TARGET_PATH = pathlib.Path("./")
FILE_SUFFIX = ".dat"

#######################################################################
#!!!!!!!!!!!!!!!!!!!!  Begin of changes !!!!!!!!!!!!!!!!!!!!!!!!!
#
dateiname='npt-out-3'   # dateiname bitte ändern
kommentar = "  "
#
# Interaction parameters (repulsive Lennard-Jones)
lj_eps=1
lj_sig=1
lj_cut=3

# Temp parameters´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´ 
start_temp = 0.2
end_temp = 2.5
step_temp = 0.01
n_temp = int((end_temp-start_temp)/step_temp)
tt=np.linspace(start_temp,end_temp,n_temp+1)

# System parameters
box = 10
n_part = 1000
pressure =0.1

# Integration parameters
n_cycles = 100
n_steps = 100


# Warmup parameters
warm_cycles=50   
warm_steps=100
cool_cycles=100
cool_steps=1000
#

######################  End of changes ###########################
#################################################################



gamma_v=0.0

target_filename=dateiname

def increment_filename_if_file_already_exists(target_filename, counter = 0):
    if target_filename.exists():
        new_filename = pathlib.Path(TARGET_PATH /f"{target_filename.stem.rsplit('_',1)[0]}_{counter+1}").with_suffix(FILE_SUFFIX)
        return increment_filename_if_file_already_exists(new_filename, counter + 1)
    else:
        return target_filename

target_filename = pathlib.Path(TARGET_PATH / target_filename).with_suffix(FILE_SUFFIX)
new_filename = increment_filename_if_file_already_exists(target_filename)
print(new_filename)
#datei = open(dateiname, 'a')
datei = open(new_filename, 'a')    

required_features = ["NPT", "LENNARD_JONES"]
espressomd.assert_features(required_features)
system = espressomd.System(box_l=3 * [box])
np.random.seed(seed=42)
#
system.time_step = 0.005
system.cell_system.skin = 0.4
system.non_bonded_inter[0, 0].lennard_jones.set_params(
    epsilon=lj_eps, sigma=lj_sig, cutoff=lj_cut, shift="auto")
#system.bonded_inter[0] = espressomd.interactions.HarmonicBond(k=5.0, r_0=1.0)


for i in range(n_part):
    part1 = system.part.add(pos=np.random.random(3) * system.box_l)

system.integrator.set_steepest_descent(f_max=0.0, gamma=30.0,
                                       max_displacement=0.1)
system.integrator.run(warm_cycles*warm_steps)
# print("E after minimization:", system.analysis.energy()["total"])

system.integrator.set_isotropic_npt(ext_pressure=pressure, piston=0.01)
system.thermostat.set_npt(kT=0.0, gamma0=0.9, gammav=0.01, seed=42)
system.integrator.run(cool_cycles*cool_steps)

print(" ")
print("# Epsilon=",lj_eps, ", Sigma=",lj_sig, ", Cutoff=",lj_cut, ", Particles=", n_part, sep="")
print("# pressure=",pressure, ", warm_cycles=",warm_cycles, ", warm_steps=",warm_steps, ", cool_cycles=",cool_cycles, ", coll_steps=",cool_steps,", n_cycles=",n_cycles,", n_steps=",n_steps,
      ", gamma_v=",gamma_v, sep="" )
print("#")


xData = []
yData = []

# dt = datetime.datetime.now()
# dateiname=dateiname+dt.strftime("_%Y-%m-%d-%H:%M")+".dat"

#datei = open(dateiname, 'a')
# datei = open(new_filename, 'a')  

#
datei = open(new_filename, 'w')
datei.write("Epsilon=" + str(lj_eps) + ", Sigma=" + str(lj_sig) + ", Cutoff=" + str(lj_cut) + ", Particles=" + str(n_part)
            + ", pressure=" + str(pressure) + "\n")
datei.write( "warm_cycles=" + str(warm_cycles) + ", warm_steps=" + str(warm_steps)+ ", cool_cycles=" + str(cool_cycles) + ", cool_steps=" + str(cool_steps)+
             ", n_cycles=" + str(n_cycles)  + ", n_steps=" + str(n_steps) + ",  gamma_v=" + str(gamma_v) + "\n")
datei.write("Kommentar: " + kommentar  + "\n\n")
#
datei.write( "temp \t  vol \t pressure \t time \n" )
datei.close()
#datei.write("Epsilon=" + str(lj_eps))

anfang=time.time()

def integrate(temp):
    for ii in range(0,n_cycles,1):
        system.integrator.run(n_steps)

 
def main():    
     for temp in tt:
        system.thermostat.set_npt(kT=temp, gamma0=1.0, gammav=gamma_v, seed=42)
        system.integrator.set_isotropic_npt(ext_pressure=pressure, piston=0.01)
        integrate(temp)
        P = system.analysis.pressure()['total']
#        
        
        rechenzeit=round(time.time()-anfang,1)
        
        
#        print("Temperature:", temp, "Pressure:", P, "Box:", system.box_l)
        volume=system.box_l[0]*system.box_l[1]*system.box_l[2]
        print("T=",temp.round(5), ", volume=",volume.round(2), ", pressure =", P.round(4),     ", time=",rechenzeit,"s", sep="")
        #d        xData.append(temp)
        yData.append(volume)
        datei = open(new_filename, 'a')
        datei.write(str(round(temp,3)) + "\t" + str(volume.round(4))+ "\t" + str(P.round(4)) + "\t" + str(rechenzeit)+ "\n")
        datei.close()
  
#    
#         plt.plot(xData,yData)
#         plt.draw()
#         plt.pause(0.01)
#         plt.xlabel("temperature")
#         plt.ylabel("volume")
      
 
main()

