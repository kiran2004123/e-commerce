import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# SAMPLE E-COMMERCE DATASET
# ==========================

np.random.seed(42)

n = 100

df = pd.DataFrame({
    "Order_ID": np.arange(1001, 1001 + n),
    "Category": np.random.choice(
        ["Electronics", "Furniture", "Clothing"],
        n
    ),
    "Region": np.random.choice(
        ["North", "South", "East", "West"],
        n
    ),
    "Price": np.random.randint(500, 50000, n),
    "Quantity": np.random.randint(1, 10, n),
    "Rating": np.random.randint(1, 6, n)
})

df["Sales"] = df["Price"] * df["Quantity"]

print("\nDATASET PREVIEW\n")
print(df.head())

# ==========================================
# MATPLOTLIB VISUALIZATIONS
# ==========================================

# 1. Sales by Category
sales_by_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(
    sales_by_category.index,
    sales_by_category.values,
    color=["red", "blue", "green"]
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# ==========================================

# 2. Histogram of Prices
plt.figure(figsize=(8,5))
plt.hist(
    df["Price"],
    bins=10,
    color="orange",
    edgecolor="black"
)

plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# ==========================================

# 3. Pie Chart
plt.figure(figsize=(8,8))
plt.pie(
    sales_by_category,
    labels=sales_by_category.index,
    autopct="%1.1f%%"
)

plt.title("Sales Contribution")
plt.show()

# ==========================================

# 4. Order Wise Sales Trend
plt.figure(figsize=(10,5))

plt.plot(
    df["Order_ID"],
    df["Sales"],
    marker="o",
    linestyle="-"
)

plt.title("Order Wise Sales")
plt.xlabel("Order ID")
plt.ylabel("Sales")
plt.show()

# ==========================================

# 5. Sales by Region
sales_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(
    sales_region.index,
    sales_region.values,
    color="purple"
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# ==========================================
# SEABORN VISUALIZATIONS
# ==========================================

sns.set_style("whitegrid")

# 6. Count Plot
plt.figure(figsize=(8,5))

sns.countplot(
    x="Category",
    data=df,
    palette="Set2"
)

plt.title("Category Count")
plt.show()

# ==========================================

# 7. Box Plot
plt.figure(figsize=(8,5))

sns.boxplot(
    x="Category",
    y="Price",
    data=df,
    palette="Set3"
)

plt.title("Category vs Price")
plt.show()

# ==========================================

# 8. Scatter Plot
plt.figure(figsize=(10,6))

sns.scatterplot(
    x="Price",
    y="Sales",
    hue="Category",
    data=df,
    s=100
)

plt.title("Price vs Sales")
plt.show()

# ==========================================

# 9. Heatmap

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

# ==========================================



# ==========================================
# BONUS DASHBOARD
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(12,8))

# Category Count
sns.countplot(
    x="Category",
    data=df,
    ax=axes[0,0]
)

axes[0,0].set_title("Category Count")

# Price Distribution
axes[0,1].hist(
    df["Price"],
    bins=10,
    color="skyblue"
)

axes[0,1].set_title("Price Distribution")

# Rating Distribution
sns.countplot(
    x="Rating",
    data=df,
    ax=axes[1,0]
)

axes[1,0].set_title("Ratings")

# Scatter
sns.scatterplot(
    x="Price",
    y="Sales",
    hue="Category",
    data=df,
    ax=axes[1,1]
)

axes[1,1].set_title("Price vs Sales")

plt.tight_layout()
plt.show()
