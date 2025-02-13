from extract_products_html import scrape_product_html
from extract_product_info import extract_product_info
from product_changes import compare_price
from scrape_motherboard_laptop import scrape_motherboard_laptop

def main():
    scrape_product_html()
    scrape_motherboard_laptop('motherboard')
    scrape_motherboard_laptop('laptop')
    extract_product_info()
    compare_price()

if __name__ == "__main__":
    main()
