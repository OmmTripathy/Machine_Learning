import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Products": ["Laptop", "Mobile", "Smartwatch", "Headphones"],
    "Price": [80000, 30000, 10000, 5000],
    "Sales": [50, 100, 80, 150],
    "Profit": [12000, 8000, 2500, 1500],
}
df = pd.DataFrame(data)


# Scatter Plot
plt.scatter(df.Price, df.Sales)
plt.xlabel("Price")
plt.ylabel("Sales")
plt.title("Price vs Sales")

id = df["Sales"].idxmax()
plt.plot(
    df.loc[id, "Price"],
    df.loc[id, "Sales"],
    '+r',
    mew=2,
    ms=12
)
plt.show()


# Line Plot
plt.plot(df.Sales, df.Profit, 'k*--')
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.title("Sales vs Profit")
plt.show()


# Bar Graph
bars = plt.bar(df.Products, df.Profit)
plt.bar_label(bars)
plt.xlabel("Products")
plt.ylabel("Profit")
plt.title("Profit Graph")
plt.show()


# Bar Graph 
df["profit_margin"] = (df["Profit"]/df["Sales"]) * 100
bars = plt.bar(df.Products, df.profit_margin)
plt.bar_label(bars)
plt.xlabel("Products")
plt.ylabel("Profit margin")
plt.title("Profit as Percent of Sales")
plt.show()


# Pie Chart
plt.pie(df["Sales"], labels=df["Products"], autopct='%1.2f%%')
plt.show()


# Histogram
plt.hist(df.Sales, bins=3, color="skyblue", edgecolor="black")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Distribution of Sales")
plt.show()