import pandas as pd

data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-02-01"],
    "Product": ["Laptop", "Phone", "Laptop"],
    "Revenue": [50000, 20000, 30000]
}

df = pd.DataFrame(data)

df["Date"] = pd.to_datetime(df["Date"])

# Total revenue per product
print(df.groupby("Product")["Revenue"].sum())

# Best selling product
print(df.groupby("Product")["Revenue"].sum().idxmax())

# Monthly revenue
df["Month"] = df["Date"].dt.month
print(df.groupby("Month")["Revenue"].sum())
