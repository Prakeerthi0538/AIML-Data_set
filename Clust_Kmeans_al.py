# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 10:28:50 2023

@author: prake
"""

import pandas as pd
df=pd.read_excel(r"C:\Users\prake\Desktop\AIML\spy\cluster_Kmeans\kmeans1.xlsx")

df1=df.drop(["ID Tag","Model"],axis=1)

df.columns

df1=df1.drop(["Department"],axis=1)

df1.head()

from sklearn.cluster import KMeans
km=KMeans(n_clusters=2,init='k-means++',n_init=10)

km.fit(df1)

x=km.fit_predict(df1)

df['cluster']=x

df1=df.sort_values(['cluster'])
df1

df1.to_csv('KmeansPredicted.csv')