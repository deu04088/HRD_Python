import numpy as np
sample = np.array([[1, 1], [2, 2], [3, 3]])
print(sample, end = '\n\n')

# flat 하게 출력
b = np.insert(sample, 1, 4)        # insert(순서 array, index 위치, 넣을 값) 
print(b, end = '\n\n')

# 행의 값에 4를 추가
c = np.insert(sample, 1, 4, axis = 0) 
print(c, end = '\n\n')

# 열의 값에 4를 추가
d = np.insert(sample, 1, 4, axis = 1) 
print(d, end = '\n\n')

# flatten 평탄화
e = sample.flatten()
print(e, end = '\n\n')

# 전치(행, 열 순서 교환)
f = sample.T
print(f, end = '\n\n')


flip_sample = np.array([[1,2,3], [4,5,6]])
# 열을 기준으로 뒤집기
g = np.flip(flip_sample, axis = 1)  
print(g, end = '\n\n')

# 행을 기준으로 뒤집기
h = np.flip(flip_sample, axis = 0) 
print(h, end = '\n\n')


a = np.array([10, 20, 30])
print(a)
new_a = a.astype(dtype = np.float64)
print(new_a, end = '\n\n')


# 열 방향 동작
i = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
i.sort(axis = 1)
print(i, end = '\n\n')

# 행 방향 동작
j = np.array([[35, 24, 55], [69, 19, 9], [4, 1, 11]])
j.sort(axis = 0)
print(j)