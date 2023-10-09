# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 10:09:19 2023

@author: prake
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv(r"C:\Users\prake\Desktop\AIML\spy\task3\spotify.csv",encoding='unicode_escape')

#data preprocessing...
data.head
data.columns
data.isna().sum()

data['key'].value_counts()
data['key'].fillna(data['key'].mode()[0],inplace=True)

data['in_shazam_charts'].value_counts()
data['in_shazam_charts'].fillna(10,inplace=True)

data.isna().sum()
data.describe()
data.info()


#data visualization
df=pd.DataFrame(data)

df['streams'] = pd.to_numeric(df['streams'], errors='coerce', downcast='integer').astype('Int64')
df['streams_in_millions']=df['streams']/1000000
df['streams_in_millions'].fillna(1.0,inplace=True)
df['detailed_name']=df['track_name'].astype(str) +"("+ df["artist(s)_name"]+")"

# #Top 10 most streaming songs with artist name...
# fig,ax=plt.subplots(figsize=(25,8))
# plt.xticks(rotation=45, ha="right")
# sns.barplot(data=df.sort_values('streams_in_millions', ascending=True).head(10),x='detailed_name',y='streams_in_millions')
# plt.xlabel('Song Name')
# plt.ylabel('Stream in million')
# plt.title('Top 10 Most-Streamed Songs')
# plt.show()


plt.figure(figsize= (8, 6))
plt.
#lable encoding for object type...
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

s=['streams','key','mode']
for i in s:
    df[i]=le.fit_transform(df[i])

#converting object type to int 64..
df['in_deezer_playlists']=pd.to_numeric(df['in_deezer_playlists'], errors='coerce', downcast='integer').astype('Int64')
df['in_shazam_charts']=pd.to_numeric(df['in_shazam_charts'], errors='coerce', downcast='integer').astype('Int64')


#selecting columns for visualization..
#data visualization for column in_apple_charts ...
#plot to show apple charts distribution
plt.figure(figsize=(16, 8))
sns.distplot(df.in_apple_charts,bins=20)
