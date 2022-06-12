import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)
y = -5 + x*x
fig, ax = plt.subplots()
ax.plot(x,y,linewidth=2.0)
ax.set(xlim=(-10,10), xticks=np.arange(-5,5), ylim=(-20,20), yticks=np.arange(-10,10))
plt.show()