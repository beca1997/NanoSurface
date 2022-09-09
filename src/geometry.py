#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 12:45:13 2022

@author: giacomobecatti
"""
from ase import Atoms
import numpy as np
def max_distance(atoms: Atoms):
    """
    

    Parameters
    ----------
    atoms : Atoms
        The Atoms object (from ASE) containing the positions of every single atom

    Returns
    -------
    dist_max : Float
        Returns the distance between the atom lacated further away from the center of mass.
        Useful to obtain a sort of effective radius of the nanoparticle
    """
    N = len(atoms.positions)
    dist = np.zeros(N)
    com = atoms.get_center_of_mass()
    for i in range(N):
        dist_i_vec = atoms.positions[i] - com
        dist_i_x = dist_i_vec[0]
        dist_i_y = dist_i_vec[1]
        dist_i_z = dist_i_vec[2]
        dist2 = dist_i_x * dist_i_x + dist_i_y * dist_i_y + dist_i_z * dist_i_z
        dist[i] = np.sqrt(dist2)
    dist_max = np.max(dist)
    return dist_max


def distance(nano1: Atoms, nano2:Atoms):
    """
    

    Parameters
    ----------
    nano1 : Atoms
        The first nanoparticle (or other ASE Atoms object)
    nano2 : Atoms
        The second nanoparticle (or other ASE Atoms object)

    Returns
    -------
    distance: Float
        Returns the distance between two nanoparticles (or other ASE atoms objects)

    """
    com_1 = nano1.get_center_of_mass()
    com_2 = nano2.get_center_of_mass()
    dist_vec = com_1 - com_2
    dist = np.sqrt(np.sum(dist_vec*dist_vec))
    return dist
    
    