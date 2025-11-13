# step04_visual_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# 1 Load the cleaned dataset

INPUT_FILE = r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output\sales_clean.csv"
OUTPUT_DIR = r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output\visuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)


try:
    df = pd.read_csv(INPUT_FILE, parse_dates=["Order Date", "Ship Date"])
    print(f"Loaded cleaned dataset successfully — Rows: {len(df)}")
except FileNotFoundError:
    print("ERROR: sales_clean.csv not found. Please run Step 2 first.")
    exit()


# 2 Monthly Sales Trend

df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o", color="teal")
plt.title("Monthly Sales Trend", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/monthly_sales_trend.png")
plt.close()

# 3 Sales by Category

category_sales = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar", color="skyblue")
plt.title("Sales by Category", fontsize=14)
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/sales_by_category.png")
plt.close()

# 4 Top 10 Products by Profit

top_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_products.plot(kind="barh", color="seagreen")
plt.title("Top 10 Products by Profit", fontsize=14)
plt.xlabel("Total Profit")
plt.ylabel("Product Name")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/top10_products_profit.png")
plt.close()

# 5 Sales by Region

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7, 5))
region_sales.plot(kind="bar", color="salmon")
plt.title("Sales by Region", fontsize=14)
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/sales_by_region.png")
plt.close()

# 6 Profit vs Discount

plt.figure(figsize=(8, 5))
plt.scatter(df["Discount"], df["Profit"], alpha=0.5, color="orange")
plt.title("Profit vs Discount", fontsize=14)
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/profit_vs_discount.png")
plt.close()

# 7 Completion Message

print("All visuals created successfully!")
print("Step 4 complete — Charts saved to:", OUTPUT_DIR)
