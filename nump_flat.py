import numpy as np
a=np.arange(1,10).reshape(3,3)
print(a)
##a=a.flatten()
##a=a.flatten(order='c')# default to get single elements by row
a=a.flatten(order='F') #F to get col wise
print(a)
