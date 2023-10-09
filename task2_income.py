# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:53:41 2023

@author: prake
"""

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\task2\income.csv")

#Pre-processing steps...
data.shape
data.columns

#taking a named a and passing the column names to the list
a=[i for i in 'ABCDEFGHIJKLMNO']
data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\task2\income.csv",names=a)

data.columns

# data['B'].value_counts()

#to check how many cols are having ? 
l1=[' ?']
d1=data[data.columns].isin(l1).sum()

#checking if the value of a rows in a column is '?' and replacing it with the mode value of that column
for col in data.columns:
    for i in range(len(data[col])):
        if isinstance(data[col][i], str) and data[col][i].strip().startswith('?'):
            data[col][i] = pd.NA
mode_values=data.mode().iloc[0]          
data.fillna(mode_values,inplace=True) 

# To check if there are any empty spaces or not
data.isna().sum()

#converting the string tyoe data into numerical data
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
# data[['B','D','F','G','H','I','J','N']]=data[['B','D','F','G','H','I','J','N']].apply(le.fit_transform)

s='BDFGHIJN'
for i in s:
    data[i]=le.fit_transform(data[i])

#separating the independent and dependent value by converting them into arrray 
x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])

#taking 80% data for traing
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

#importing the knn algorthim and giving the k size=10 to increase the accuracy
# from sklearn.neighbors import KNeighborsClassifier
# model=KNeighborsClassifier(n_neighbors=10)

# #Making the algoritm train on given dataset..
# model.fit(xtrain,ytrain)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(xtrain,ytrain)

#asking the algoritm to predict on xtest data
ypred=model.predict(xtest)

#Comparing the ytest and ypred to get the accuracy...
from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100

# # For predicting new data....
# model.predict([[47,	4,	51835,	14,	15	,2	,10, 5,	4,	0,	0,1902,60,16]])
# model.predict([[50,	1,	251585,	9,	13,	0,	4,	1,	4,	1,	0,	0,	55,	38]])
# model.predict([[49,	4,	160187,	6,	5,	3,	8,	1,	2,	0,	0,	0,	16,	23]])

a=[i for i in 'ABCDEFGHIJKLMNO']
data1=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\task2\income.csv",names=a)
data1.drop(['O'],axis=1,inplace=True)
l1=[' ?']
d1=data1[data1.columns].isin(l1).sum()

for col1 in data1.columns:
    for i in range(len(data1[col1])):
        if isinstance(data1[col1][i], str) and data1[col1][i].strip().startswith('?'):
            data1[col1][i] = pd.NA
mode_values=data1.mode().iloc[0]          
data1.fillna(mode_values,inplace=True) 

# data1['B'].value_counts()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
# s='BDFGHIJN'
for i in s:
    data1[i]=le.fit_transform(data1[i])
    
test=model.predict(data1)


