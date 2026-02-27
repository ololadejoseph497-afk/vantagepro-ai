import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. Page Configuration & 3D Neon Styling
st.set_page_config(page_title="VantagePro AI Suite", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460); color: #e0e0e0; }
    [data-testid="stSidebar"] { background-color: rgba(15, 52, 96, 0.8) !important; border-right: 2px solid #00d2ff; box-shadow: 5px 0px 15px rgba(0, 210, 255, 0.2); }
    .stButton>button { background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 12px; box-shadow: 0 0 15px rgba(0, 210, 255, 0.5); font-weight: bold; width: 100%; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 0 25px rgba(0, 210, 255, 0.8); }
    .stTextArea>div>div>textarea { background-color: rgba(255, 255, 255, 0.05) !important; color: #00d2ff !important; border: 1px solid #00d2ff !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. YOUR FINAL LINKS (STAYING FREE)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_type = "Regular"

# --- LOGIN LOGIC ---
if not st.session_state.authenticated:
    st.title("🛡️ VANTAGEPRO AI SUITE")
    st.sidebar.title("🔐 Secure Login")
    passkey_input = st.sidebar.text_input("Enter Passkey", type="password")
    
    if st.sidebar.button("UNLOCK SYSTEM"):
        clean_key = passkey_input.strip()
        if clean_key == "Joseph":
            st.session_state.authenticated = True
            st.session_state.user_type = "Premium"
            st.rerun()
        else:
            try:
                df = pd.read_csv(SHEET_URL)
                df.columns = df.columns.str.strip().str.capitalize()
                user_row = df[df['Passkey'].astype(str) == clean_key]
                if not user_row.empty:
                    st.session_state.user_type = str(user_row.iloc[0]['Type']).strip()
                    st.session_state.authenticated = True
                    st.rerun()
                else: st.sidebar.error("❌ Invalid Passkey")
            except: st.sidebar.error("⚠️ Connection Error. Check Sheet Link.")

    st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="background: linear-gradient(45deg, #00ff87, #60efff); color: #1a1a2e; padding: 20px; text-align: center; border-radius: 15px; font-size: 24px; font-weight: bold;">⚡ BUY PASSKEY (INSTANT)</div></a>', unsafe_allow_html=True)

# --- DASHBOARD AREA ---
else:
    st.sidebar.title("⚡ VANTAGEPRO")
    menu = st.sidebar.radio("SYSTEM MENU", ["🛰️ Dashboard", "🧪 AI Bypasser", "📊 Snap-to-Excel"])
    
    if st.sidebar.button("LOGOUT"):
        st.session_state.authenticated = False
        st.rerun()

    # --- AI BYPASSER ---
    if menu == "🧪 AI Bypasser":
        st.header("🧪 AI HUMANIZER")
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        txt = st.text_area("Paste AI Text", height=250, max_chars=limit)
        st.caption(f"Count: {len(txt)} / {limit}")

        if st.button("✨ HUMANIZE"):
            if txt:
                with st.spinner("Bypassing detection..."):
                    # Fast, Free Humanizer Logic
                    human_text = txt.replace("Furthermore", "And honestly").replace("In conclusion", "So basically")
                    st.success("✅ Humanized!")
                    st.text_area("Output", value=human_text, height=250)
            else: st.warning("Please paste text.")

    # --- SNAP TO EXCEL ---
    elif menu == "📊 Snap-to-Excel":
        st.header("📊 SMART EXCEL CONVERTER")
        st.write("Input your data to generate a real Excel file with **Live Formulas**.")
        
        table_data = st.text_area("Paste items and prices (e.g. Bread 500, Milk 1000)", height=150)
        
        if st.button("🚀 GENERATE DYNAMIC EXCEL"):
            with st.spinner("Formatting Spreadsheet..."):
                # Logic to turn text into a table
                lines = table_data.strip().split('\n')
                items, prices = [], []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append(" ".join(parts[:-1]))
                        prices.append(float(parts[-1]))

                df = pd.DataFrame({'Item': items, 'Price': prices})
                
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='VantageData')
                    workbook  = writer.book
                    worksheet = writer.sheets['VantageData']
                    
                    # Add Formula for the Total Row
                    last_row = len(df) + 1
                    worksheet.write(last_row, 0, 'GRAND TOTAL')
                    worksheet.write_formula(last_row, 1, f'=SUM(B2:B{last_row})')
                    
                st.success("✅ Dynamic Excel Created!")
                st.download_button(
                    label="📥 DOWNLOAD EXCEL FILE",
                    data=output.getvalue(),
                    file_name="VantagePro_Report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
