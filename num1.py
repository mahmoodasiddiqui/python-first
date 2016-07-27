import numpy as np
'''a2 = np.array([1.,2.,3.,4.0,5.0])
print(a2.dtype)

a3 =np.array([0]*10)
print(a3)

a4=np.array(range(10))
print(a4)

a5 = np.zeros(10, dtype=int)
print(a5)

a6 = np.zeros(10)
print(a6)

m = np.arange(0, 20).reshape(5, 4)
print(m)
size1 = np.size(m,0)
size2 = np.size(m)
print(size1)
print(size2)

print(m[0])
print(m[0,2])
print(m[1,])
print(m[:,2])'''

a = np.array(5)
a = np.arange(5)
print(a<4)
#print(a<2 or a>3)
r = a<4
print(a[r])
s=np.sum(a<4)
print(s)

