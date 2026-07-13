# 🎬 Netflix Content Analytics Dashboard

## 📈 Dashboard Preview
> *Screenshots are available in the `Screenshots/` folder.*

## 🎯 Objective
Built a premium Netflix-themed content analytics dashboard to explore 8,800+ titles across Movies and TV Shows. The dashboard reveals content distribution trends, genre popularity, seasonal release patterns, and Year-over-Year growth using a multi-table Star Schema data model.

## 🛠️ Tools Used
- **Power BI** — Dark-mode Netflix-branded dashboard with custom radial neon-glow theme
- **Python (Pandas)** — Data cleaning, multi-value genre/country separation into bridge tables, and alignment error fixes
- **DAX** — Advanced measures including Total Titles, Movies, TV Shows, Avg Movie Duration, Titles YoY %
- **SQL** — KPI validation queries

## 📈 Key KPIs
| KPI | Value |
|-----|-------|
| Total Titles | 8,807 |
| Movies | 6,131 |
| TV Shows | 2,676 |
| Avg Movie Duration | 99.57 min |
| Genres Covered | 42 |
| Countries Covered | 121 |

## 🧹 Data Cleaning
- Fixed critical data alignment errors caused by newline characters (`\n`) inside the `description` column.
- Resolved the Louis C.K. duration data shift bug where `74 min` was incorrectly placed in the `listed_in` column.
- Separated multi-value `listed_in` (genres) and `country` columns into normalized bridge tables (`Genre.csv`, `Country.csv`).
- Standardized `date_added` to proper Date format and extracted Year, Month Number, and Month Name.

## 📁 Dataset
- **Source:** [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Tables:** 3 (Titles, Genre, Country — Star Schema)
- **Rows:** Titles: 8,807 | Genre: 19,323 | Country: 10,845

## 📞 Contact
- **LinkedIn:** [Parag Varshney](https://www.linkedin.com/in/parag-varshney-15a62b231/)
- **GitHub:** [VarshneyParag](https://github.com/VarshneyParag)
- **Email:** paragvarshney9678@gmail.com
