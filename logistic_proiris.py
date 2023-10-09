# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 10:56:40 2023

@author: prake
"""

import numpy as np
import pandas as pd
import mathplotlib.pyplot  as plt

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\logistic_iris\iris1.csv")

x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,train_size=0.5,random_state=5)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()

model.fit(xtrain, ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100
