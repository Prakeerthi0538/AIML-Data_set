# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:59:07 2023

@author: prake
"""

# Reading a file using pandas

import pandas as pd
data=pd.read_csv(r'C:\Users\prake\Desktop\AIML\IMDB-Movie-Data.csv')
print(data)
data.head(10)# to 10 rows
data.tail()# last 5 rows
data.shape # returns no.of rows,cols
data.columns# returns only cols names
data.index# returns the indexes

s=data.append(data)
# to add data to the data set use append.. better to not maodify the original dataset
print(data.shape)
print(s.shape)

s.drop_duplicates(inplace=True)
# here this command removes duplicate and also inplace=T means it saves changes in s itself
print(s.shape)

data.describe()# to describe all cols but should be Number type

data['Rank'].describe() # describes a specific col

data.isna() # is empty or not in form of bool type

data.isna().sum() # to find out how many empty cells by doing sum on isna data

data.dropna(inplace=True) # to delete the row having empty space

data.dropna(axis=1,inplace=True) # to delete cols having empty spaces

data.drop(['Rank','Title'],axis=1,inplace=True)# to delete  a specific col(s)

data.fillna(1,inplace=True) #to replace empty cxells with 1, we can give any nymber inplace of 1
data.isna().sum()

data['Metascore'].fillna(data['Metascore'].mean(),inplace=True)
# replacing Metascore with avg of that particular col
data.isna().sum()

data['Revenue (Millions)'].fillna(data['Revenue (Millions)'].mean(),inplace=True)
# replacing Revenue (Millions) with avg of that particular col
data.isna().sum()

data['Director'].unique() #to get unique elements in a col

data['Director'].value_counts()# to get the repeated count of every element

print(data.shape)

data['Rank'].replace(to_replace=1,value=10,inplace=True)
# Replace the data of given col name as the number to be replaced and with what 
#value it hass to be replaced in the same data set
data.head()# to check the data if it has changed or not we use this command

data.loc[100] #it is a row refference, it gives the details of the row when we give index number as loc
data['Rank']
data.iloc[:,:2]# it is a col reference, it returns cols by its index as loc

data[data['Rating']>8.0].count()
# compares the entire data set that having greater then 8.0 and prints the count of each col

data[data['Year']==2008].sum()# to get the sum of something[revenue] in a particular year

data[(data['Year']==2015) & (data['Rating']>8.0)].count()
#TO check the movies released in 2015 and having rating more than 8.0 and its count
# can check many coditions at a time
# &  -->AND
# |  -->OR

z=data.sort_values(['Year']) #sorts the data set by given condition(can use many cinditions)

import numpy as np
a=np.arange(0,1000)
data['sample']=a

data['verdict']=data['Rating'].apply(lambda x: 'Good' if x>6.0 else 'Bad')
# Creates a new col named verdict with the given condition as rating greater then 6.0

data['Datetime']=pd.date_range('2023-01-01 6:00',periods=1000)
# Creates a new col with coresponding date and time

data['date']=pd.to_datetime(data['Datetime']).dt.day

data['Month']=pd.to_datetime(data['Datetime']).dt.month

data['Yrs']=pd.to_datetime(data['Datetime']).dt.year









