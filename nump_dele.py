import numpy as np
a=np.arange(1,17).reshape(4,4)
print(a)
b=np.delete(a,2,axis=1)
print(b)
