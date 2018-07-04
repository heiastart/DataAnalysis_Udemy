# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 14:15:15 2018

@author: heias
"""

import os, glob, pandas

def addField(indir='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\Extract'):
    os.chdir(indir)
    fileList = glob.glob('*')
    # print(fileList)
    
    for filename in fileList:
        df = pandas.read_csv(filename, sep='\s+', header=None)
        df['Station'] = [filename.rsplit('-', 1)[0]] * df.shape[0]
        df.to_csv(filename + '.csv', index=None, header=None, sep=';')