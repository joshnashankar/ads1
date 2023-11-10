#importing libary functions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Reading csv file for the data
df= pd.read_csv('Adult_Tobacco_Consumption_In_The_U.S.__2000-Present.csv')
#taking first five days of data by using .head
def data_tobacco(tobacco,x_label,y_label):
#counts the different type of tobacco
    counts = df[tobacco].value_counts().sort_index()
#plot a bar graph using counts value
    plt.bar(counts.index, counts.values,width = 0.5)
    plt.legend()
#Adding lables and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title('Type of tobacco')
    plt.show()
#calling variables in data_tobacco
data_tobacco('Topic','type of tobacco','number of persons')