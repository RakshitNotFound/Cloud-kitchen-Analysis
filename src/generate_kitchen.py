import pandas as pd
import numpy as np
import random
import os

def generate_kitchens():
    np.random.seed(42)
    random.seed(42)
    
    locations = ['Indiranagar', 'HSR Layout', 'Koramangala', 'Whitefield', 'Jayanagar', 'Marathahalli', 'Bellandur', 'Electronic City']
    kitchens_data = []
    
    for i in range(8):
        kitchens_data.append({
            'Kitchen_ID': f"KT-{100 + i}",
            'Location': locations[i],
            'Monthly_Rent_INR': np.random.randint(40000, 120000),
            'Monthly_Staff_Cost_INR': np.random.randint(60000, 150000),
            'Max_Capacity_Per_Hour': np.random.choice([40, 60, 80, 100])
        })
        
    df = pd.DataFrame(kitchens_data)
    
    # Automatically create the folders if they don't exist
    os.makedirs('data/raw', exist_ok=True)
    
    df.to_csv('data/raw/kitchens_master.csv', index=False)
    print("Kitchens data generated successfully in data/raw/")

if __name__ == "__main__":
    generate_kitchens()