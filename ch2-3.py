
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dataset
temp = np.random.randint(0, 50, 5)
df = pd.DataFrame({'Temp': temp})
print(df)


# Calculate Q1, Q3 and IQR
Q1 = df['Temp'].quantile(0.25)
Q3 = df['Temp'].quantile(0.75)

IQR = Q3 - Q1


# Calculate lower and upper bounds
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR


# Detect all outliers
outliers = df.loc[
    (df['Temp'] < lower) |
    (df['Temp'] > upper)
]
print(outliers)


# Visualize using boxplot
plt.boxplot(df.Temp)
plt.title("Outlier Detection")
plt.ylabel("Temperature")
plt.show()


# Detect lower (negative) outliers
negative_outliers = df.loc[df['Temp'] < lower]
print("\nLower Outliers:")
print(negative_outliers)


# Detect upper (positive) outliers
positive_outliers = df.loc[df['Temp'] > upper]
print("\nUpper Outliers:")
print(positive_outliers)