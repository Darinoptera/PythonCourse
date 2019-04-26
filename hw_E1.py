import numpy as np
s = np.random.poisson(5, 10000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 15, density=True)
plt.show()
count, bins, ignored = plt.hist(s, 15, cumulative=True)
plt.show()
