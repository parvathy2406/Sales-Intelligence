import pandas as pd

df = pd.read_csv("data/processed/cleaned_sales.csv")

# Ensure date format
df['order_date'] = pd.to_datetime(df['order_date'])

summary = {}

# KPIs
summary['total_sales'] = df['revenue'].sum()
summary['total_orders'] = df['order_id'].nunique()
summary['avg_sales'] = df['revenue'].mean()

# Group insights
summary['top_category'] = df.groupby('category')['revenue'].sum().idxmax()
summary['top_region'] = df.groupby('region')['revenue'].sum().idxmax()

# Save summary for BI layer
summary_df = pd.DataFrame(list(summary.items()), columns=['metric', 'value'])
summary_df.to_csv("data/processed/kpi_summary.csv", index=False)

print("✅ BI summary file created successfully!")