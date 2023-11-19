import numpy as np
import matplotlib.pyplot as plt

dat = np.random.rand(2,100)
plt.plot(dat[:][0],dat[:][1],'co')
plt.ylabel('Y')
plt.ylabel('X')
plt.show()