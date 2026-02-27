import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="VantagePro AI Suite", page_icon="🛡️", layout="wide")

# 2. Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. Master Connection (REPLACE WITH YOUR LINK)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"

# 4. Session State for Login
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- LOGIN PAGE ---
if not st.session_state.authenticated:
    st.title("🛡️ VantagePro AI Suite")
    st.sidebar.title("Login Area")
    
    passkey_input = st.sidebar.text_input("Enter Passkey", type="password")
    if st.sidebar.button("Login"):
        clean_key = passkey_input.strip()
        
        # A. Check Master Key
        if clean_key == "Joseph":
            st.session_state.authenticated = True
            st.rerun()
            
        # B. Check Google Sheet
        else:
            try:
                df = pd.read_csv(SHEET_URL)
                # Ensure headers match your sheet exactly
                df.columns = df.columns.str.strip() 
                
                # Look for the passkey
                user_row = df[df['Passkey'].astype(str) == clean_key]
                
                if not user_row.empty:
                    status = str(user_row.iloc[0]['Status']).strip()
                    expiry_date = str(user_row.iloc[0]['Date']).strip()
                    
                    # Check Expiry Date if it exists
                    is_expired = False
                    if expiry_date != 'nan' and expiry_date != '':
                        try:
                            # Formats date like 2026-12-31
                            exp_dt = datetime.strptime(expiry_date, '%Y-%m-%d')
                            if datetime.now() > exp_dt:
                                is_expired = True
                        except:
                            pass # If date format is wrong, we ignore it
                    
                    if is_expired:
                        st.sidebar.error("❌ This passkey has expired.")
                    elif status != "Active":
                        st.sidebar.error("❌ This key is inactive.")
                    else:
                        st.session_state.authenticated = True
                        st.rerun()
                else:
                    st.sidebar.error("❌ Invalid Passkey.")
            except Exception as e:
                st.sidebar.error("Database connection failed. Please check your sheet link.")

    # Purchase Section
    st.write("### Access Required")
    st.write("Please enter a valid passkey in the sidebar or purchase one below.")
    if st.button("💳 Get Instant Passkey via Paystack"):
        st.write("Redirecting to Paystack...")

# --- DASHBOARD PAGE ---
else:
    st.balloons()
    st.sidebar.success("Logged In")
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

    st.title("🚀 VantagePro AI Dashboard")
    st.write("Select a tool below to get started.")
    
    # TOOLS WILL GO HERE
    col1, col2 = st.columns(2)
    with col1:
        st.info("🛠️ AI Bypassing Tool (Ready to install)")
    with col2:
        st.info("📊 Snap-to-Excel Tool (Ready to install)")
