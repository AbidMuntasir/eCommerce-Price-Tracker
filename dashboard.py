import streamlit as st
import pandas as pd


# Load CSV files
price_drop_df = pd.read_csv('data/price_drops.csv')  # Products with price drops
new_product_df = pd.read_csv('data/new_products.csv')  # Newly added products

# Streamlit Page Config
st.set_page_config(page_title="Startech Price Tracker", page_icon="https://www.startech.com.bd/image/catalog/logo.png", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #121212;
            color: #e0e0e0;
        }
        a {
            text-decoration: none !important;
            color: inherit !important;
        }
        .product-card {
            background-color: #262730;  
            padding: 10px;  
            border-radius: 10px;
            margin: 10px;
            margin-left:9%;
            width: 80%; 
            height: auto;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.5);
        }
        .product-title {
            font-size: 18px; 
            font-weight: bold;
            margin-top: 10px;
            color: #e0e0e0;
            display: -webkit-box;
            -webkit-line-clamp: 2; /* Allows up to 2 lines */
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
            
        }
        .product-price {
            font-size: 16px; 
            font-weight: bold;
            color: #ff6f61;
            margin-top: 5px;
        }
        .old-price {
            font-size: 14px;  
            text-decoration: line-through;
            color: #999999;
            margin-top: 5px;  
        }
        .product-category {
            font-size: 12px;  
            color: #b0b0b0;
            margin-top: 5px;
        }
        .stTabs [role="tablist"] button {
            font-size: 18px;
        }
        .stSelectbox, .stTextInput {
            margin-bottom: 20px;
        }
        .main-title {
            text-align: center;
            color: #ff6f61 !important;  
        }
        @media (max-width: 940px) {
            .product-title {
                font-size: 16px;  /* Smaller font size */
            }
            .product-price {
                font-size: 14px;  /* Smaller font size */
            }
            .old-price {
                font-size: 12px;  /* Smaller font size */
            }
            .product-category {
                font-size: 10px;  /* Smaller font size */
            }
        }
        @media (max-width: 1200px) and (min-width: 640px) {
            .old-price {
                display:block;
            }
        }
        @media (max-width: 640px) {
            
            .product-title {
                font-size: 18px;  /* Return to actual value */
            }
            .product-price {
                font-size: 16px;  /* Return to actual value */
            }
            .old-price {
                font-size: 14px;  /* Return to actual value */
            }
            .product-category {
                font-size: 12px;  /* Return to actual value */
            }
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<a href='https://www.startech.com.bd/' target='_blank'><h1 class='main-title'>Startech Price Tracker</h1></a>", unsafe_allow_html=True)

# Create Tabs for Price Drops & New Products
tab1, tab2 = st.tabs(["Price Drops", "New Products"])

# ------------------ PRICE DROP SECTION ------------------
with tab1:
    st.subheader("Products with Price Drops")

    # Filter by Category and Search by Product Name
    col1, col2 = st.columns(2)
    with col1:
        categories = ['All'] + list(price_drop_df['product category'].unique())
        selected_category = st.selectbox("Select Category", options=categories, key='price_drop_category')
    with col2:
        search_query = st.text_input("Search Product", key='price_drop_search')

    # Filter DataFrame
    filtered_df = price_drop_df[
        ((price_drop_df['product category'] == selected_category) | (selected_category == 'All')) &
        (price_drop_df['product name'].str.contains(search_query, case=False))
    ]

    if not filtered_df.empty:
        num_cols = 5  # Number of columns
        rows = [filtered_df.iloc[i:i + num_cols] for i in range(0, len(filtered_df), num_cols)]
        for row in rows:
            cols = st.columns(num_cols)
            for col, (_, product) in zip(cols, row.iterrows()):
                col.markdown(f"""
                    <a href="{product['product link']}" target="_blank">
                        <div class="product-card">
                            <img src="{product['product image']}" alt="{product['product name']}" style="width:100%; height:auto; border-radius: 10px;">
                            <div class="product-title">{product['product name']}</div>
                            <div class="product-price">{product['new price']} ৳
                                <span class="old-price">{product['old price']} ৳</span>
                            </div>
                            <div class="product-category">{product['product category']}</div>
                        </div>
                    </a>
                """, unsafe_allow_html=True)
    else:
        st.info("No price drops found for the selected category or search query.")

# ------------------ NEW PRODUCT SECTION ------------------
with tab2:
    st.subheader("Newly Added Products")

    # Filter by Category and Search by Product Name
    col1, col2 = st.columns(2)
    with col1:
        categories = ['All'] + list(new_product_df['product category'].unique())
        selected_category = st.selectbox("Select Category", options=categories, key='new_product_category')
    with col2:
        search_query = st.text_input("Search Product", key='new_product_search')

    # Filter DataFrame
    filtered_df = new_product_df[
        ((new_product_df['product category'] == selected_category) | (selected_category == 'All')) &
        (new_product_df['product name'].str.contains(search_query, case=False))
    ]

    if not filtered_df.empty:
        num_cols = 5  # Number of columns
        rows = [filtered_df.iloc[i:i + num_cols] for i in range(0, len(filtered_df), num_cols)]
        for row in rows:
            cols = st.columns(num_cols)
            for col, (_, product) in zip(cols, row.iterrows()):
                col.markdown(f"""
                    <a href="{product['product link']}" target="_blank">
                        <div class="product-card">
                            <img src="{product['product image']}" alt="{product['product name']}" style="width:100%; height:auto; border-radius: 10px;">
                            <div class="product-title">{product['product name']}</div>
                            <div class="product-price">{product['product price']} ৳</div>
                            <div class="product-category">{product['product category']}</div>
                        </div>
                    </a>
                """, unsafe_allow_html=True)
    else:
        st.info("No new products found for the selected category or search query.")
