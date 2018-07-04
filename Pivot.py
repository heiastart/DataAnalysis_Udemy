# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:10:16 2018

@author: heias
"""
import pandas, numpy

def pivot(infile="C:\\out\\Concatenated-Merged.csv",outfile="C:\\out\\Pivoted.csv"):
    df=pandas.read_csv(infile)
    df=df.replace(-9999,numpy.nan)
    df['Temp']=df["Temp"]/10.0
    table=pandas.pivot_table(df,index=["ID"],columns="Year",values="Temp")
    table.to_csv(outfile, sep=';')
    

    
    