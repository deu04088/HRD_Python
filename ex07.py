import numpy as np

# 다차원 배열을 위한 행렬 곱셈 
# append() 활용
a = np.array([1, 2, 3])
b = np.array([[4, 5, 6], [7, 8, 9]])
c = np.append(a, b)
print(c, end = '\n\n')
d = np.append([a], b, axis = 0)
print(d, end = '\n\n')

# numpy의 matmul() 활용
a = np.array([[1,2], [3, 4]])
b = np.array([[10, 20], [30, 40]])

# 각 위치에 따라 원소 간의 곱셈
print(a * b, end = '\n\n')  

#일반적인 행렬곱
print(np.matmul(a, b), end = '\n\n')    
print(a @ b, end = '\n\n')


# reshape()
c = np.arange(12)   # 0 ~ 11까지의 수열 저장
print(c, end = '\n\n')
print(c.reshape(3, 4), end = '\n\n')    # 3x4 행렬로 데이터 구조 변형