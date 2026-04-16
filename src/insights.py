import pandas as pd

df = pd.read_csv("data/processed/cleaned_sales.csv")

print("\n BASIC DATA OVERVIEW")
print(df.info())

print("\n TOTAL SALES")
print(df['revenue'].sum())

print("\n SALES BY CATEGORY")
print(df.groupby('category')['revenue'].sum().sort_values(ascending=False))

print("\n SALES BY REGION")
print(df.groupby('region')['revenue'].sum().sort_values(ascending=False))

print("\n TOP 10 CUSTOMERS")
print(df.groupby('customer_name')['revenue'].sum().sort_values(ascending=False).head(10))

print("\n MONTHLY TREND PREVIEW")
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.to_period('M')
print(df.groupby('month')['revenue'].sum())