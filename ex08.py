import matplotlib.pyplot as plt
import numpy as np

# x = [0, 1, 2, 3]
# data = [1, 2, 3, 4, ]
# plt.plot(x, data)
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.show()

# x = [i for i in np.linspace(0, 10, 1_000)]
# print(x)
# y = [i ** 2 for i in x]
# print(y)
# plt.plot(x, y)
# plt.axis([0, 10, 0, 10])
# plt.show()


x = np.arange(-20, 20)
y1 = 2 * x
y2 = (1/3) * x ** 2 + 5
y3 = -x ** 2 -5
plt.plot(x, y1, 'g--', x , y2, 'r^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])
plt.show()