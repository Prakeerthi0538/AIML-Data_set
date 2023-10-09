# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:07:16 2023

@author: prake
"""

import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\class_lungpro\survey lung cancer.csv")

data.shape
data.isna().sum()
data.columns

# Converting string of male to 0 and Female to 1...it is a preprocessing step....
# Its just for 2 categories...
data['GENDER']=data['GENDER'].map({"M":0,"F":1})

# What if the are n number of classes...for that we use a package from sklearn called...
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
data['GENDER']=le.fit_transform(data['GENDER'])

x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=10)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest,ypred)*100


