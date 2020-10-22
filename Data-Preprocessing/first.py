#!usr/bin/env python3
#coding: utf-8
"""
Created on Thu Oct 2020

@author: mharikmert
"""
#libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
print(data)

height = data['boy'] # can be used one bracket for one column
height = data[['boy']]
print(height)

height_weight = data[['boy', 'kilo']] # can not be used one bracket for two column
print(height_weight)
