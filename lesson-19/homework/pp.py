# Homework Assignments Solutions

import pandas as pd
import sqlite3

solutions = []

# =========================
# Homework 1: Analyzing Sales Data
# =========================

# Load sales data
sales_data = pd.read_csv('task/sales_data.csv')

# 1. Group by Category and calculate total quantity, average price, maximum quantity
sales_summary = sales_data.groupby('Category').agg(
    Total_Quantity=('Quantity', 'sum'),
    Average_Price=('Price', 'mean'),
    Max_Quantity=('Quantity', 'max')
).reset_index()
solutions.append(sales_summary)

# 2. Identify top-selling product in each category
top_products = sales_data.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling = top_products.groupby('Category').first().reset_index()
solutions.append(top_selling)

# 3. Find the date with highest total sales (quantity * price)
sales_data['Total_Sales'] = sales_data['Quantity'] * sales_data['Price']
top_sale_date = sales_data.groupby('Date')['Total_Sales'].sum().idxmax()
solutions.append(top_sale_date)

# =========================
# Homework 2: Examining Customer Orders
# =========================

# Load customer orders data
customer_orders = pd.read_csv('task/customer_orders.csv')

# 1. Group by CustomerID and filter customers with at least 20 orders
customer_order_counts = customer_orders.groupby('CustomerID').size().reset_index(name='Order_Count')
active_customers = customer_order_counts[customer_order_counts['Order_Count'] >= 20]
solutions.append(active_customers)

# 2. Identify customers with average price per unit > $120
avg_price_per_customer = customer_orders.groupby('CustomerID')['Price'].mean().reset_index()
high_value_customers = avg_price_per_customer[avg_price_per_customer['Price'] > 120]
solutions.append(high_value_customers)

# 3. Total quantity and price for each product, filter products with quantity >= 5
product_summary = customer_orders.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('Price', 'sum')
).reset_index()
filtered_products = product_summary[product_summary['Total_Quantity'] >= 5]
solutions.append(filtered_products)

# =========================
# Homework 3: Population Salary Analysis
# =========================

# Connect to SQLite database
conn = sqlite3.connect('task/population.db')

# Read population table
population = pd.read_sql_query('SELECT * FROM population', conn)

# Load salary band info
salary_bands = pd.read_excel('task/population salary analysis.xlsx')

# Merge population data with salary band
population['Salary Band'] = pd.cut(population['Salary'], 
                                   bins=salary_bands['Min Salary'].tolist() + [float('inf')],
                                   labels=salary_bands['Band'])

# 1. Percentage of population for each salary category
pop_count = population['Salary Band'].value_counts(normalize=True) * 100
solutions.append(pop_count)

# 2. Average salary in each salary category
avg_salary_by_band = population.groupby('Salary Band')['Salary'].mean()
solutions.append(avg_salary_by_band)

# 3. Median salary in each salary category
median_salary_by_band = population.groupby('Salary Band')['Salary'].median()
solutions.append(median_salary_by_band)

# 4. Number of population in each salary category
count_by_band = population['Salary Band'].value_counts()
solutions.append(count_by_band)

# 5. Same measures in each State
state_salary_summary = population.groupby(['State', 'Salary Band']).agg(
    Population_Percent=('State', lambda x: len(x) / len(population) * 100),
    Avg_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median'),
    Population_Count=('State', 'count')
).reset_index()
solutions.append(state_salary_summary)

# =========================
# Print all solutions
# =========================
for idx, sol in enumerate(solutions, 1):
    print(f'\nSolution {idx}:\n', sol)
