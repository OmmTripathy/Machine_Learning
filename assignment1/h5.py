import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

study_hours = np.random.uniform(1, 10, 100)
test_score = 35 + 6 * study_hours + np.random.normal(0, 5, 100)
test_score = np.clip(test_score, 0, 100)

df = pd.DataFrame({
    "Study Hours": study_hours,
    "Test Score": test_score
})
print(df)

print("Number of samples:", df.shape[0])
print("Number of features:", 1)
print("Number of target variables:", 1)
print("Feature name:", "Study Hours")
print("Target:", "Test Score")
print("Shape:", df.shape)
print("Data types:\n", df[["Study Hours"]].dtypes)

print("\nStatistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

plt.scatter(df["Study Hours"], df["Test Score"])
plt.title("Study Hours vs Test Score")
plt.xlabel("Study Hours")
plt.ylabel("Test Score")