import pandas as pd
import time 
import os
def compare_price():
    print("Generating report...")
    # Load today.csv
    today_df = pd.read_csv('data/today.csv')
    # Find if yestrday.csv exists
    try:
        yesterday_df = pd.read_csv('data/yesterday.csv')
        yesterday_df['product price'] = yesterday_df['product price'].astype(int)
        # Find the price changes
        merged_df = pd.merge(today_df, yesterday_df, on='product name', how='left', suffixes=('', '_y'))

        # Drop duplicate columns (except for price)
        cols_to_drop = [col for col in merged_df.columns if col.endswith('_y') and col not in ['product price_y']]
        merged_df.drop(columns=cols_to_drop, inplace=True)
        
        price_change_df = merged_df[merged_df['product price'] < merged_df['product price_y']]

        price_change_df =price_change_df.rename(columns={'product price': 'new price', 'product price_y': 'old price'})
        
        # Identify new products (where price_y is NaN)
        new_product_df = merged_df[merged_df['product price_y'].isna()]
        new_product_df = new_product_df.rename(columns={'product price_x': 'price'})

        # Drop the price_y column
        new_product_df.drop(columns=['product price_y'], inplace=True)

    except FileNotFoundError:
        print('Yesterday.csv not found. No price change comparison possible.')
        price_change_df = pd.DataFrame()  
        new_product_df = today_df.copy()  
    # Convert price columns to integer
    price_change_df['old price'] = price_change_df['old price'].astype(int)
    
    price_change_df.to_csv("data/price_drops.csv", index=False)
    new_product_df.to_csv("data/new_products.csv", index=False)
    print("Report generated.")
