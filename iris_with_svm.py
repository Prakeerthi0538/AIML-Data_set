# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:17:33 2023

@author: prake
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\iris_pro\iris.csv")

a=plt.scatter(data['sl'],data['class'])
plt.show()

b=plt.scatter(data['sw'],data['class'])
plt.show()

c=plt.scatter(data['pl'],data['class'])
plt.show()

d=plt.scatter(data['pw'],data['class'])
plt.show()

e=plt.scatter(a,b)
plt.show()

x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25,random_state=1)

# SVC for classsification...SVR for regression...
from sklearn.svm import SVC
model=SVC(kernel='linear')

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest,ypred)*100


model.predict([[5.3,3.0,2.0,2.1],[5.4,4.1,3.0,1.5]])