# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 17:39:34 2025

@author: Shwet
"""
#import libraries
import numpy as np
import pandas as pd

#load dataset
df=pd.read_csv("C:/Users/Shwet/Downloads/hospital_records_2021_2024_with_bills.csv")
df

#check it head and dtypes
df.head()
df.dtypes



#creating copy of original dataset
df1=df.copy()
df1

#convert  dtype object to datetime
df1['Date of Birth']=pd.to_datetime(df1['Date of Birth'])
df1['Date of Birth']

#check it duplicate rows
df1.duplicated().sum()
df1.T.duplicated().sum()

#check it missing values
df1.isnull().sum()

df1.to_csv('Hospital Record')
df1
