import pandas as pd
import os

Input_file = r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output\sales_clean.csv"
Output_folder = r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output"

os.makedirs(Output_folder, exist_ok=True)

df = pd.read_csv(Input_file)
print("Dataset loaded successfully!")

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()
avg_discount = df["Discount"].mean()
profit_margin = (total_profit / total_sales) * 100
avg_order_value = df.groupby("Order ID")["Sales"].sum().mean()

# Top States & Products

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

top_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

# Prepare KPI summary (flat data)

kpi_summary = {
    "Total Sales": [round(total_sales, 2)],
    "Total Profit": [round(total_profit, 2)],
    "Total Quantity Sold": [int(total_quantity)],
    "Average Discount": [round(avg_discount, 4)],
    "Profit Margin (%)": [round(profit_margin, 2)],
    "Average Order Value": [round(avg_order_value, 2)],
}

# Save outputs as CSV files

kpi_df = pd.DataFrame(kpi_summary)
kpi_df.to_csv(os.path.join(Output_folder, "kpi_summary.csv"), index=False)
print(" Files saved successfully:")
print(" - kpi_summary.csv")
