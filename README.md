# 🛒 E-Commerce Data Analysis using Python

## 📌 Project Overview

This project analyzes an e-commerce retail dataset using **Python**, **NumPy**, and **pandas** to extract meaningful business insights. The goal is to understand customer purchasing behavior, identify top-performing products, segment customers based on spending, and build a simple product recommendation system.

This project was developed to strengthen my data analysis skills and apply NumPy and pandas to a real-world business problem.


## 🎯 Objectives

- Clean and preprocess the dataset
- Analyze customer purchasing behavior
- Calculate product revenue and sales statistics
- Identify VIP customers
- Segment customers based on total spending
- Find top-performing products
- Build a basic product recommendation system


## 🛠️ Technologies Used

- Python
- NumPy
- pandas
- openpyxl (for Excel files)
- VS Code

---

## 📂 Dataset

Dataset: **Online Retail Dataset**

Main columns used:

- CustomerID
- Description
- Quantity
- UnitPrice

A new column named **PurchaseAmount** is created using:

```python
PurchaseAmount = Quantity * UnitPrice
```

---

## 📊 Analysis Performed

### ✔ Data Cleaning

- Removed missing values
- Selected required columns
- Created PurchaseAmount column

### ✔ Exploratory Data Analysis (EDA)

- Dataset information
- Shape of dataset
- Summary statistics
- Product-wise analysis

### ✔ Product Analysis

- Average purchase amount
- Standard deviation
- Total revenue per product
- Top 5 products
- Lowest-performing products

### ✔ Customer Analysis

- Total spending by each customer
- Top 10 VIP customers

### ✔ Customer Segmentation

Customers are classified into:

- Low
- Medium
- High
- VIP

using spending quartiles (25%, 50%, and 75%).

### ✔ Performance Comparison

Compared the execution time of NumPy operations with a traditional Python loop to demonstrate NumPy's efficiency in numerical computations.

### ✔ Product Recommendation

A simple recommendation system suggests products that a customer has not purchased yet based on product popularity.

---

## 📈 Skills Demonstrated

- Data Cleaning
- Data Analysis
- NumPy
- pandas
- GroupBy Operations
- Sorting & Ranking
- Customer Segmentation
- Business Analytics
- Performance Analysis
- Recommendation Logic

---

## 🚀 Future Improvements

- Add Matplotlib visualizations
- Create interactive dashboards
- Perform RFM Analysis
- Build a Machine Learning recommendation system
- Deploy as a Streamlit web application

---

## ▶️ How to Run

Clone the repository

```bash
git clone https://github.com/Rriya09/ecommerce-data-analysis-python.git
```

Install dependencies

```bash
pip install numpy pandas openpyxl
```

Run the project

```bash
python analysis.py
```

---

## 📷 Sample Output

- Top Selling Products
- Customer Segmentation
- VIP Customers
- Product Recommendations

---

## 👩‍💻 Author

**Riya**

BCA Student | Aspiring Data Analyst 

- GitHub: https://github.com/Rriya09
  
Currently learning:
- Python
- NumPy
- pandas
- SQL
- Data Visualization


Feel free to connect with me on LinkedIn and check out my other projects!

---

⭐ If you found this project useful, consider giving it a star!
