# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 22:54:42 2018

@author: heias
"""
import simplekml


def kml(lon, lat):
    kml = simplekml.Kml()
    kml.newpoint(name='Sample', coords=[(lon,lat)])
    kml.save('C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\KML\\sample.kml')
    
longitude = float(input('Please enter longitude: '))
latitude = float(input('Please enter latitude: '))
kml(longitude,latitude)

print('You have created a kml-file for the given coordinates')
