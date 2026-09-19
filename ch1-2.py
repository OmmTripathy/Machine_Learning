import pandas as pd
import numpy as np
from numpy import random 
import matplotlib.pyplot as plt


temp = np.random.randint(0,50,5)
cu = np.random.randint(10,35,5)
data = {'Temp' : temp, 'CU' : cu}
df = pd.DataFrame(data)


plt.subplot(2, 2, 1)                         # Top-left
plt.bar(df["Temp"], df["CU"])
plt.title("Temperature vs CPU")

plt.subplot(2, 2, 2)                         # Top-right
plt.hist(df["Temp"], color = "green")
plt.title("Temperature Distribution")

plt.subplot(2, 2, 3)                         # Bottom-left
plt.boxplot(df["CU"])
plt.title("CPU Box Plot")

plt.subplot(2, 2, 4)                         # Bottom-right
plt.scatter(df["Temp"], df["CU"], color = "pink")
plt.title("Temp vs CPU Scatter")

plt.tight_layout()
plt.show()