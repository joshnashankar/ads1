# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 18:42:18 2023

@author: malle
"""
#importing libary functions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Reading csv file for the data
stock_data= pd.read_csv('stocks.csv')
#taking first five days of data by using .head
first_five_days=stock_data.head(5)
#using a function to call opening and closing variables and days high and low
def graph1(a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3):
    #ploting the graph using inbuilt function .plot
    plt.plot(first_five_days[a1],label=b1, linewidth = 2)
    plt.plot(first_five_days[a2],label=b2, linewidth = 2)
    plt.plot(first_five_days[a3],label=b3, linewidth = 2)
    plt.plot(first_five_days[a4],label=b4, linewidth = 2)
    #To use title and to plot on x-axis and Y-axis
    plt.xlabel(c1)
    plt.ylabel(c2)
    plt.title(c3)
    plt.legend()
    plt.grid()
    plt.show()
#Calling function for the variables to plot a line graph
graph1('Open','High','Low', 'Close','Open','High','Low', 'Close','first five days of stock','ranges of the stock','Opening and closing of first five days of a stock')