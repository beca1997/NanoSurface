import numpy as np
import ase
from ase import Atoms
from ase.build import fcc110, bcc111
from ase.visualize import view
from ase.io import read, write
import geometry as gm
from os import listdir
from os.path import isfile, join



nanocoll = []
onlyfiles = [f for f in listdir("../models/") if isfile(join("../models/", f))]
for i in range(len(onlyfiles)):
    nano = read("../models/"+onlyfiles[i])
    nanocoll.append(nano)

    

