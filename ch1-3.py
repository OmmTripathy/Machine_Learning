import numpy as np
import matplotlib.pyplot as plt


nd = np.random.normal(0, 1, 10000)    
# 0 → mean of the normal distribution, 1 → standard deviation of the normal distribution.
ud = np.random.uniform(-2, 2, 10000)  
# low = -2, high = 2 → range of the uniform distribution.


# Plot histograms
# Normal distribution
plt.subplot(1, 2, 1)
plt.hist(nd, bins = 40, color = 'red', edgecolor = 'black')  # bins = 40 → number of intervals in each histogram.
plt.title("Normal Distribution (mean=0, std=1)")

# Uniform distribution
plt.subplot(1, 2, 2)
plt.hist(ud, bins = 40, color = 'blue', edgecolor = 'black')
plt.title("Uniform Distribution (-2 to 2)")

plt.show()



# plt.subplot(rows, columns, position)
# 1 → Number of rows
# 2 → Number of columns
# 1 or 2 → Position of the plot