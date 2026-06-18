# customer_order_analysis
# 🛒 Customer Order Analysis Using Python

A Python data analysis project that processes e-commerce customer orders to generate meaningful business insights. Built as part of a B.Tech final year course-end project.

---

## 📌 Project Overview

This project simulates the role of a **Data Analyst** at an e-commerce company. Using Python's core data structures — **lists, tuples, dictionaries, and sets** — the program analyzes customer purchase behavior and generates insights to help business managers make data-driven decisions.

---

## 🎯 Features

- ✅ Store and organize customer orders using lists, tuples & dictionaries
- ✅ Classify products by category using dictionaries and sets
- ✅ Classify customers as High-value, Moderate, or Low-value buyers
- ✅ Calculate total revenue per product category
- ✅ Find top 3 highest spending customers
- ✅ Identify customers who bought Electronics using list comprehension
- ✅ Use set operations to find customers who bought from multiple categories

---

## 🗂️ Project Structure

```
customer-order-analysis-python/
│
├── customer_order_analysis.py   # Main Python script
└── README.md                    # Project documentation
```

---

## 🧰 Tech Stack

- **Language:** Python 3
- **Libraries Used:** None (only built-in Python data structures)
- **Concepts Covered:** Lists, Tuples, Dictionaries, Sets, Loops, Conditionals, List Comprehension, Lambda, Sorting

---

## ▶️ How to Run

**Step 1:** Make sure Python 3 is installed on your system.
```bash
python --version
```

**Step 2:** Clone this repository.
```bash
git clone https://github.com/YOUR_USERNAME/customer-order-analysis-python.git
cd customer-order-analysis-python
```

**Step 3:** Run the Python script.
```bash
python customer_order_analysis.py
```

---

## 📊 Sample Output

```
==================================================
CUSTOMER SPENDING & CLASSIFICATION
==================================================
  Ankit    spent $820   → High-value buyer 🏆
  Rahul    spent $110   → High-value buyer 🏆
  Priya    spent $100   → Moderate buyer
  Sneha    spent $70    → Moderate buyer
  Amit     spent $50    → Moderate buyer

==================================================
REVENUE BY CATEGORY
==================================================
  Electronics          → $890
  Clothing             → $160
  Home Essentials      → $100

==================================================
TOP 3 HIGHEST SPENDING CUSTOMERS
==================================================
  #1 Ankit — $820
  #2 Rahul — $110
  #3 Priya — $100
```

---

## 📚 Key Python Concepts Used

| Concept | Where Used |
|---|---|
| List | Storing customer names and orders |
| Tuple | Each order record (name, product, price, category) |
| Dictionary | Customer → products, product → category, revenue per category |
| Set | Unique categories, unique products, set intersection |
| Loop + Conditionals | Customer classification logic |
| List Comprehension | Finding electronics customers |
| Lambda + Sorting | Finding top 3 spenders |
| Set Intersection | Finding customers who bought both Electronics & Clothing |

---

## 👨‍💻 Author

**[Your Name]**
B.Tech Final Year Student
[Your GitHub Profile Link]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
