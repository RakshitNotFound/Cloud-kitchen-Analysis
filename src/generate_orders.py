import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# We import the menu from your other file
from generate_menu import get_menu

def generate_orders():
    np.random.seed(42)
    random.seed(42)
    
    # Load the kitchen data we just made
    df_kitchens = pd.read_csv('data/raw/kitchens_master.csv')
    kitchens_list = df_kitchens.to_dict('records')
    
    menu = get_menu()
    
    num_orders = 15000
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    orders_data = []

    for _ in range(num_orders):
        random_days = random.randint(0, (end_date - start_date).days)
        order_date = start_date + timedelta(days=random_days)
        
        # Simulate Peak Hours: Lunch (12-2 PM) and Dinner (7-10 PM)
        hour = random.randint(0, 23)
        if random.random() < 0.4: # 40% chance it's a peak meal hour
            hour = random.choice([12, 13, 14, 19, 20, 21, 22])
            
        minute = random.randint(0, 59)
        
        # Weekend spikes
        if order_date.weekday() in [4, 5, 6]: 
            if random.random() < 0.3: 
                hour = random.choice([12, 13, 14, 19, 20, 21, 22])
        
        order_time = f"{hour:02d}:{minute:02d}:00"
        
        brand = np.random.choice(['Olio', 'EatFit'], p=[0.6, 0.4])
        kitchen = random.choice(kitchens_list)
        
        item_data = random.choice(menu[brand])
        quantity = np.random.choice([1, 1, 1, 2, 2, 3], p=[0.6, 0.15, 0.05, 0.1, 0.05, 0.05])
        
        if brand == 'Olio':
            prep_time = np.random.normal(18, 4)
        else:
            prep_time = np.random.normal(10, 3)
            
        if random.random() < 0.02:
            prep_time = np.nan
        else:
            prep_time = max(2, round(prep_time, 1))
            
        if random.random() < 0.01:
            quantity = -1

        orders_data.append({
            'Order_ID': f"ORD-{random.randint(10000, 99999)}",
            'Order_Date': order_date.strftime('%Y-%m-%d'),
            'Order_Time': order_time,
            'Kitchen_ID': kitchen['Kitchen_ID'],
            'Brand': brand,
            'Item_Name': item_data['Item'],
            'Quantity': quantity,
            'Selling_Price': item_data['Price'],
            'Food_Cost': item_data['Cost'],
            'Prep_Time_Mins': prep_time
        })

    df_orders = pd.DataFrame(orders_data)
    
    # Automatically create the folders
    os.makedirs('data/raw', exist_ok=True)
    
    df_orders.to_csv('data/raw/orders_raw.csv', index=False)
    print(f"Generated {len(df_orders)} orders successfully in data/raw/")

if __name__ == "__main__":
    generate_orders()