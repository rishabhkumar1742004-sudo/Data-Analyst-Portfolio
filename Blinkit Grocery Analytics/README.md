# 🛒 Blinkit Grocery Sales & Marketing Analytics Dashboard

## 📈 Dashboard Preview
> *Screenshots are available in the `Screenshots/` folder.*

## 🎯 Objective
Designed a premium dark-mode Blinkit Grocery Analytics Dashboard analyzing ₹4.97M in sales across 5,000 orders. The 4-page dashboard covers business overview, product profitability, delivery & customer feedback, and marketing campaign ROI — providing 360° operational intelligence for quick-commerce decision makers.

## 🛠️ Tools Used
- **Power BI** — 4-page dark-mode dashboard with neon green glowing theme and Star Schema model
- **Python (Pandas)** — Data preprocessing, date standardization, and multi-table cleaning pipeline
- **DAX** — 10+ measures including SUMX Revenue, ROAS, On-time Delivery %, Avg Rating
- **SQL** — Database schema design, KPI validation, and category/outlet breakdown queries

## 📈 Key KPIs
| KPI | Value |
|-----|-------|
| Total Revenue | ₹4.97M |
| Total Orders | 5,000 |
| Total Customers | 2,500 |
| Average Order Value | ₹994.48 |
| On-time Delivery % | 69.40% |
| Items Sold | 10,034 |
| Avg Margin % | 27.78% |
| Avg Customer Rating | 3.34 ⭐ |
| Marketing Spend | ₹16.32M |
| Campaign ROAS | 1.97x |

## 🧹 Data Cleaning
- Processed 8 relational CSV files (Orders, Products, Customers, Delivery, Feedback, Marketing, OrderItems, Inventory).
- Standardized all date columns from mixed formats (`DD-MM-YYYY`, `YYYY-MM-DD HH:MM:SS`) to uniform `Date` type.
- Filled missing `reasons_if_delayed` values with "On Time" for clean delivery analysis.
- Stripped whitespace and newline characters from all text columns.
- Generated cleaned, renamed output files for direct Power BI import.

## 📁 Dataset
- **Source:** [Kaggle - Blinkit Sales Dataset](https://www.kaggle.com/datasets/akxiit/blinkit-sales-dataset)
- **Tables:** 8 relational CSVs (Star Schema)
- **Total Rows:** 98,000+ (across all tables)

## 📊 Dashboard Pages
| Page | Focus Area |
|------|-----------|
| Business Overview | Revenue KPIs, Monthly Trend, Category Donut, Delivery Status |
| Product Analysis | Category Revenue, Top Brands Treemap, Profitability Matrix |
| Delivery & Feedback | On-time %, Delay Reasons, CSAT by Segment, Feedback Categories |
| Revenue & Marketing | Channel Spend vs Revenue, Campaign ROAS, Clicks vs Conversions |

## 📞 Contact
- **LinkedIn:** [Parag Varshney](https://www.linkedin.com/in/parag-varshney-15a62b231/)
- **GitHub:** [VarshneyParag](https://github.com/VarshneyParag)
- **Email:** paragvarshney9678@gmail.com
