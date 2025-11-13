import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load the cleaned data
sales = pd.read_csv(r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output\sales_clean.csv")

# Prepare data for forecasting
sales['Order Date'] = pd.to_datetime(sales['Order Date'])

# Group by month and sum the total sales
monthly_sales = (
    sales.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales']
    .sum()
    .reset_index()
)

# Prophet requires columns named 'ds' (date) and 'y' (value)
monthly_sales.rename(columns={'Order Date': 'ds', 'Sales': 'y'}, inplace=True)

print("Monthly sales data prepared:")
print(monthly_sales.head())

# Create and fit the Prophet model

model = Prophet()
model.fit(monthly_sales)

# Make future predictions (next 6 months)

future = model.make_future_dataframe(periods=6, freq='M')
forecast = model.predict(future)

# Plot the forecast

fig1 = model.plot(forecast)
plt.title("📈 Sales Forecast (Next 6 Months)")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.show()

fig2 = model.plot_components(forecast)
plt.show()

# Save forecast results WITH PROPER ENCODING

forecast_output_path = r"C:\Users\MCW\Desktop\dinesh\dinesh\sales_performance_dashboard\output\sales_forecast.csv"

forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(forecast_output_path, index=False, encoding='utf-8')

print("Forecast saved successfully with UTF-8 encoding!")

# Display key predictions

predictions = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10)
print("\n Latest forecasted values:")
print(predictions)
