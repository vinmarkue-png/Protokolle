#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:42:50 2023

@author: dilger
"""

import numpy as np
import espressomd
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
import pathlib

TARGET_PATH = pathlib.Path("./")
FILE_SUFFIX = ".dat"

######################################################################
#!!!!!!!!!!!!!!!!!!!!  Begin of changes !!!!!!!!!!!!!!!!!!!!!!!!!
#
dateiname='nvt-out_task_2'           # Dateinamen bitte ändern
kommentar = " "

# dt = datetime.datetime.now()
# dateiname=dateiname+dt.strftime("_%Y-%m-%d-%H:%M")+".dat"


# Interaction parameters (repulsive Lennard-Jones)
#############################################################
epsilon =.0104*1.602*10**-19        # J
sigma = 0.34*10**-9     

lj_eps = 1.0
lj_sig = 1.0
lj_cut = 3.0 * lj_sig


# Temp parameters
start_temp = 0.25
end_temp = 1
step_temp = 0.01
n_temp = int((end_temp-start_temp)/step_temp)
tt=np.linspace(start_temp,end_temp,n_temp+1)

density_factor=1.0
density = 6.23*10**23/8.314/300*10**5*density_factor
# particle density at 1 bar and 300 K
n = density*sigma**3   # Particles in the box
n_part = 1000
box_l=(n_part/n)**(1/3)  #  Bpx size for 1 bar, 300 K an 1000 particles
# box = 10   not neccesarry

# warmup integration (steepest descent)
warm_cycles = 50
warm_steps = 100
cool_cycles = 100
cool_steps = 10000

# Integration parameters
n_cycles = 200
n_steps = 4000


#
######################  End of changes ###########################
#################################################################

gamma_0=0.2

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



datei.write("Epsilon=" + str(lj_eps) + ", Sigma=" + str(lj_sig) + ", Cutoff/Sigma =" + str(lj_cut/lj_sig) + ", Particles=" + str(n_part) +"\n")  
datei.write( "n_cycles=" + str(n_cycles) + ", n_steps=" + str(n_steps) + ", warm_cycles=" + str(warm_cycles) +", warm_steps=" + str(warm_steps) +
             ", cool_cycles=" + str(cool_cycles) +", cool_steps=" + str(cool_steps) + ", gamma_0=" + str(gamma_0) +  "\n")
datei.write("Kommentar: " + kommentar + "\n\n")
datei.write( "temp \t  pressure \t time \n" )
datei.close()


#############################################################
#  Setup System                                             #
#############################################################
system = espressomd.System(box_l=[box_l] * 3)
np.random.seed(seed=42)

system.time_step = 0.01
system.cell_system.skin = 0.4

system.non_bonded_inter[0, 0].lennard_jones.set_params(
    epsilon=lj_eps, sigma=lj_sig, cutoff=lj_cut, shift="auto")

# convergence criterion (particles are separated by at least 90% sigma)
min_dist = 0.9 * lj_sig

required_features = ["LENNARD_JONES"]
espressomd.assert_features(required_features)


# Particle setup
#############################################################
volume = box_l**3

for i in range(n_part):
    system.part.add(pos=np.random.random(3) * system.box_l)

act_min_dist = system.analysis.min_dist()

# minimize energy using min_dist as the convergence criterion
system.integrator.set_steepest_descent(f_max=0, gamma=1e-3,
                                       max_displacement=lj_sig / 100)
i = 0
while i < warm_steps and system.analysis.min_dist() < min_dist:
    system.integrator.run(warm_cycles)
    i += 1

system.integrator.set_vv()

#  activate.thermostat
system.thermostat.set_langevin(kT=1.0, gamma=1.0, seed=42)

for i in range(warm_steps):
    system.integrator.run(warm_cycles)
    
system.thermostat.set_langevin(kT=start_temp-0.2, gamma=1.0, seed=42)   
for i in range(cool_steps):
    system.integrator.run(cool_cycles)

system.thermostat.set_langevin(kT=start_temp-0.1, gamma=1.0, seed=42)   
for i in range(cool_steps):
    system.integrator.run(cool_cycles)
    
system.thermostat.set_langevin(kT=start_temp-0.05, gamma=1.0, seed=42)   
for i in range(cool_steps):
    system.integrator.run(cool_cycles)    
  
anfang=time.time()

#############################################################
#      Integration                                          #
#############################################################
#
def integration():
    P=0
    for ii in range(n_steps):
        system.integrator.run(steps=n_cycles)
        P += system.analysis.pressure()['total']
        pressure= P/(ii+1)
    return pressure
#    
def main():
     xData=[]
     yData=[]
     for temp in tt:
         P=0
         pressure=0   
         system.thermostat.set_langevin(kT=temp, gamma=gamma_0, seed=42)   
         pressure = integration()
         rechenzeit=round(time.time()-anfang,1)        
#          print(temp, pressure)
         print("temp=",temp.round(5), ", pressure=",pressure.round(6), ", time=",rechenzeit,"s", sep="")
#        
         xData.append(temp)
         yData.append(pressure)
         datei = open(new_filename, 'a')
         datei.write(str(temp.round(4)) + "\t" + str(pressure.round(8))+ "\t" + str(rechenzeit)+"\n")
         datei.close()
#             
#          plt.plot(xData,yData)
#          plt.draw()
#          plt.pause(0.01)
#          plt.xlabel("temperature")
#          plt.ylabel("volume")
#       
main()

