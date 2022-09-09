import numpy as np
import ase
from ase import Atoms, Atom
from ase.build import fcc110, bcc111
from ase.visualize import view
from ase.io import read, write, Trajectory
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.md.verlet import VelocityVerlet
from ase.constraints import FixAtoms
from ase import units
import geometry as gm
from misc import read_files, height, assemble
from numpy.random import randint, uniform

nano_collection = read_files()

r = randint(0, len(nano_collection))
slab = fcc110("Au", size = (20, 20, 3))

slab_x = max(slab.positions[:,0])   #x extreme of slab
slab_y = max(slab.positions[:,1])   #x extreme of slab

N_nano = 15
particles = []
for i in range(N_nano):
    r = randint(0, len(nano_collection))
    particles.append(nano_collection[r])
    

for i in range(0,N_nano):
    particles[i].translate([uniform(5,slab_x - gm.max_distance(particles[i])), uniform(5,slab_y- gm.max_distance(particles[i])), 150])
    particles[i].set_velocities([0,0,-0.05])
    no_collision = True
    
    while(no_collision):
        if(height(particles[i], slab) <= gm.max_distance(particles[i])+1):
            no_collision = False
            break
        
        for j in range(0,i):
            dist_ij = gm.distance(particles[i], particles[j])
            if (abs(dist_ij) <= gm.max_distance(particles[i]) +gm.max_distance(particles[j])):
                no_collision = False
                break
            else:
                no_collision = True
        particles[i].translate([0,0,-0.1])
        

ass = assemble(particles)
sys = ass + slab
write("../sys.xyz", sys)
#view(nano+slab)
# nano.set_velocities([0,0,-0.01])
# slab.set_constraint()
# system = nano + slab
# system.set_calculator(EMT())
# dyn = VelocityVerlet(system, timestep=5.0 * units.fs,trajectory="md.traj")
# dyn.run(500)

