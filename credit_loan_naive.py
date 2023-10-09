# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:53:02 2023

@author: prake
"""

import pandas as pd
import numpy as np

a=[i for i in 'ABCDEFGHIJKLMNOP']
data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\credit_approval\credit_loan(1).csv",names=a)

data.shape
data.isna().sum()

li=['?']
d1=data[data.columns].isin(li).sum()


data['A']=data['A'].str.replace('?',data['A'].mode()[0])
data['B']=data['B'].str.replace('?','0.01')
data['D']=data['D'].str.replace('?',data['D'].mode()[0])
data['E']=data['E'].str.replace('?',data['E'].mode()[0])
data['F']=data['F'].str.replace('?',data['F'].mode()[0])
data['G']=data['G'].str.replace('?',data['G'].mode()[0])
data['N']=data['N'].str.replace('?',data['N'].mode()[0])

# data['A']=data['A'].str.replace('?',data['A'].max())
# data['B']=data['B'].str.replace('?','0.01')
# data['D']=data['D'].str.replace('?',data['D'].max())
# data['E']=data['E'].str.replace('?',data['E'].max())
# data['F']=data['F'].str.replace('?',data['F'].max())
# data['G']=data['G'].str.replace('?',data['G'].max())
# data['N']=data['N'].str.replace('?',data['N'].mode()[0])

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

s='ADEFGIJLM'
for i in s:
    data[i]=le.fit_transform(data[i])
    
x=np.array(data.iloc[ : , :-1])
y=np.array(data.iloc[ : ,-1])


# # -----------------------------------------------------------------------------
# # KNN WITHOUT MIN_MAX_SCALING......

# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

# from sklearn.neighbors import KNeighborsClassifier
# model=KNeighborsClassifier(n_neighbors=3)

# model.fit(xtrain,ytrain)

# ypred=model.predict(xtest)

# from sklearn.metrics import accuracy_score
# accuracy_score(ytest, ypred)*100

# -----------------------------------------------------------------------------
# KNN WITH MIN_MAX_SCALING.....

from sklearn.preprocessing import MinMaxScaler
scaled=MinMaxScaler()
scaledx=scaled.fit_transform(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(scaledx,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100
# -----------------------------------------------------------------------------
# KNN WITH standerdization.....

from sklearn.preprocessing import StandardScaler
scaled=StandardScaler()
scaledx=scaled.fit_transform(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(scaledx,y,test_size=0.2,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100

# -----------------------------------------------------------------------------
# NAIVE_BAYES.....

# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

# from sklearn.naive_bayes import GaussianNB
# model=GaussianNB()
# model.fit(xtrain,ytrain)

# ypred=model.predict(xtest)

# from sklearn.metrics import accuracy_score
# accuracy_score(ytest, ypred)*100

# # -----------------------------------------------------------------------------
# # LOGISTIC REGRESSION.......

# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)

# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()

# model.fit(xtrain,ytrain)

# ypred=model.predict(xtest)

# from sklearn.metrics import accuracy_score
# accuracy_score(ytest, ypred)*100

# Y=(X-MEAN)/SD         ---->standerdization...


