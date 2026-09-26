import numpy as np

data = np.array([
    [10, -20, 30], 
    [40, -50, 60], 
    [70, 80, -90]])

print("Mean of row:",np.mean(data, axis=1))
print("Mean of col:",np.mean(data, axis=0))
print("STD of row:",np.std(data, axis=1))
print("Min value of row:",np.min(data, axis=1))
print("Min value of col:",np.min(data, axis=0))