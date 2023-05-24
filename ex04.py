import numpy as np

a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([2, 3, 4])

print(a + b)
print(a * b)

print(np.eye(4) * 10)

a = np.linspace(0, 10, 5)
print(a)