# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:48:13 2023

@author: prake
"""

import numpy as np
import pandas as pd

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\forest_fires\fires.csv")

data.shape
data.columns
data.isna().sum()

x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.1,random_state=2)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100