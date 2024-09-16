import numpy as np
vector = np.array([1,2,2])
print(vector)

#shape array
print(vector.shape)
print(vector.dtype)

zeros = np.array([12,123,123])
print(zeros)


one =np.ones(5)
print(one)

arr = np.arange(10,20,5)
print(arr)


rar = np.random.rand(5)
print(rar)


print('''==================================================''')

print(min(rar))
print(rar.min())

print('''==================================================''')

print(max(rar))
print(rar.max())

print('''==================================================''')

print(rar.argmax())
print(rar.argmin())

print('''==================================================''')

print(rar.mean())
print(rar.std())

print('''==================================================''')
arr2d = np.array([[1,2,2],[1,2,3]])
print(arr2d)
print('''==================================================''')
print(arr2d[0])
print('''==================================================''')
print(arr2d[0,:])
print('''==================================================''')
print(arr2d[:,0])