# 🧮 Sales Performance Analysis using Python

## 📘 Overview
This project analyzes sales data from a **Sample Superstore dataset** to uncover key insights into sales, profit, and performance trends.  
The goal is to perform **data cleaning, KPI generation, visualization, and forecasting** using Python.

---

## 🚀 Project Workflow
1. **Data Loading & Cleaning** (`load_prepare.py`)  
   - Removed duplicates and handled missing values  
   - Converted dates, filtered invalid values, and prepared a clean dataset  

2. **KPI Calculation** (`kpi_metrics.py`)  
   - Calculated total sales, profit, quantity, discount, and profit margin  
   - Generated top-performing states and products  

3. **Data Visualization** (`analysis_visuals.py`)  
   - Created visual charts using **Matplotlib**:  
     - Monthly sales trend  
     - Sales by category and region  
     - Top 10 profitable products  
     - Profit vs. discount relationship  

4. **Sales Forecasting** (`forecast.py`)  
   - Used **Facebook Prophet** to forecast the next 6 months of sales  
   - Visualized forecast and seasonal trends  

---

## 🧰 Tools & Libraries
- **Python**
- **Pandas**
- **Matplotlib**
- **Prophet (Facebook Prophet)**
- **NumPy**
- **CSV / Data Handling**

---

## 📊 Key Insights
- Identified top-performing regions and categories by sales and profit  
- Found clear monthly sales trends and discount–profit correlations  
- Forecasted future sales trends with seasonal variation  

---

## 🔗 Results & Visuals
Generated charts are saved in the `output/visuals/` folder:
- `monthly_sales_trend.png`  
- `sales_by_category.png`  
- `sales_by_region.png`  
- `top10_products_profit.png`  
- `profit_vs_discount.png`

---

## 📈 Forecast Output
Sales forecast (next 6 months) is stored as:
output/sales_forecast.csv