import streamlit as st
import pandas as pd

# This version has a built-in key so Google Sheets won't block you!
st.set_page_config(page_title="VantagePro AI Suite", layout="wide")

# CSS for styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ VantagePro AI Suite")

# Sidebar Login
st.sidebar.header("User Authentication")
passkey = st.sidebar.text_input("Enter Passkey", type="password")

# THE "EMERGENCY" LOGIN LOGIC
if passkey:
    if passkey == "Joseph family":
        st.sidebar.success("Access Granted: Permanent")
        st.balloons()
        
        st.header("Welcome to the Dashboard")
        st.write("You are now logged in as a Family Member.")
        
        # This is where your tools will go next!
        st.info("The AI Bypassing and Excel tools are ready to be added here.")
        
    else:
        # Check Google Sheet as a backup for other customers
        try:
            # Replace the URL below with your link one last time if you want to test it
            SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
            df = pd.read_csv(SHEET_URL)
            user_data = df[df['Passkey'] == passkey]
            
            if not user_data.empty:
                status = user_data.iloc[0]['Status']
                if status == "Active":
                    st.sidebar.success("Access Granted")
                    st.write("Welcome, Customer!")
                else:
                    st.sidebar.error("Key Expired or Inactive")
            else:
                st.sidebar.error("Invalid Passkey")
        except:
            st.sidebar.error("Database Connection Error - But 'Joseph family' key will still work!")

else:
    st.warning("Please enter your passkey in the sidebar to begin.")
    if st.button("Purchase Access"):
        st.write("Redirecting to Paystack...")
