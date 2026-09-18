import pandas as pd
import numpy as np
from numpy import random 
import matplotlib.pyplot as plt

temp = np.random.randint(0,50,5)
cu = np.random.randint(10,35,5)
data = {'Temp' : temp, 'CU' : cu}
df = pd.DataFrame(data)
print(df)


# add a new column
df["Percent"] = [43,54,49,57,40]
print(df)


# column based on existing column
df["Process"] = 10 + df["CU"]/100
print(df)


# min and max -- of a specific column (CU => column name)
print(df.CU.min())
print(df.CU.max())
# ------- OR ------- #
print(df["CU"].min())
print(df["CU"].max())


# values with a condition -- of a specific column
print(df[df.CU < 15])
print(df[df.CU >= 25])


# some operations
print("Sum:", df["Temp"].sum())
print("Count:", df["Temp"].count())
print("Average:", df["Temp"].mean())
print("Middle value:", df["Temp"].median())
print("Standard deviation:", df["Temp"].std())
print("Variance:", df["Temp"].var())


# total non-missing values
print(df["Temp"].count())
# Counts how many times each unique value occurs
print(df["Temp"].value_counts())


# If temperature is > 30 → "high", else "low"
df["class"] = np.where(df["Temp"] > 30, "high", "low")
print(df)


# Save selected columns & make new csv file
new_df = df[["Temp", "Percent", "class"]]
new_df.to_csv("students_new.csv", index=False)