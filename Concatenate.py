# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:54:15 2018

@author: heias
"""

import os,glob,pandas

def concatenate(indir='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\Extract', outfile='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\Extract\\Concatenated.csv'):
    os.chdir(indir)
    fileList = glob.glob('*.csv')
    # print(fileList)
    dfList = []
    colNames = ['Year','Month','Day','Hour','Temp','DewTemp','Pressure','WindDir','WindSpeed','Sky','Precip1','Precip6','ID']
    for filename in fileList:
        print(filename)
        df = pandas.read_csv(filename, header=None, sep=';')
        dfList.append(df)
    
    concatDf = pandas.concat(dfList)
    concatDf.columns = colNames
    concatDf.to_csv(outfile, index=None, sep=';')
    
