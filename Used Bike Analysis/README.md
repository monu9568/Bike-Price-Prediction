# 🏍️ Bike Price Prediction Dashboard | Internship Project

### 📘 Project Overview
This project aims to predict the prices of **used bikes** based on various factors such as model year, mileage, power, and ownership details.  
It combines **Machine Learning** with **Power BI visualization** to provide actionable insights into the used bike market.

---

### 📊 Dataset Information
The dataset includes details about used bikes with the following columns:

| Column Name | Description |
|--------------|-------------|
| model_name | Name of the bike model |
| model_year | Year the model was manufactured |
| kms_driven | Total kilometers driven |
| owner | Ownership type (first, second, etc.) |
| location | City or region of sale |
| mileage | Average mileage (km/l) |
| power | Engine power (BHP) |
| price | Selling price (target variable) |
| cc | Engine capacity in cubic centimeters |
| brand | Brand name of the bike |

---

### ⚙️ Steps Performed
1. **Data Cleaning** – Removed null values, standardized units, and cleaned inconsistent entries.  
2. **Feature Engineering** – Created numerical columns (`mileage_num`, `power_num`, `kms_driven_num`, etc.) and grouped price ranges.  
3. **Exploratory Data Analysis (EDA)** – Identified key patterns between price and features like model year, mileage, and power.  
4. **Machine Learning Model** – Trained a **Random Forest Regressor** to predict used bike prices.  
5. **Power BI Dashboard** – Designed an interactive dashboard showing KPIs, trend charts, and model performance metrics.

---

### 🤖 Model Performance

| Scale | Metric | Value |
|--------|---------|--------|
| **Log Scale** | R² Score | 0.91 |
| **Log Scale** | MAE | 0.14 |
| **Log Scale** | RMSE | 0.19 |
| **Original Scale** | MAE | ₹11,758 |
| **Original Scale** | RMSE | ₹17,236 |

✅ **R² Score of 0.91** indicates a strong predictive performance.

---

### 📈 Power BI Dashboard Highlights
- **KPI Cards** – Total bikes, average price, mileage, and kilometers driven.  
- **Charts** – Price vs Model Year, Brand-wise Average Price, Ownership Distribution, Location Analysis.  
- **Model Insights Section** – Displays ML model accuracy (R², MAE, RMSE).  
- **Slicers** – Model Year, Brand, and Price Range for dynamic filtering.

*(Dashboard built with a modern dark gradient theme for a professional analytical look.)*

---

### 🧠 Tools & Technologies Used
- **Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Visualization Tool:** Power BI  
- **Environment:** Jupyter Notebook<img width="1061" height="595" alt="Bike Prediction Dashboard" src="https://github.com/user-attachments/assets/f02f0c72-ac69-4c6b-8e16-8a626c8d2d76" />
  
- **Version Control:** GitHub

---


