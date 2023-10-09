# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 10:40:29 2023

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

# -------------------------------------------------------------------------------------

from sklearn.neighbors import KNeighborsClassifier
model1=KNeighborsClassifier(n_neighbors=2)

model1.fit(xtrain,ytrain)

ypred1=model1.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred1)*100

# Accuracy   98.82106366256222

# -------------------------------------------------------------------------------------

from sklearn.tree import DecisionTreeClassifier
model2=DecisionTreeClassifier()

model2.fit(xtrain,ytrain)

ypred2=model2.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred2)*100

# Accuracy   98.44773382237359

# -----------------------------------------------------------------------------------------

from sklearn.ensemble import RandomForestClassifier
model3=RandomForestClassifier()

model3.fit(xtrain,ytrain)

ypred3=model3.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred3)*100

# Accuracy    99.52187581870578

# -------------------------------------------------------------------------------------------