# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:02:59 2023

@author: prake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\Crime_data\location_crime.csv")

data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')
    
data['timestamp'] = pd.to_datetime(data['timestamp'], format = '%d-%m/%Y %H:%M:%S')



column_new = data.iloc[:,0]

db=pd.DataFrame({"year": column_new.dt.year,
              "month": column_new.dt.month,
              "day": column_new.dt.day,
              "hour": column_new.dt.hour,
              "dayofyear": column_new.dt.dayofyear,
              "week": column_new.dt.week,
               "weekofyear": column_new.dt.weekofyear,
              "dayofweek": column_new.dt.dayofweek,
              "weekday": column_new.dt.weekday,
              "quarter": column_new.dt.quarter,
             })

newdataset=data.drop('timestamp',axis=1)
data1=pd.concat([db,newdataset],axis=1)
data1=data1.dropna()

data1.shape

x=data1.iloc[:,[1,2,3,4,6,16,17]].values
y=data1.iloc[:,[10,11,12,13,14,15]].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=9)
    
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


from sklearn import metrics
metrics.accuracy_score(y_test,y_pred)*100

model.predict(x[[100]])