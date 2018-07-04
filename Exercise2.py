# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:02:07 2018

@author: heias
"""

import os,pandas

def addCurrency(indir='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\txt_csv'):
    os.chdir(indir)
    df = pandas.read_csv('Income1984_SemicolonSep.csv', sep=';')
    # print(df)
    df['1984 Euros'] = df['1984']*0.88
    df['1984 Pounds'] = df['1984']*0.6
    df['1984 Kroner'] = df['1984']*8.04
    df.to_csv('Income1984_multCurrency.csv', index=0, sep=';')