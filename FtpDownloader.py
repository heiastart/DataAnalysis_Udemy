# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 00:35:41 2018

@author: Øyvind Sørlie
"""

from ftplib import FTP
import os

def ftpDownloader(filename,host='ftp.pyclass.com',user='student@pyclass.com',passwd='student123'):
    ftp = FTP(host)
    ftp.login(user,passwd)
    ftp.cwd("Data")
    os.chdir("C://Users//heias//AnacondaProjects//DataAnalysis_Udemy/")
    with open(filename,'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)