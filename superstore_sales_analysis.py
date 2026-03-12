import numpy as np 
import pandas as pd

#Loading the dataset using pandas.read_csv()
url = "https://raw.githubusercontent.com/yannie28/Global-Superstore/master/Global_Superstore(CSV).csv"
df = pd.read_csv(url)

#Displaing first 5 rows and dataset shape
print(df.head())
print(df.shape)

#Showing column names and data types using info()
print("Showing the column names and data types")
print(df.info())

#Checking missing values in each column
missing_value = pd.isnull(df)
print(f"\nThe total missing values \n{missing_value.sum()}")

#Removing duplicate rows
df = df.drop_duplicates()
print("\nRemoving the duplicates values form data set \n",df.shape)

#Converting Order Date column to datetime.
df["Order Date"] = pd.to_datetime(df["Order Date"])


#Create a new column : Profit Margin
df['profit_margin'] = df["Profit"]/df["Sales"]

# Finding top selling products
product_sales = df.groupby("Product Name")["Sales"].sum()
product_sales = product_sales.sort_values(ascending=False)
top_product = product_sales.head(10)
print(f"\nThe total salles by Category : \n{top_product}")

#Finding top 10 cities with highest sales.
highest_sales = df.groupby('City')['Sales'].sum()
highest_sales = highest_sales.sort_values(ascending=False).head(10)
print(f"\nThe top 10 cities with highest sales \n{highest_sales}")

#Finding total profit by Region.
Total_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False).head()
print(f"\nThe total profit by \n{Total_profit}")

#Extracting Year and Month from Order Date and calculate monthly sales.
df['months'] = df["Order Date"].dt.month
df['Year'] = df["Order Date"].dt.year
monthly_sales = df.groupby('months')['Sales'].sum()
print(f"\nMonthly sales \n{monthly_sales}")

#Business Insights
print("\nMotorola Smart Phone category generates the highest revenue among all categories.")
print("Sydney City is the top-performing city in terms of sales.")
print("The Eastern Asia region contributes the highest total profit.")
print("Sales peak during December, suggesting seasonal demand.")
print("Some products generate high sales but lower profit due to discounts.")