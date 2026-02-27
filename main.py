import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURATION ---
# Replace the link below with your Google Sheet link (ending in /export?format=csv)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/edit?usp=drivesdk"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

def check_access(user_key):
    try:
        df = pd.read_csv(SHEET_URL)
        # Clean the data
        df['Passkey'] = df['Passkey'].astype(str).str.strip()
        
        # Check if the key exists and is Active
        user_row = df[(df['Passkey'] == user_key) & (df['Status'] == 'Active')]
        
        if not user_row.empty:
            return True, user_row.iloc[0]['Type']
        return False, None
    except Exception as e:
        st.error("Database connection error. Please try again.")
        return False, None

# --- WEBSITE INTERFACE ---
st.set_page_config(page_title="VantagePro AI", page_icon="🚀")

st.sidebar.title("🔐 VantagePro Login")
user_input = st.sidebar.text_input("Enter Passkey:", type="password")

if st.sidebar.button("Unlock Tools"):
    is_valid, user_type = check_access(user_input)
    
    if is_valid:
        st.sidebar.success(f"Access Granted: {user_type}")
        st.session_state['authenticated'] = True
    else:
        st.sidebar.error("Invalid or Expired Key")

# --- LOCKED CONTENT ---
if 'authenticated' not in st.session_state:
    st.title("🏆 VantagePro AI Suite")
    st.info("Please enter your passkey in the sidebar to begin.")
    st.write("Don't have a key? Get one instantly below:")
    st.link_button("💳 Purchase Access (₦5,000)", PAYSTACK_LINK)
else:
    # --- YOUR AI TOOLS GO HERE ---
    st.title("🔓 VantagePro AI Dashboard")
    st.write("Welcome back! Select a tool from the menu.")
    # (Add your tool buttons/logic here)
