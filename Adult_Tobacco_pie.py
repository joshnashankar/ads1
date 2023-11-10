# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:42:18 2023

@author: malle
"""


#importing libary function to plot and to read variables
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#using function to call Measure from the file
def Tobacco_consumption(Type_of_tobacco, title):
    #reading csv file for the data
    U_S_tobacco_consumption = pd.read_csv('Adult_Tobacco_Consumption_In_The_U.S.__2000-Present.csv')
    #using .pie which is inbulit fuction for the pie chart and here we count the different type of tobacco users
    plt.pie(U_S_tobacco_consumption[Type_of_tobacco].value_counts().values, labels = U_S_tobacco_consumption[Type_of_tobacco].value_counts().index, autopct='%1.1f%%')
    plt.title(title)
    plt.show()
#calling variables in the pie which are used in def function 
Tobacco_consumption('Measure','Number of people using different type of tobacco in U.S')