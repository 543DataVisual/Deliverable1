#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:51:42 2023

@author: annareeder
"""
import pandas as pd

##loading in the data
location='https://github.com/reederan/543-1/raw/main/'
file= 'copy_tractassignments.csv'

tractcsv=pd.read_csv(location + file)


##checking to see what needs to be cleaned 
tractcsv.columns
tractcsv.community_center.value_counts()

##subsetting the data
tractcsv = tractcsv[['tract','community_center','per_cap_income','total_non_english']]
tractcsv

##removing the space that is creating the issue
tractcsv.community_center.str.strip()
tractcsv.community_center=tractcsv.community_center.str.strip()
tractcsv
##resaving the data

tractcsv.to_csv("cleanedtractsfile3.csv", index=False)
