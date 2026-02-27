import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="VantagePro AI Suite", page_icon="🛡️", layout="wide")

# 2. YOUR LINKS - UPDATE THESE!
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. Styling the Purchase Button
st.markdown("""
    <style>
    .pay-btn {
        display: block;
        width: 100%;
        text-align: center;
        background-color: #00bb77;
        color: white !important;
        padding: 15px;
        text-decoration: none;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        margin-top: 20px;
    }
    .pay-btn:hover { background-color: #008855; }
    </style>
    """, unsafe_allow_html=True)

# 4. Auth Logic
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- LOGIN PAGE ---
if not st.session_state.authenticated:
    st.title("🛡️ VantagePro AI Suite")
    
    st.sidebar.title("Login Area")
    # Adding 'on_change' or simply the text_input allows 'Enter' key to work
    passkey_input = st.sidebar.text_input("Enter Passkey", type="password")
    submit_button = st.sidebar.button("Login")
    
    # If they click the button OR hit enter
    if submit_button or (passkey_input and len(passkey_input) > 0):
        # We only trigger the login if they actually pressed a button or we can check via session_state
        # But in Streamlit, hitting 'Enter' on a text_input automatically refreshes the script.
        
        clean_key = passkey_input.strip()
        
        if clean_key == "Joseph":
            st.session_state.authenticated = True
            st.rerun()
        elif clean_key != "":
            try:
                df = pd.read_csv(SHEET_URL)
                df.columns = df.columns.str.strip()
                user_row = df[df['Passkey'].astype(str) == clean_key]
                
                if not user_row.empty:
                    status = str(user_row.iloc[0]['Status']).strip()
                    expiry_date = str(user_row.iloc[0]['Date']).strip()
                    
                    # Date/Expiry Check
                    is_expired = False
                    if expiry_date != 'nan' and expiry_date != '':
                        try:
                            exp_dt = datetime.strptime(expiry_date, '%Y-%m-%d')
                            if datetime.now() > exp_dt:
                                is_expired = True
                        except: pass
                    
                    if is_expired:
                        st.sidebar.error("❌ Key Expired")
                    elif status != "Active":
                        st.sidebar.error("❌ Key Inactive")
                    else:
                        st.session_state.authenticated = True
                        st.rerun()
                else:
                    # Only show error if they actually tried to log in
                    if submit_button:
                        st.sidebar.error("❌ Invalid Passkey")
            except:
                st.sidebar.error("Database Connection Error")

    # --- MAIN SCREEN ---
    st.markdown("### 🔑 Instant Access")
    st.write("Unlock the AI Bypassing and Excel Automation tools below.")
    
    # This is your Paystack Button
    st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" class="pay-btn">💳 BUY PASSKEY INSTANTLY</a>', unsafe_allow_html=True)
    
    st.write("---")
    st.caption("Passkeys are delivered to your email address immediately after payment confirmation.")

# --- DASHBOARD PAGE ---
else:
    st.title("🚀 VantagePro AI Dashboard")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"authenticated": False}))
    
    st.success("Access Granted. System is active.")
    
    # TOOLS GO HERE
    st.subheader("Your AI Toolkit")
    # ... TOOL CODE WILL BE INSERTED HERE ...
