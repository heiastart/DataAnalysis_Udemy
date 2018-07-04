# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 14:35:46 2018

@author: heias
 
"""

import os
from ftplib import FTP, error_perm

def ftpDownloader(stationID, startYear, endYear, url="ftp.pyclass.com", user="student@pyclass.com", passwd="student123"):
    ftp = FTP(url)
    ftp.login(user, passwd)
    if not os.path.exists('C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy'):
        os.makedirs('C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy')
    os.chdir('C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy')
    
    for year in range(startYear, endYear+1):
        # Path of file we want to download
        fullpath = '/Data/%s/%s-%s.gz' % (year, stationID, year)
        filename = os.path.basename(fullpath)
        
        # Create a local empty file for the data from ftp-server to be stored in
        try:
            with open(filename,'wb') as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
                print('%s successfully downloaded' % filename)
        except error_perm:
            # For files not present on the server
            print('%s is not available!' % filename)
            os.remove(filename)
    ftp.close()
        
        
    
      