import matplotlib.pyplot as plt
import numpy as np

(fig, ax) = plt.subplots(nrows=2, ncols=2)

X = np.random.randn(100)
Y = np.random.randn(100)
ax[0,0].scatter(X, Y)

X = np.arange(10)
Y = np.random.uniform(1, 10, 10)
ax[0,1].bar(X,Y)

X = np.linspace(0, 10, 100)
Y = np.cos(X)
ax[1,0].plot(X, Y)

Z = np.random.uniform(1, 10, (400, 400))
ax[1,1].imshow(Z)

plt.show()