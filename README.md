# Cloud Kitchen Profitability Analysis (Curefoods Simulation)

## 📌 Project Overview
An end-to-end data pipeline simulating a multi-brand cloud kitchen business (modeled after Curefoods). The goal was to analyze brand profitability and identify which kitchen locations are operating at a net loss due to high overhead costs.

## 🛠️ Tech Stack
* **Python (Pandas, NumPy, Faker):** Generated 15,000 realistic, slightly messy orders.
* **DuckDB (SQL):** Created an in-memory analytical database to run complex queries (CTEs, Joins) for financial aggregation.
* **Power BI:** Built an executive dashboard to visualize Revenue, Gross Profit, and Net Profit by location.

## 💡 Key Business Insight
While the 'Olio' brand generated 60% of total revenue, the dashboard revealed that high-rent kitchen locations (like Indiranagar) were operating at a net loss because their order volume wasn't high enough to cover fixed costs.

## 📂 Repository Structure
* `/src`: Python scripts for data generation and SQL execution.
* `/data`: Raw and processed CSV files.
* `/dashboard`: Contains a screenshot of the Power BI report.

## 🚀 How to Run
1. Install dependencies: `pip install pandas numpy faker duckdb`
2. Generate data: `python src/generate_kitchen.py` then `python src/generate_orders.py`
3. Run SQL analysis: `python src/run_sql.py`