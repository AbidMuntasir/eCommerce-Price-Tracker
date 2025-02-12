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
        # Find the price changes
        merged_df = pd.merge(today_df,yesterday_df,on='product name',how='left')
        price_change_df = merged_df[merged_df['product price_x'] < merged_df['product price_y']]
        price_change_df['Price drop'] = price_change_df['product price_y'] - price_change_df['product price_x']
        price_change_df =price_change_df.rename(columns={'product price_x': 'new price', 'product price_y': 'old price'})
        
        # Identify new products (where price_y is NaN)
        new_product_df = merged_df[merged_df['product price_y'].isna()][['product name', 'product price_x']]
        new_product_df = new_product_df.rename(columns={'product price_x': 'new price'})

    except FileNotFoundError:
        print('Yesterday.csv not found. No price change comparison possible.')
        price_change_df = pd.DataFrame()  
        new_product_df = today_df.copy()  

    price_change_df.to_csv("data/price_drops.csv", index=False)
    new_product_df.to_csv("data/new_products.csv", index=False)
    print("Report generated.")
