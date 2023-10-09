# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:21:24 2023

@author: prake
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\data_pro_task4\data.csv") 

data.isna().sum()

li=['?']
d1=data[data.columns].isin(li).sum()

data.dropna(axis=1,inplace=True)

data.columns

data.describe()

data.dtypes

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

s=['cap-shape','cap-color','does-bruise-or-bleed','gill-color','stem-color','has-ring','habitat','season']
for i in s:
    data[i]=le.fit_transform(data[i])
    
x=np.array(data.iloc[ : ,1: ])
y=np.array(data.iloc[ : ,0])
 
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=2)

model.fit(xtrain, ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100

# model.predict('1.59','6','5','0','3','5.02','2.44','11','0','1','1')