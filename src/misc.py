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