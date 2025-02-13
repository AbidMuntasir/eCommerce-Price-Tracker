import pandas as pd
from bs4 import BeautifulSoup
import os 
def extract_product_info() :
    print("Extracting product info...")
    product_category = ["CPU", "Coolers","Motherboard","RAM", "Storage", "Graphics Card", "Power Supply", "Casing", "Monitors", "Casing Cooler", "Keyboard", "Mouse", "Anti Virus","Headphone","UPS","Laptop"]
    category_no = 0
    products = {'product name': [],'product category':[] ,'product price': []}
    while True: 
        product_no = 1
        file_path = f"products/{category_no}-{product_no}.html"
        
        if not os.path.exists(file_path):
            break
        while True:
            try:
                with open(f"products/{category_no}-{product_no}.html", "r", encoding="utf-8") as file:
                    html_content = file.read()  # Read file content
                soup = BeautifulSoup(html_content, "html.parser")
                product_name = soup.find("img").get("alt")
        
                try:
                    product_price = soup.find("span", class_="price-new").text.strip()
                except AttributeError:
                    if category_no == 15 or category_no == 2:
                        product_price = soup.find("div", class_="p-item-price").text.strip()
                    else:
                        product_price = soup.find("div", class_="price space-between").span.text.strip()
                products["product name"].append(product_name)  
                products["product category"].append(product_category[category_no])
                products["product price"].append(product_price)
                product_no += 1
            except FileNotFoundError:
                category_no += 1
                break

    products_df = pd.DataFrame(products)
    products_df["product price"] = products_df["product price"].str.replace("৳", "")
    products_df["product price"] = products_df["product price"].str.replace(",", "")
    products_df["product price"] = products_df["product price"].astype(int)

    if os.path.exists("data/today.csv"):
        if os.path.exists("data/yesterday.csv"):
            os.remove("data/yesterday.csv")
        os.rename("data/today.csv", "data/yesterday.csv")
        products_df.to_csv("data/today.csv", index=False)
    else:
        products_df.to_csv("data/today.csv", index=False)

    print("Product info extraction complete.")

