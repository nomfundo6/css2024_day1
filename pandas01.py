# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:17:22 2024

@author: sikha
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())

import pandas
file_2 = pandas.read_csv("iris.csv")
print(file_2)

print(file_2.info())
print(file_2.describe())

import pandas 
file_3 = pandas.read_csv("diab_data.csv")
print(file_3)

print(file_3.info())
print(file_3.describe())


file_4 = pandas.read_csv("housing_data.csv")
print(file_4)
#There were no column names; come back to this

print(file_4.info())
print(file_4.describe())


file_5 = pandas.read_csv("insurance_data.csv", skiprows=5)
print(file_5)
# Did not work before because there was a whole bunch of unnecessary rows.

print(file_5.info())
print(file_5. describe())