#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Chris Thompson

@pythonVersion: 3.8

@description: This is a script to analyze review data from Angry Metal Guy.
"""
#####################################
#IMPORT MODULES
#####################################
import pandas as pd
%matplotlib inline

#####################################
#GLOBAL VARIABLES
#####################################


#####################################
#USER-DEFINED FUNCTIONS
#####################################


#####################################
#RUN SCRIPT
#####################################
if __name__ == "__main__":
    df = pd.read_csv('amg_reviews_3.csv')
    print(df.shape)
        
    df["Date"] = pd.to_datetime(df["Date"])
    print(df.head())
    
    df["day"] = df["Date"].dt.day
    df["month"] = df["Date"].dt.month
    df["year"] = df["Date"].dt.year
    
    
    recent = df.loc[(df['year'] >= 2018)]
        
    recent_reviews = recent.groupby(recent["year"]).count()["Album"]
    
    print(recent_reviews.plot(x= 'Year', 
           y= 'Reviews', 
           kind='line',
           figsize = (20,10), 
           title="Total Reviews by Year",
           grid=True , 
           style = 'r'))
    
    print("Total reviews hit a peak in 2019, but have fallen since then.")
    