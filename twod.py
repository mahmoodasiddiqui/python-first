import numpy as np
m = np.arange(0, 20).reshape(5, 4)
print(m)
print(m[:,0])
print(m[:,1])
print(m[:,2])
print(m[:,1:3])
n = m.ravel()
print(n)



