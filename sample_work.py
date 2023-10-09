# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:15:08 2023

@author: prake
"""
import pandas as pd
a=pd.Series([1,2,3,4])
b=pd.DataFrame([[1,2,3],[4,5,6]])
print("Series")
print(a)
print("Data Frame")
print(b)
c={'c':[1,2,3],'Python':[4,5,6]} #can determine a col only by its name in excel
d=pd.DataFrame(c)
print("Data Frame wiith col names")
print(d)
f=pd.DataFrame([[1,2,3],[4,5,6]],columns=['c','Python','Java'])
print("Data Frame with col names written seperately")
print(f)
g=pd.DataFrame([[1,2,3],[6,7,8]],
               columns=['C','Python','Java'],
               index=[5,6])
print(g)