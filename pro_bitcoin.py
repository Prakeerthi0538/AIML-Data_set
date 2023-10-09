# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:43:39 2023

@author: prake
"""

import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\bitcoin_pro\bitcoin.csv")
df.head()


df.drop(['Date'],1,inplace=True)


predictionDays = 30

# Create another column shifted 'n'  units up
df['Prediction'] = df[['Price']].shift(-predictionDays)


# show the first 5 rows
df.head()
df.tail()


# Create the independent data set
# Here we will convert the data frame into a numpy array and drp the prediction column
x = np.array(df.drop(['Prediction'],1))
# Remove the last 'n' rows where 'n' is the predictionDays
x = x[:len(df)-predictionDays]
print(x)

# Create the dependent data set
# convert the data frame into a numpy array
y = np.array(df['Prediction'])
# Get all the values except last 'n' rows
y = y[:-predictionDays]
print(y)

import sklearn
# Split the data into 80% training and 20% testing
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size = 0.2,random_state=4)

# set the predictionDays array equal to last 30 rows from the original data set

predictionDays_array = np.array(df.drop(['Prediction'],1))[-predictionDays:]
print(predictionDays_array)


from sklearn.svm import SVR
# Create and Train the Support Vector Machine (Regression) using radial basis function
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.00001)

svr_rbf.fit(xtrain, ytrain)

# print the predicted values
svm_prediction = svr_rbf.predict(xtest)
print(svm_prediction)
print()
print(ytest)


from sklearn.metrics import mean_squared_error
import math
print(math.sqrt(mean_squared_error(
    ytest,svm_prediction)))



#future prediction
print(svr_rbf.predict([[10585.66211]]))