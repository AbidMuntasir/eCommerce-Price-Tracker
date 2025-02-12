import streamlit as st
import pandas as pd

# Load CSV files
price_drop_df = pd.read_csv('data/price_drops.csv')  # Products with price drops
new_product_df = pd.read_csv('data/new_products.csv')  # Newly added products

# Streamlit Page Config
st.set_page_config(page_title="Price Tracker Dashboard", page_icon="💰", layout="wide")

# Custom Styling with Hover Effects
st.markdown("""
    <style>
        body { font-family: 'Arial', sans-serif; background-color: #1E1E1E; color: #E0E0E0; }

        .price-drop-card, .new-product-card { 
            background-color: #2A2A2A; 
            padding: 20px; 
            border-radius: 12px; 
            margin-bottom: 15px; 
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.4);
            width: 100%;
            transition: transform 0.2s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        
        /* Hover Effect */
        .price-drop-card:hover, .new-product-card:hover { 
            transform: translateY(-5px); 
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.6);
        }

        .title { font-size: 26px; font-weight: bold; color: #FFFFFF; }
        .price-text { font-size: 22px; font-weight: bold; color: #FF5252; }
        .old-price { text-decoration: line-through; color: #B0B0B0; }

        /* Remove Streamlit's default styling blocks */
        [data-testid="stVerticalBlock"] {
            background: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.title("📊 Product Price Tracker Dashboard")

# Create Tabs for Price Drops & New Products
tab1, tab2 = st.tabs(["🔻 Price Drops", "🆕 New Products"])

# ------------------ PRICE DROP SECTION ------------------
with tab1:
    st.subheader("📉 Products with Price Drops")

    # Filter by Category
    categories = price_drop_df['product category'].unique()
    selected_category = st.selectbox("Select Category", options=categories)

    # Search by Product Name
    search_query = st.text_input("Search Product")

    filtered_df = price_drop_df[
        (price_drop_df['product category'] == selected_category) & 
        (price_drop_df['product name'].str.contains(search_query, case=False))
    ]

    if not filtered_df.empty:
        for index, row in filtered_df.iterrows():
            st.markdown(f"""
                <div class="price-drop-card">
                    <span class="title">{row["product name"]}</span><br>
                    <span class="price-text">{row["new price"]} ৳</span> 
                    <span class="old-price">{row["old price"]} ৳</span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No price drops found for the selected category or search query.")

# ------------------ NEW PRODUCT SECTION ------------------
with tab2:
    st.subheader("🛒 Newly Added Products")

    if not new_product_df.empty:
        for index, row in new_product_df.iterrows():
            st.markdown(f"""
                <div class="new-product-card">
                    <span class="title">{row["product name"]}</span><br>
                    <span class="price-text">{row["product price"]} ৳</span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No new products added today.")
