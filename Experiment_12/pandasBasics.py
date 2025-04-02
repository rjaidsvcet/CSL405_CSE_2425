import pandas as pd

# Creating a DataFrame with Product Data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [1200, 800, 300, 400, 100],
    "Stock": [10, 25, 30, 15, 50],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"]
}
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Adding a Discounted Price Column
df["Discounted Price"] = df["Price"] * 0.90  # Applying a 10% discount
print("\nDataFrame after adding Discounted Price:")
print(df)

# Filtering products priced above $500
filtered_df = df[df["Price"] > 500]
print("\nFiltered Products (Price > 500):")
print(filtered_df)

# Grouping by Category and computing average price
category_avg_price = df.groupby("Category")["Price"].mean()
print("\nAverage Price per Category:")
print(category_avg_price)

# Saving to CSV
df.to_csv("product_data.csv", index=False)
print("\nData saved to product_data.csv")