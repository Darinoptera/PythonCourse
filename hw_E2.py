import numpy as np
s =np.random.pareto(3, 1000)
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 50, density=True)
plt.show()
count, bins, ignored = plt.hist(s, 50, cumulative=True)
plt.show()
