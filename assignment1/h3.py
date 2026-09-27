import numpy as np
import pandas as pd

data = {
    "Products": ["Laptop", "Mobile", "Smartwatch", "Headphones"],
    "Price": [80000, 30000, 10000, 5000],
    "Sales": [50, 100, 80, 150],
    "Profit": [12000, 8000, 2500, 1500],
}

df = pd.DataFrame(data)

print("----- Product Sales Data -----")
print(df)

print("\nColumns:", df.columns)

print("Rows & Columns:", df.shape)

print("\n----- First 3 Products -----")
print(df.head(3))

print(df[["Sales", "Profit"]])

print("\n----- Sales Statistics -----")
print("Average Sales:", df["Sales"].mean())
print("Maximum Sales:", df["Sales"].max())
print("Minimum Sales:", df["Sales"].min())

print("\n----- Products with Profit > 4000 -----")
print(df[df["Profit"] > 4000])

print("\n----- Products Sorted by Profit -----")
print(df.sort_values("Profit", ascending=False))