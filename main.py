import streamlit as st
import pandas as pd
from datetime import datetime
import io
import time
import random

# 1. SCI-FI ENGINE CONFIG
st.set_page_config(
    page_title="VANTAGE OMEGA | COMMAND", 
    page_icon="📡", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATABASE CONFIG (YOUR LINK INTEGRATED) ---
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 2. THE GENIUS UI (3D Moving Grid + Neon Architecture)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300&display=swap');
    
    .stApp {{
        background: radial-gradient(circle at center, #001220 0%, #000000 100%) !important;
        background-attachment: fixed !important;
    }}
    
    /* THE MOVING SCI-FI GRID ENGINE */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(0, 243, 255, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 243, 255, 0.1) 1px, transparent 1px);
        background-size: 50px 50px;
        transform: perspective(500px) rotateX(60deg) translateY(-100px);
        animation: gridMove 12s linear infinite;
        z-index: -1;
    }}

    @keyframes gridMove {{
        0% {{ background-position: 0 0; }}
        100% {{ background-position: 0 1000px; }}
    }}

    .glass-card {{
        background: rgba(0, 15, 30, 0.8) !important;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 243, 255, 0.3);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.7);
        margin-bottom: 20px;
    }}

    h1, h2, h3 {{ font-family: 'Orbitron', sans-serif !important; color: #00f3ff !important; letter-spacing: 3px; }}
    p, span {{ font-family: 'JetBrains Mono', monospace !important; color: #e2e8f0; }}

    .stButton>button {{
        background: linear-gradient(135deg, #ffd700 0%, #b8860b 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 8px !important; padding: 12px !important; width: 100%;
        box-shadow: 0 5px 15px rgba(255, 215, 0, 0.2) !important;
        transition: 0.2s;
    }}
    
    .stButton>button:active {{
        transform: scale(0.98);
    }}
    </style>
""", unsafe_allow_html=True)

# 3. CORE LOGIC FUNCTIONS
if "authenticated" not in st.session_state: st.session_state.authenticated = False

# --- SIDEBAR ---
st.sidebar.markdown("<h1 style='color:#00f3ff; font-family:Orbitron;'>VANTAGE Ω</h1>", unsafe_allow_html=True)
menu = st.sidebar.radio("SYSTEM ACCESS", ["DASHBOARD", "AI HUMANIZER (FREE)", "DATA VAULT (PRO)"])

if st.session_state.authenticated:
    if st.sidebar.button("LOGOUT / LOCK"):
        st.session_state.authenticated = False
        st.rerun()

# --- MODULE 1: DASHBOARD ---
if menu == "DASHBOARD":
    st.markdown("<h1>Command Dashboard</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("NETWORK", "ENCRYPTED", "STABLE")
    col2.metric("SYNC MODE", "AUTO-REFRESH", "5s")
    col3.metric("OS VERSION", "OMEGA 1.5", "LATEST")
    
    st.markdown(f"""
        <div class='glass-card'>
            <h3 style='color:#ffd700;'>Welcome back, Administrator</h3>
            <p>VantagePro Omega is live. All manual tasks are now handled by the Make.com Neural Link.</p>
            <p>The system is scanning Column E for expiration dates and Column B for passkeys.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.code(f"[{datetime.now().strftime('%H:%M:%S')}] SYSTEM_CHECK: Google Database Linked\n[{datetime.now().strftime('%H:%M:%S')}] HUD_INTEGRITY: 100%")

# --- MODULE 2: AI HUMANIZER ---
elif menu == "AI HUMANIZER (FREE)":
    st.markdown("<h1>Neural Humanizer</h1>", unsafe_allow_html=True)
    txt = st.text_area("INJECT AI TEXT DATA", height=250)
    if st.button("EXECUTE"):
        if txt:
            with st.spinner("Scrubbing AI signatures..."):
                time.sleep(1)
                res = txt.replace("Furthermore", "Also").replace("Moreover", "In addition").replace("utilization", "use").replace("In conclusion", "Ultimately")
                st.markdown(f"<div class='glass-card'><h3>Scrubbed Result</h3><p>{res}</p></div>", unsafe_allow_html=True)

# --- MODULE 3: DATA VAULT (THE AUTO-SYNC LOCK) ---
elif menu == "DATA VAULT (PRO)":
    if not st.session_state.authenticated:
        st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ffd700;'>🔐 ENCRYPTED VAULT</h2>", unsafe_allow_html=True)
        pk = st.text_input("Enter Passkey", type="password")
        
        if st.button("VERIFY ACCESS"):
            k = pk.strip()
            if k == "Joseph": # Master Admin Bypass
                st.session_state.authenticated = True
                st.rerun()
            else:
                try:
                    with st.spinner("Syncing with Global Database..."):
                        # FORCED CLEAR CACHE FOR INSTANT SYNC
                        st.cache_data.clear()
                        df = pd.read_csv(SHEET_URL)
                    
                    df.columns = df.columns.str.strip().str.capitalize()
                    # Check if key exists in the "Passkey" column
                    user_match = df[df['Passkey'].astype(str) == k]
                    
                    if not user_match.empty:
                        # CHECK EXPIRATION
                        expiry_val = str(user_match.iloc[0]['Date']).strip()
                        expiry_date = datetime.strptime(expiry_val, '%Y-%m-%d').date()
                        
                        if datetime.now().date() <= expiry_date:
                            st.session_state.authenticated = True
                            st.success("AUTHENTICATION SUCCESSFUL")
                            st.rerun()
                        else:
                            st.error(f"ACCESS EXPIRED: Locked on {expiry_date}")
                    else:
                        st.error("INVALID KEY: Connection Terminated.")
                except Exception as e:
                    st.error("SATELLITE LINK ERROR: Ensure Column E is named 'Date' (YYYY-MM-DD)")
        
        st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="margin-top:20px; padding:15px; border:1px solid #ffd700; color:#ffd700; border-radius:10px; font-weight:700;">GET ACCESS KEY</div></a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.markdown("<h1>Secure Data Compiler</h1>", unsafe_allow_html=True)
        raw_data = st.text_area("Input Stream (Description Price)", height=250)
        
        if st.button("EXTRACT EXCEL REPORT"):
            if raw_data:
                lines = raw_data.strip().split('\n')
                items, prices = [], []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append(" ".join(parts[:-1]))
                        try: prices.append(float(parts[-1].replace(',', '')))
                        except: prices.append(0.0)
                
                if items:
                    df_out = pd.DataFrame({'Description': items, 'Price': prices})
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df_out.to_excel(writer, index=False, sheet_name='VAULT')
                        workbook, worksheet = writer.book, writer.sheets['VAULT']
                        money_fmt = workbook.add_format({'num_format': '#,##0.00'})
                        total_fmt = workbook.add_format({'bg_color': '#ffd700', 'bold': True})
                        worksheet.set_column('B:B', 15, money_fmt)
                        worksheet.write(len(df_out) + 1, 0, 'TOTAL', total_fmt)
                        worksheet.write_formula(len(df_out) + 1, 1, f'=SUM(B2:B{len(df_out)+1})', total_fmt)
                    
                    st.download_button("📥 DOWNLOAD ENCRYPTED REPORT", data=output.getvalue(), file_name="Vantage_Omega.xlsx")
                    st.success("Extraction Complete.")

st.markdown("<p style='text-align:center; color:grey; margin-top:50px;'>© 2026 VANTAGEPRO OMEGA | INFRASTRUCTURE STATUS: SECURE</p>", unsafe_allow_html=True)
