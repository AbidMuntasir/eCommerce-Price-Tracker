#  eCommerce Price Tracker

An automated price tracker that scrapes product information from the **Startech** website, tracks price changes, display newly added products and displays the data on an interactive dashboard.

---

## 📂 Project Structure

```
eCommerce Price Tracker/
│
├── data/
│   ├── price_drops.csv
│   ├── new_products.csv
│   ├── today.csv
│   └── yesterday.csv
│
├── products/
│   └── [category_no]-[product_no].html
│
├── extract_products_html.py
├── extract_product_info.py
├── product_changes.py
├── run_scripts.py
├── dashboard.py
└── README.md
```

### 🔹 **Project Structure & File Descriptions**

- **`data/`** → Contains CSV files with extracted product data.

  - `price_drops.csv` → List of products with price drops.
  - `new_products.csv` → List of newly added products.
  - `today.csv` → Product data scraped today.
  - `yesterday.csv` → Product data scraped yesterday.

- **`products/`** → Stores raw HTML files of product pages.

- **`extract_products_html.py`** → Scrapes product HTML from Startech.

- **`extract_product_info.py`** → Extracts product details from HTML and saves them as CSV.

- **`product_changes.py`** → Compares today's and yesterday's prices to detect changes.

- **`run_scripts.py`** → Runs all the scripts except the dashboard.

- **`dashboard.py`** → Streamlit-powered dashboard for data visualization.

---

## 🚀 How to Use

### 1️⃣ Run Everything at Once

Execute all scripts (except the dashboard) using:

```bash
python run_script.py
```

### 2️⃣ Scrape Product HTML (If Running Manually)

Extract product pages from Startech.

```bash
python extract_products_html.py
```

### 3️⃣ Extract Product Data

Process the HTML files and save structured data.

```bash
python extract_product_info.py
```

### 4️⃣ Compare Price Changes

Identify price drops and new products.

```bash
python product_changes.py
```

### 5️⃣ Launch the Dashboard

Run the Streamlit app to visualize price trends.

```bash
streamlit run dashboard.py
```

📌 **Dashboard Link:** [Startech Price Tracker](<https://startech-price-tracker.streamlit.app//>)

---

## 🛠️ Requirements

- Python 3.x
- `pandas`
- `selenium`
- `beautifulsoup4`
- `streamlit`

### 🔹 Installation

Install dependencies using pip:

```bash
pip install pandas selenium beautifulsoup4 streamlit
```

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
---
## **Contact**
For inquiries or collaboration:
- **Email**: abidmuntasir.am@gmail.com
- **GitHub**: [AbidMuntasir](https://github.com/AbidMuntasir)



