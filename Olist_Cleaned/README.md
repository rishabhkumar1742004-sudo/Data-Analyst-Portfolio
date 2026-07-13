# 🇧🇷 Olist E-Commerce Marketplace Dashboard

## 📈 Dashboard Preview
> *Screenshots are available in the `Screenshots/` folder.*

## 🎯 Objective
Designed an enterprise-grade analytics dashboard for Brazil's largest online marketplace (Olist), processing 8 interconnected relational tables into a unified Star Schema model. The dashboard provides 360° insights into sales performance, logistics efficiency, seller analytics, and customer satisfaction across all Brazilian states.

## 🛠️ Tools Used
- **Power BI** — Multi-page executive dashboard with Star Schema data model
- **Python (Pandas)** — ETL pipeline for cleaning, merging, and standardizing 8 relational CSVs
- **DAX** — Advanced measures including Revenue, AOV, Delivery Time, and Review Scores
- **SQL** — KPI validation queries and data integrity checks

## 📈 Key KPIs
| KPI | Value |
|-----|-------|
| Total Revenue | R$ 15.44M |
| Total Orders | 98,666 |
| Total Customers | 99,441 |
| Average Order Value | R$ 156.50 |
| Average Review Score | 4.09 ⭐ |
| Avg Delivery Time | ~12 days |

## 🧹 Data Cleaning
- Merged 8 relational CSVs (orders, customers, sellers, products, payments, reviews, geolocation, order_items).
- Standardized date columns to `datetime` format.
- Handled missing values in review comments and product dimensions.
- Translated Portuguese category names to English.
- Removed duplicates in geolocation data (19K unique zip codes from 1M+ raw records).

## 📁 Dataset
- **Source:** [Kaggle - Brazilian E-Commerce (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Tables:** 8 relational CSVs
- **Total Rows:** 500K+ (across all tables)

## 📞 Contact
- **LinkedIn:** [Parag Varshney](https://www.linkedin.com/in/paragvarshney/)
- **GitHub:** [VarshneyParag](https://github.com/VarshneyParag)
- **Email:** paragvarshney9678@gmail.com
