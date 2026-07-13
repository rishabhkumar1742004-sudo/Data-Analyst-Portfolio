import pandas as pd
import numpy as np
import os

def clean_and_rename_files():
    print("Starting data preprocessing for Blinkit Grocery Analytics...")
    
    # Files mapping: (raw_filename, output_filename)
    files_map = {
        'blinkit_customers.csv': 'Customers.csv',
        'blinkit_customer_feedback.csv': 'Feedback.csv',
        'blinkit_delivery_performance.csv': 'Delivery.csv',
        'blinkit_inventory.csv': 'Inventory.csv',
        'blinkit_marketing_performance.csv': 'Marketing.csv',
        'blinkit_orders.csv': 'Orders.csv',
        'blinkit_order_items.csv': 'OrderItems.csv',
        'blinkit_products.csv': 'Products.csv'
    }
    
    for raw_file, clean_file in files_map.items():
        if not os.path.exists(raw_file):
            print(f"Warning: {raw_file} not found. Skipping.")
            continue
            
        print(f"\nProcessing {raw_file} -> {clean_file}...")
        df = pd.read_csv(raw_file)
        
        # 1. Strip whitespace, newlines, and carriage returns from all object/string columns
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].apply(lambda x: str(x).replace('\n', ' ').replace('\r', ' ').strip() if pd.notnull(x) else x)
            
        # 2. Specific file cleaning logic
        if clean_file == 'Delivery.csv':
            # Fill missing values in reasons_if_delayed
            df['reasons_if_delayed'] = df['reasons_if_delayed'].fillna('On Time')
            
        elif clean_file == 'Inventory.csv':
            # Parse DD-MM-YYYY dates and convert to standard YYYY-MM-DD
            print("Standardizing inventory dates...")
            df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
            
        elif clean_file == 'Marketing.csv':
            print("Standardizing marketing dates...")
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            
        elif clean_file == 'Orders.csv':
            print("Standardizing order timestamps...")
            df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
            df['promised_delivery_time'] = pd.to_datetime(df['promised_delivery_time'], errors='coerce')
            df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'], errors='coerce')
            
        elif clean_file == 'Customers.csv':
            print("Standardizing customer registration dates...")
            df['registration_date'] = pd.to_datetime(df['registration_date'], errors='coerce')
            
        elif clean_file == 'Feedback.csv':
            print("Standardizing feedback dates...")
            df['feedback_date'] = pd.to_datetime(df['feedback_date'], errors='coerce')

        # Save to output file
        df.to_csv(clean_file, index=False)
        print(f"Successfully saved {clean_file} with shape {df.shape}")
        
    print("\nData preprocessing completed successfully! All cleaned files are saved in the project folder.")

if __name__ == "__main__":
    clean_and_rename_files()
