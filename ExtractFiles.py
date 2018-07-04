# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 00:17:38 2018

@author: heias
"""

import os
import glob
import patoolib

def extractFiles(indir='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\rawData', out='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\Extract'):
    os.chdir(indir)
    
    # Make list of gz-files that we later can iterate through
    archives = glob.glob("*.gz")
    print(archives)
    
    if not os.path.exists(out):
        os.makedirs(out)
        
    # Check whether extracted files already exists using files variable
    files = os.listdir(out)
    for archive in archives:
        if archive[:-3] not in files:
            patoolib.extract_archive(archive, outdir=out)
            