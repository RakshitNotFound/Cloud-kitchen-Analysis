import duckdb
import pandas as pd
import os

def run_analysis():
    # Connect to an in-memory database
    con = duckdb.connect()

    print("Loading data into DuckDB...")
    
    # Load your CSVs (Notice there is no ../ anymore)
    con.execute("CREATE TABLE orders AS SELECT * FROM read_csv_auto('data/raw/orders_raw.csv')")
    con.execute("CREATE TABLE kitchens AS SELECT * FROM read_csv_auto('data/raw/kitchens_master.csv')")

    print("Running SQL Queries...")

    # Query 1: Revenue by Brand
    query1 = """
        SELECT 
            Brand,
            SUM(Quantity * Selling_Price) AS Total_Revenue,
            SUM(Quantity * Food_Cost) AS Total_Food_Cost,
            SUM(Quantity * (Selling_Price - Food_Cost)) AS Gross_Profit
        FROM orders
        WHERE Quantity > 0
        GROUP BY Brand
        ORDER BY Gross_Profit DESC;
    """
    
    df_results = con.execute(query1).df()
    print("\n--- Brand Profitability ---")
    print(df_results)
    
    # Save results to a new CSV for Power BI
    os.makedirs('data/processed', exist_ok=True)
    df_results.to_csv('data/processed/brand_profitability.csv', index=False)
    print("\nSaved results to data/processed/brand_profitability.csv")

if __name__ == "__main__":
    run_analysis()