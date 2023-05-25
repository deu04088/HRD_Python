import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi * 2, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), 'r-')
plt.plot(x, np.cos(x), 'b:')

fig.savefig('sin_cos_fig.png')