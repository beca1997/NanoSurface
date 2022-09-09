#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:48:46 2022

@author: giacomobecatti
"""
from os import listdir
from os.path import isfile, join
from ase.io import read, write
from ase import Atoms


def read_files():
    """
    Used to obtain a list containing all the nanoparticles from the model folder 

    Returns
    -------
    nanocoll : List of Atoms
        List of ASE Atoms each representing one of the nanoparticles from the "model" folder

    """
    nanocoll = []
    onlyfiles = [f for f in listdir("../models/") if isfile(join("../models/", f))]
    for i in range(len(onlyfiles)):
        nano = read("../models/"+onlyfiles[i])
        nanocoll.append(nano)
    return nanocoll

def assemble(particles):
    """
    Assemble a list of Atoms into a single Atoms object for simulation and visualization

    Parameters
    ----------
    particles : List of atoms
        List of atoms objects to be combined into singo ASE Atoms object

    Returns
    -------
    assembly : Atoms 
        THe ASE Atoms object resulting from combining all atoms in list

    """
    assembly = Atoms()
    for i in range(len(particles)):
        assembly+=particles[i]
        
    return assembly

def height(nano: Atoms, slab: Atoms):
    """
    Determines the height of the nanoparticle center of mass above the slab

    Parameters
    ----------
    nano : Atoms
        DESCRIPTION.
    slab : Atoms
        DESCRIPTION.

    Returns
    -------
    height : TYPE
        DESCRIPTION.

    """
    nano_z = nano.get_center_of_mass()[2]
    slab_z = max(slab.get_positions()[:,2])
    
    height = nano_z - slab_z
    return height