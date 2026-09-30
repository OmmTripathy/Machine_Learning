import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

study_hours = np.random.uniform(1, 10, 100)
test_score = 35 + 6 * study_hours + np.random.normal(0, 5, 100)
test_score = np.clip(test_score, 0, 100)

df = pd.DataFrame({
    "Study Hours": study_hours,
    "Test Score": test_score
})

X = df[["Study Hours"]]
y = df["Test Score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)

m = model.coef_[0]
c = model.intercept_

print("Slope:", m)
print("Intercept:", c)
print(f"Test score = {m:.2f} × Study Hours + {c:.2f}")

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

results = pd.DataFrame({
    "Study Hours": X_test["Study Hours"].values,
    "Actual Test Score": y_test.values,
    "Predicted Test Score": y_pred
})

print("\nResults:")
print(results)

results.to_csv("linearregressionpredictions.csv", index=False)

plt.scatter(X_test["Study Hours"], y_test, label="Actual")
plt.plot(X_test["Study Hours"], y_pred, label="Regression Line")
plt.title("Simple Linear Regression: Study Hours vs Test Score")
plt.xlabel("Study Hours")
plt.ylabel("Test Score")
plt.legend()
plt.grid()
plt.show()