import numpy as np
##a=np.array([[1,2,3],[5,6,7]])
##print(a)
##print('\n')
##b=np.append(a,[[4,8,9]],axis=0)# 0 for performing op on row wise
##print(b)
##print('\n')
##b=np.append(a,[[4],[8]],axis=1)#1 col wise
##print(b)
##a=np.arange(1,17).reshape(4,4)
##print(a)
##b=np.insert(a,1,[[1,1,1,1]],axis=0)
##print(b)
a=np.arange(1,17).reshape(4,4)
print(a)
b=np.insert(a,1,[[1],[1],[1],[1]],axis=1)
print(b)
