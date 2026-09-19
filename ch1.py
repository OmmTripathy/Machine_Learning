import pandas as pd
import numpy as np
from numpy import random 
import matplotlib.pyplot as plt


temp = np.random.randint(0,50,5)
cu = np.random.randint(10,35,5)
data = {'Temp' : temp, 'CU' : cu}
df = pd.DataFrame(data)


df["usage"] = np.where(df["CU"] > 20, "high", "low")
df["Temp_Status"] = np.where(df["Temp"] > 30, "Hot", "Normal")
df["Load_Index"] = df["Temp"] * df["CU"] / 100
print(df)


# display the value on top of each bar in a bar graph
bars = plt.bar(df["Temp"], df["CU"])
plt.bar_label(bars)
plt.show()


# 1. Bar graph
plt.bar(df["Temp"], df["CU"])
plt.xlabel("Temperature (°C)")
plt.ylabel("CPU Utilization (%)")
plt.title("CPU Utilization at Diff Temps")
plt.show()


# 2. Pie chart
usage_count = df["usage"].value_counts()
plt.pie(usage_count, labels = usage_count.index, autopct = "%1.1f%%")
plt.title("High vs Low CPU Usage")
plt.show()


# 3. Histogram - Temperature
plt.hist(df["Temp"], bins = 5, edgecolor = "black")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.title("Temperature Distribution")
plt.show()


# 6. Box plot - CPU utilization
plt.boxplot(df["CU"])
plt.ylabel("CPU Utilization (%)")
plt.title("CPU Utilization Box Plot")
plt.show()


# 7. Scatter plot - Temperature vs CPU
plt.scatter(df["Temp"], df["CU"])
plt.xlabel("Temperature (°C)")
plt.ylabel("CPU Utilization (%)")
plt.title("Temperature vs CPU Utilization")
plt.show()


# 8. Line graph - CPU readings
plt.plot(df.index, df["CU"], marker = "o")
plt.xlabel("Reading Number")
plt.ylabel("CPU Utilization (%)")
plt.title("CPU Utilization Across Readings")
plt.show()


# 10. Compare temperature and CPU using two lines
plt.plot(df.index, df["Temp"], marker = "o", label = "Temp")
plt.plot(df.index, df["CU"], marker = "s", label = "CPU Utilization")

plt.xlabel("Reading Number")
plt.ylabel("Value")
plt.title("Temperature and CPU Comparison")
plt.legend()
plt.show()