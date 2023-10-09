# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:28:24 2023

@author: prake
"""

import numpy as np
import pandas as pd

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\city_power_task5\Tetuan City power consumption.csv")

data.columns

data.describe

data.isna().sum()

data.dtypes

data['DateTime']=pd.to_datetime(data['DateTime'])
data['year'] = data['DateTime'].dt.year
data['month'] = data['DateTime'].dt.month
data['day'] = data['DateTime'].dt.day
data['hour'] = data['DateTime'].dt.hour
data['minute'] = data['DateTime'].dt.minute

data.drop(['DateTime'],axis=1,inplace=True)

x=np.array(data.iloc[ : ,[0,1,2,3,4,8,9,10,11,12]])
y=np.array(data.iloc[ : ,[5,6,7]])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import mean_squared_error
import math
math.sqrt(mean_squared_error(ytest, ypred))