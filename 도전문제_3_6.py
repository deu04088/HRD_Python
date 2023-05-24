# arange()를 사용하여 1 ~ 50까지의 원소를 가지는 다차원 배열을 만들자, 이 배열의 원소 
# 50개를 랜덤하게 섞어 80%는 train_data에, 20%는 test_data에 넣어 이 두 배열을 반환
# 하는 함수 train_test_split()을 만들자. 반환된 배열 값을 각각 출력하라.

import numpy as np

def train_test_split(data):
    np.random.shuffle(data)

    train_data = []
    test_data = []

    for i in range(1, len(data) + 1):
        if (i / len(data) * 100) <= 80:
            train_data.append(data[i-1])
        else:
            test_data.append(data[i-1])
            
    print(train_data, test_data, sep ='\n')

# 아래 함수가 강사님이 짜신 파이썬에 가까운 함수
# def train_test_split(data):
#     np.random.shuffle(data)

#     size = int(len(data)*0.8)
#     train_data = data[:size]
#     test_data = data[size:]
            
#     print(train_data, test_data, sep ='\n')
    
num = np.arange(1, 51)
train_test_split(num)


