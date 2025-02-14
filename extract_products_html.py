from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
def scrape_product_html():
    print("Scraping product HTML...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Determine the correct ChromeDriver path based on the OS
    if sys.platform == "win32":  
        service_instance = Service(executable_path="chromedriver.exe")  # Windows
    else:
        service_instance = Service(executable_path="/usr/local/bin/chromedriver")  # Linux (GitHub Actions)

    driver = webdriver.Chrome(service=service_instance,options=chrome_options)
    driver.set_window_size(1366, 768)
    driver.get("https://www.startech.com.bd/tool/pc_builder")
    category_no = 0
    while True:
        if category_no > len(driver.find_elements(By.LINK_TEXT, "Choose")) - 1:
            break
        buttonElements = driver.find_elements(By.LINK_TEXT, "Choose")
        buttonElements[category_no].click()
        product_no = 0   
        while True:
            productElements = driver.find_elements(By.CLASS_NAME, "product-thumb")
            for productElement in productElements:
                product_no += 1
                productHTML = productElement.get_attribute("outerHTML")
                file_path = f"products/{category_no}-{product_no}.html" 
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(productHTML)
            try:
                nxt_pg = driver.find_element(By.LINK_TEXT, "NEXT")
                nxt_pg.click()
            except:
                break
        main_page_click  = driver.find_element(By.LINK_TEXT, "PC Builder")
        main_page_click.click()
        category_no += 1
    
    driver.quit()
    print("Product HTML scraping complete.")
