import pandas as pd

df = pd.read_csv(r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\data\SampleSuperstore.csv",encoding='ISO-8859-1')
print("file loaded successfully")

print("\ndataset shape:")
print(f"Rows: {df.shape[0]} | columns: {df.shape[1]}")

print("\nfirst 5 rows:")
print(df.head().to_string(index=False))

print("\nColumn names:")
print(list(df.columns))

print("\nData types:")
print(df.dtypes)

print("\nMissing values")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

#Convert 'Order Date' & 'Ship Date' to datetime

date_cols = ["Order Date", "Ship Date"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col],errors='coerce',dayfirst=False)

invalid_order = df[df["Order Date"].isna()]
invalid_ship = df[df["Ship Date"].isna()]

if not invalid_order.empty:
    print(f"Found {len(invalid_order)} rows with invalid Order Date. Dropping them.")
    df = df.dropna(subset=["Order Date"])

if not invalid_ship.empty:
    print(f"Found {len(invalid_ship)} rows with invalid Ship Date. Dropping them.")
    df = df.dropna(subset=["Ship Date"])

print("Both Order Date and Ship Date converted successfully.")

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month_Name"] = df["Order Date"].dt.strftime("%b")

df["Ship_Year"] = df["Ship Date"].dt.year
df["Ship_Month"] = df["Ship Date"].dt.month
df["Ship_Month_Name"] = df["Ship Date"].dt.strftime("%b")

invalid_sales = df[df['Sales'] < 0]
invalid_profit = df[df['Profit'] < -10000]

print(f"Invalid Sales Rows: {len(invalid_sales)}")
print(f"Invalid Profit Rows (< -10,000): {len(invalid_profit)}")

# Drop columns not needed for analysis

cols_to_drop = ["Row ID", "Postal Code"]
df.drop(columns=cols_to_drop,inplace=True,errors='ignore')

print(df.shape[1])
print(list(df.columns))

Output_file = r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output\sales_clean.csv"
df.to_csv(Output_file,index=False)
print("cleaned dataset saved")