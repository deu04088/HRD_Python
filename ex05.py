import numpy as np
from math import sin

a = np.logspace(0, np.pi, 11).round(10)
result = []
for i in a:
    result.append(sin(i))
print(np.pi)
print(a, end = '\n\n')
print(result)