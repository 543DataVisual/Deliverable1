#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:51:42 2023

@author: annareeder
"""
import pandas as pd

location='https://github.com/reederan/543-1/raw/main/'
file= 'copy_tractassignments.csv'

tractcsv=pd.read_csv(location + file)

tractcsv.head()

tractcsv.columns

stay=[]