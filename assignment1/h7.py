import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = pd.read_csv("Simple_House_Price.csv")

plt.scatter(df["Area_sqft"], df["Price"])
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.title("Area vs House Price")

X = df[["Area_sqft"]]
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("Training percentage:", len(X_train) / len(df) * 100, "%")
print("Testing percentage:", len(X_test) / len(df) * 100, "%")

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)

print("Training actual shape:", y_train.shape)
print("Training predicted shape:", y_train_pred.shape)

y_test_pred = model.predict(X_test)

results = pd.DataFrame({
    "Area_sqft": X_test["Area_sqft"],
    "Actual Price": y_test,
    "Predicted Price": y_test_pred
})

results["Residual"] = results["Actual Price"] - results["Predicted Price"]

print("\nTest Results:")
print(results)

mae = mean_absolute_error(y_test, y_test_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
r2 = r2_score(y_test, y_test_pred)

print("\nMAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

if mae > rmse:
    print("MAE is larger:", mae)
else:
    print("RMSE is larger:", rmse)