import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float)
y = np.array([[5,6],[7,8]], dtype=np.float)

print(x + y)
print(np.add(x, y))

print(x - y)

print(x * y)
print(np.multiply(x, y))

print(x / y)

print(np.sqrt(x))

v = np.array([9,10])
w = np.array([11, 12])

print(np.dot(v, w))

print(np.dot(x, v))

print(np.dot(x, y))

x = np.array([[1,2],[3,4]])

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

