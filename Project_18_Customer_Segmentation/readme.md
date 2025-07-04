# 🧠 Customer Segmentation using K-Means Clustering

Customer segmentation is the process of dividing customers into groups based on common characteristics. This project uses **K-Means Clustering**, an unsupervised machine learning algorithm, to identify distinct customer segments from mall customer data.

---

## 📁 Dataset

**Mall Customer Segmentation Dataset**  
Available on Kaggle  
It includes:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

## 🎯 Project Objective

To segment customers based on their purchasing behavior and demographic data, helping businesses tailor their marketing strategies.

---

## 🧰 Technologies & Libraries

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn (KMeans, StandardScaler)

---

## 📌 Steps Performed

1. **Data Loading and Exploration**  
   Loaded the dataset and performed basic EDA.

2. **Preprocessing**  
   - Removed unnecessary columns like `CustomerID`
   - Converted categorical data (`Gender`) to numerical
   - Scaled numerical features

3. **Elbow Method**  
   Used to determine the optimal number of clusters by plotting the Within-Cluster Sum of Squares (WCSS).

4. **K-Means Clustering**  
   Trained a model with optimal clusters (K=5).

5. **Visualization**  
   Plotted customer segments based on `Annual Income` and `Spending Score`.

---

## 📊 Results

Identified 5 unique customer segments:
- High income, high spenders
- Low income, high spenders
- Medium income, moderate spenders
- High income, low spenders
- Low income, low spenders

These clusters can now be used for:
- Targeted marketing
- Customer loyalty campaigns
- Product personalization

---
