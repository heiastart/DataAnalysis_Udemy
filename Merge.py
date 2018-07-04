# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 20:03:35 2018

@author: heias
"""

import pandas

def merge(left='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\join\\Concatenated.csv', right='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\join\\station-info.txt', output='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\join\\Concat-merged.csv'):
    leftDf = pandas.read_csv(left, sep=';')
    rightDf = pandas.read_fwf(right, converters={'USAF':str,'WBAN':str})
    rightDf['USAF_WBAN'] = rightDf['USAF'] + '-' + rightDf['WBAN']
    mergedDf = pandas.merge(leftDf, rightDf.loc[:,['USAF_WBAN', 'STATION NAME', 'LAT', 'LON']], left_on='ID', right_on='USAF_WBAN')
    mergedDf.to_csv(output, sep=';')
    
