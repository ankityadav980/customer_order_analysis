# ============================================================
#   Customer Order Analysis Using Python
#   E-Commerce Data Analysis Project
# ============================================================


# ── TASK 1: Store Customer Orders ───────────────────────────

# List of customer names
customers = ["Ankit", "Rahul", "Priya", "Sneha", "Amit"]

# Each order stored as a tuple: (customer, product, price, category)
orders = [
    ("Ankit", "Laptop",    800, "Electronics"),
    ("Rahul", "T-Shirt",    30, "Clothing"),
    ("Priya", "Mixer",      60, "Home Essentials"),
    ("Sneha", "Headphones", 70, "Electronics"),
    ("Amit",  "Jeans",      50, "Clothing"),
    ("Ankit", "Mouse",      20, "Electronics"),
    ("Priya", "Cookware",   40, "Home Essentials"),
    ("Rahul", "Shoes",      80, "Clothing"),
]

# Dictionary: customer name → list of products they ordered
customer_products = {}
for name, product, price, category in orders:
    if name not in customer_products:
        customer_products[name] = []
    customer_products[name].append(product)

print("=" * 50)
print("CUSTOMER PRODUCTS")
print("=" * 50)
for name, products in customer_products.items():
    print(f"  {name}: {products}")


# ── TASK 2: Classify Products by Category ───────────────────

# Dictionary: product → category
product_category = {}
for name, product, price, category in orders:
    product_category[product] = category

# Set of unique categories
categories = set(product_category.values())

print("\n" + "=" * 50)
print("AVAILABLE PRODUCT CATEGORIES")
print("=" * 50)
for cat in categories:
    print(f"  • {cat}")


# ── TASK 3: Analyze Customer Spending ───────────────────────

# Calculate total spending per customer
customer_total = {}
for name, product, price, category in orders:
    if name not in customer_total:
        customer_total[name] = 0
    customer_total[name] += price

print("\n" + "=" * 50)
print("CUSTOMER SPENDING & CLASSIFICATION")
print("=" * 50)

for name, total in customer_total.items():
    if total > 100:
        level = "High-value buyer "
    elif total >= 50:
        level = "Moderate buyer"
    else:
        level = "Low-value buyer"
    print(f"  {name:<8} spent ${total:<5} → {level}")


# ── TASK 4: Generate Business Insights ──────────────────────

# 4a. Total revenue per product category
category_revenue = {}
for name, product, price, category in orders:
    if category not in category_revenue:
        category_revenue[category] = 0
    category_revenue[category] += price

print("\n" + "=" * 50)
print("REVENUE BY CATEGORY")
print("=" * 50)
for cat, revenue in category_revenue.items():
    print(f"  {cat:<20} → ${revenue}")

# 4b. Unique products using a set
unique_products = {product for name, product, price, category in orders}

print("\n" + "=" * 50)
print("UNIQUE PRODUCTS SOLD")
print("=" * 50)
print(f"  {unique_products}")

# 4c. ✅ FIX: List comprehension to find electronics customers
electronics_customers = [
    name for name, product, price, category in orders
    if category == "Electronics"
]

print("\n" + "=" * 50)
print("CUSTOMERS WHO BOUGHT ELECTRONICS")
print("=" * 50)
print(f"  {set(electronics_customers)}")

# 4d. Top 3 highest spending customers
sorted_customers = sorted(customer_total.items(), key=lambda x: x[1], reverse=True)

print("\n" + "=" * 50)
print("TOP 3 HIGHEST SPENDING CUSTOMERS")
print("=" * 50)
for rank, (name, total) in enumerate(sorted_customers[:3], start=1):
    print(f"  #{rank} {name} — ${total}")


# ── TASK 5: Set Operations ───────────────────────────────────

# 5a. ✅ FIX: Customers who purchased from MULTIPLE categories
customer_categories = {}
for name, product, price, category in orders:
    if name not in customer_categories:
        customer_categories[name] = set()
    customer_categories[name].add(category)

multi_category_customers = [
    name for name, cats in customer_categories.items()
    if len(cats) > 1
]

print("\n" + "=" * 50)
print("CUSTOMERS WHO BOUGHT FROM MULTIPLE CATEGORIES")
print("=" * 50)
print(f"  {multi_category_customers}")

# 5b. Common customers who bought BOTH Electronics AND Clothing
electronics_buyers = set()
clothing_buyers    = set()

for name, product, price, category in orders:
    if category == "Electronics":
        electronics_buyers.add(name)
    if category == "Clothing":
        clothing_buyers.add(name)

common_customers = electronics_buyers.intersection(clothing_buyers)

print("\n" + "=" * 50)
print("CUSTOMERS WHO BOUGHT BOTH ELECTRONICS & CLOTHING")
print("=" * 50)
print(f"  {common_customers}")

print("\n" + "=" * 50)
print("ANALYSIS COMPLETE")
print("=" * 50)
