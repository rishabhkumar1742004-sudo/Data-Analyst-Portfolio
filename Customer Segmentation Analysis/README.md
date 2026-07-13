# 🛍️ Customer Segmentation & RFM Analysis Dashboard

## 📈 Dashboard Preview
> *Screenshots are available in the `Screenshots/` folder.*

## 🎯 Objective
Built an advanced Customer Segmentation dashboard using RFM (Recency, Frequency, Monetary) analysis on a UK-based online retail dataset. The dashboard helps marketing teams identify high-value customers, at-risk segments, and personalization opportunities to optimize retention strategies.

## 🛠️ Tools Used
- **Power BI** — Interactive segmentation dashboard with drill-through capabilities
- **Python (Pandas)** — Data cleaning, transaction-level preprocessing, and RFM score computation
- **DAX** — Calculated measures for Revenue, Customer Count, and Average Order Value
- **Excel** — Raw data source (Online Retail II dataset)

## 📈 Key KPIs
| KPI | Value |
|-----|-------|
| Total Revenue | £8.91M |
| Total Customers | 4,372 |
| Total Transactions | 805,549 |
| Average Order Value | £11.06 |
| Customer Segments | Champions, Loyal, At Risk, Lost |

## 🧹 Data Cleaning
- Removed negative quantities (returns/cancellations) and zero-price transactions.
- Filtered out non-product stock codes (POST, DOT, ADJUST, etc.).
- Computed `TotalPrice = Quantity × Price` for revenue calculations.
- Built RFM scores and segmented customers into actionable groups.

## 📁 Dataset
- **Source:** [UCI Machine Learning Repository - Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- **Rows:** 805,549 (cleaned transactions)
- **Columns:** 9

## 📞 Contact
- **LinkedIn:** [Parag Varshney](https://www.linkedin.com/in/paragvarshney/)
- **GitHub:** [VarshneyParag](https://github.com/VarshneyParag)
- **Email:** paragvarshney9678@gmail.com
