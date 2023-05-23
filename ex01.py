import numpy as np
list_a = list()
for i in range(20):
    list_a.append(i)
numpy_a = np.array(list_a)
print(numpy_a)    
print(type(numpy_a))

list_new_a = [i for i in range(20)]
print(f'list_new_a : {list_new_a}')
numpy_new_a = np.array(list_new_a)
print(numpy_new_a)