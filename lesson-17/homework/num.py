import pandas as pd
import numpy as np  # Random qiymatlar uchun

# Data yaratamiz
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 1. Rename column names using function ("First Name" --> "first_name", "Age" --> "age")
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)

# 2. Print the first 3 rows of the DataFrame
print(df.head(3))

# 3. Find the mean age of the individuals
print('Mean age:', df['age'].mean())

# 4. Select and print only the 'first_name' and 'city' columns
print(df[['first_name', 'city']])

# 5. Add a new column 'Salary' with random salary values
df['salary'] = np.random.randint(4000, 8000, size=len(df))
print(df)

# 6. Display summary statistics of the DataFrame
print(df.describe())


# sales_and_expenses DataFrame yaratamiz
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

# 1. Calculate and display the maximum sales and expenses
print('Max Sales:', sales_and_expenses['Sales'].max())
print('Max Expenses:', sales_and_expenses['Expenses'].max())

# 2. Calculate and display the minimum sales and expenses
print('Min Sales:', sales_and_expenses['Sales'].min())
print('Min Expenses:', sales_and_expenses['Expenses'].min())

# 3. Calculate and display the average sales and expenses
print('Average Sales:', sales_and_expenses['Sales'].mean())
print('Average Expenses:', sales_and_expenses['Expenses'].mean())


# expenses DataFrame yaratamiz
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

# 1. .set_index methodini ishlatib 'Category'ni index qilamiz
expenses = expenses.set_index('Category')

# 2. Calculate and display the maximum expense for each category
print('Max expense for each category:')
print(expenses.max(axis=1))

# 3. Calculate and display the minimum expense for each category
print('Min expense for each category:')
print(expenses.min(axis=1))

# 4. Calculate and display the average expense for each category
print('Average expense for each category:')
print(expenses.mean(axis=1))
