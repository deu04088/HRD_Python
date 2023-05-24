# 연립방정식의 해를 numpy.linalg의 solve() 함수를 사용하여 구하여라

import numpy as np

a = np.array([[1, 1, -1], [2, -1, 3], [1, 2, 1]], dtype = 'int32')
b = np.array([0, 9, 8])
s = np.linalg.solve(a, b)
print(s)

# 행렬 a의 행렬식
print(f'{np.linalg.det(a):.2f}')     
print('{:.2f}'.format(np.linalg.det(a)))