import numpy as np
import ase
from ase import Atoms
from ase.build import fcc110, bcc111
from ase.visualize import view
from ase.io import read, write
import geometry as gm
from misc import read_files
from numpy.random import randint, uniform

nano_collection = read_files()

N_particles = 10

particles = []
for i in range(N_particles):
    r = randint(0, len(nano_collection))
    part_i = nano_collection[r]
    part_i.set_center_of_mass([uniform(-100, 100),uniform(-100, 100), 50])
    particles.append(part_i)        
    
def assemble(particles):
    assembly = Atoms()
    for i in range(len(particles)):
        assembly+=particles[i]
        
    return assembly


slab = fcc110("Au", size = (200, 200, 2))

ass = assemble(particles)
ass+=slab