import streamlit as st
import pandas as pd

st.set_page_config(page_title="VantagePro AI", layout="wide")

# Replace this with your link ending in /export?format=csv
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"

st.title("🛡️ VantagePro AI Suite")

# Sidebar
st.sidebar.header("Login")
user_input = st.sidebar.text_input("Enter Passkey", type="password")

if user_input:
    # 1. Check the "Emergency" key first (This ALWAYS works)
    if user_input.lower().strip() == "joseph":
        st.sidebar.success("Access Granted: Family")
        st.balloons()
        st.write("### Welcome to the Dashboard")
        st.info("You are logged in with the Master Key.")
    
    # 2. If not the emergency key, check Google Sheets
    else:
        try:
            df = pd.read_csv(SHEET_URL)
            # Clean the data (remove spaces and make lowercase for matching)
            df['Passkey'] = df['Passkey'].astype(str).str.strip()
            
            match = df[df['Passkey'] == user_input.strip()]
            
            if not match.empty:
                if match.iloc[0]['Status'].strip() == "Active":
                    st.sidebar.success("Access Granted")
                    st.write("### Welcome, Customer")
                else:
                    st.sidebar.error("This key is Inactive")
            else:
                st.sidebar.error("Invalid Passkey")
        except:
            st.sidebar.error("Connection Error: Please check your internet or Sheet link.")
else:
    st.info("Please enter your key in the sidebar to enter.")
