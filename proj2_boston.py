# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 11:29:05 2023

@author: prake
"""

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\boston.csv")
# As of now we dont have col names in the dataset, if we print cols ...
data.columns
# we will get output of 1st row as the col names

# To add explicit col names in a row .. we do this..
a=[i for i in 'ABCDEFGHIJKLMN']
data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\boston.csv",names=a)
data.columns

# Data is already been pre_processed...

#Model building...
x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])

x.shape
y.shape

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=1)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(xtrain, ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import mean_squared_error
import math
math.sqrt(mean_squared_error(ytest, ypred))


