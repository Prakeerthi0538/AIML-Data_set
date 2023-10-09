# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:31:08 2023

@author: prake
"""

# CLASSIFICATION PROJECT ON IRIS DATASET...


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\iris_pro\iris.csv")       #data collecting

#data understanding
data.shape
print(data)
data.isna().sum()
data.describe()
#correlation matrix
# there are 3 types of correlation
# 1. positive     ->if one is increasing other also increase and decrease also..
#2. Negative      ->if one increases other decreases and vice vers
# 3. Zero correlation    -> no relation between 2 features
# alwayes lies btw +1.00 to -1.00

a=data.corr()
plt.matshow(a)
plt.colorbar()
plt.show()

#no need of pre- processing steps as it is already a cleaned one

# getting the accuracy after intentionally deleting 2 rows in pl col
# Either delete that 2 rows or replace the cells with 0,1,mean, or any thing else...
data.fillna(data['pl'].mean(),inplace=True)

#Adding a new column to the dataframe data and inserting their index numbers as elements
data['index_val']=np.arange(0,150)
# for this we wll take x and y as follows...

#Model building

#the data should be in the form of matrix only 

#there are 2 methods of converting data into numpy array

x=np.array(data.iloc[ : , :-1])
y=data.iloc[ : ,-1].values
x.shape
y.shape

x1=np.array(data.iloc[ : , [0,1,2,3,5]])
y1=np.array(data.iloc[ : , -2])
# By using sklearn package we can divide the train and test dataset from the data
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=1)
#random_state makes the same data set for training every time when we execute

xtrain.shape
ytrain.shape

xtest.shape
ytest.shape

#importing the KNN algoritm....
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

#Training and Testing starts...
model.fit(xtrain,ytrain)

#After training asking the algoritm to predict the y vals for xtest 
#part and store in ypred
ypred=model.predict(xtest)

#by importing accuracy_score we will get the accuracy 
from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)*100

#kvalue test_size random_state are to be changed for geting the accuracy
#these aare not fixed just trail and error method

#Training and Testing ends ...

model.predict([[5.3,3.0,2.0,2.1],[5.4,4.1,3.0,1.5]])
# array(['Iris-setosa', 'Iris-versicolor'], dtype=object)

model.predict([[2.1,2.2,1.5,0.2],[7.9,3.8,6.9,2.2]])
#array(['Iris-setosa', 'Iris-virginica'], dtype=object)



