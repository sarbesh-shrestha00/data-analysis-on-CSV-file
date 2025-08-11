import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales.csv")  # Change to your file name

#  Show first few rows
print(df.head())

#  Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)

# Plot sales by category
category_sales.plot(kind="bar", title="Sales by Category")
plt.ylabel("Total Sales")
plt.show()

# Sales by Month
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\nSales by Month:\n", monthly_sales)

# Plot sales by month
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.show()
