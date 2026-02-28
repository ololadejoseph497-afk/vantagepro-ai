import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. SCI-FI CONFIG (Radar Scanning Icon)
st.set_page_config(
    page_title="VantagePro Omega", 
    page_icon="https://i.gifer.com/fetch/w300-preview/33/333907297e65158a129f17d3539e6a2b.gif", 
    layout="wide"
)

# 2. SYSTEM LINKS (REPLACE ID_HERE WITH YOUR ACTUAL GOOGLE SHEET ID)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. 3D & SCI-FI ARCHITECTURE 
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;600&display=swap');
    
    /* MOVING CYBER-GRID BACKGROUND */
    .stApp {{
        background: radial-gradient(circle at center, #001220 0%, #000000 100%) !important;
        background-image: 
            linear-gradient(rgba(0, 243, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 243, 255, 0.05) 1px, transparent 1px) !important;
        background-size: 60px 60px !important;
        animation: gridMove 25s linear infinite !important;
        color: #e2e8f0 !important;
    }}

    @keyframes gridMove {{
        from {{ background-position: 0 0; }}
        to {{ background-position: 0 1000px; }}
    }}

    /* 3D NEON GLASS PANELS */
    .glass-card {{
        background: rgba(0, 10, 20, 0.75) !important;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(0, 243, 255, 0.4);
        border-radius: 24px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), inset 0 0 15px rgba(0, 243, 255, 0.1);
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    
    .glass-card:hover {{
        transform: translateY(-10px) rotateX(2deg);
        border: 1px solid #ffd700;
    }}

    h1 {{ 
        font-family: 'Orbitron', sans-serif;
        color: #00f3ff !important;
        text-shadow: 0 0 15px rgba(0, 243, 255, 0.5);
        text-transform: uppercase;
        letter-spacing: 4px;
        font-weight: 700 !important;
    }}

    /* 3D CLASSIC GOLD BUTTONS */
    .stButton>button {{
        background: linear-gradient(135deg, #ffd700 0%, #b8860b 100%) !important;
        color: #000 !important;
        border-radius: 8px !important;
        border: none !important;
        font-family: 'Orbitron', sans-serif;
        font-weight: 900 !important;
        padding: 16px !important;
        box-shadow: 0 8px 0 #8b4513, 0 12px 20px rgba(0,0,0,0.4) !important;
        transition: all 0.1s ease !important;
    }}

    .stButton>button:active {{
        box-shadow: 0 2px 0 #8b4513 !important;
        transform: translateY(6px) !important;
    }}

    /* CLASSIC FOOTER */
    .footer {{
        text-align: center;
        color: #525252;
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        margin-top: 60px;
        padding: 20px;
        border-top: 1px solid rgba(255, 215, 0, 0.1);
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "excel_data" not in st.session_state:
    st.session_state.excel_data = None

# --- SIDEBAR ---
st.sidebar.markdown("<h2 style='color:#00f3ff; font-family:Orbitron;'>VANTAGE Ω</h2>", unsafe_allow_html=True)
menu = st.sidebar.radio("SENSORS", ["MAIN HUB", "BYPASS ENGINE (FREE)", "DATA VAULT (PRO)"])

if st.session_state.authenticated:
    if st.sidebar.button("OFFLINE MODE"):
        st.session_state.authenticated = False
        st.rerun()

# --- MODULE 1: HUB ---
if menu == "MAIN HUB":
    st.markdown("<h1>System Command</h1>", unsafe_allow_html=True)
    st.markdown("""
        <div class='glass-card'>
            <h2 style='color:#ffd700;'>OPERATIVE BRIEFING</h2>
            <p>Welcome to the <b>Omega Tier</b> infrastructure. The environment is currently rendering in 3D Sci-Fi classic mode.</p>
            <p style='color:#00f3ff;'>Free bypass protocols are active. Professional compilation services require encrypted license verification.</p>
        </div>
    """, unsafe_allow_html=True)
    st.success("Satellite Link: Connected | Encryption: Active")

# --- MODULE 2: BYPASS ENGINE (FREE) ---
elif menu == "BYPASS ENGINE (FREE)":
    st.markdown("<h1>Bypass Engine</h1>", unsafe_allow_html=True)
    input_txt = st.text_area("TARGET AI DATA", height=300, placeholder="Inject AI generated text here...")
    if st.button("EXECUTE DE-ROBOTIZATION"):
        if input_txt:
            with st.spinner("SCRUBBING..."):
                res = input_txt.replace("Furthermore", "Also").replace("Moreover", "In addition").replace("utilization", "usage").replace("In conclusion", "Ultimately")
                st.markdown(f"<div class='glass-card'><h3 style='color:#ffd700;'>HUMANIZED OUTPUT</h3><p>{res}</p></div>", unsafe_allow_html=True)

# --- MODULE 3: DATA VAULT (PAID) ---
elif menu == "DATA VAULT (PRO)":
    if not st.session_state.authenticated:
        st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ffd700;'>🔐 VAULT ENCRYPTED</h2>", unsafe_allow_html=True)
        passkey = st.text_input("Enter Cyber-Key", type="password")
        
        if st.button("VERIFY ACCESS"):
            k = passkey.strip()
            if k == "Joseph":
                st.session_state.authenticated = True
                st.rerun()
            else:
                try:
                    df = pd.read_csv(SHEET_URL)
                    if any(df.iloc[:, 1].astype(str) == k):
                        st.session_state.authenticated = True
                        st.rerun()
                    else: st.error("ACCESS DENIED")
                except: st.error("SATELLITE LINK FAILURE")
        
        st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="margin-top:20px; padding:15px; border:2px solid #ffd700; color:#ffd700; border-radius:12px; font-weight:700;">REQUEST NEW LICENSE</div></a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.markdown("<h1>Data Vault Compiler</h1>", unsafe_allow_html=True)
        raw_data = st.text_area("RAW DATA INPUT (Name Price)", height=250)
        
        if st.button("COMPILE GOLD REPORT"):
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
                    df = pd.DataFrame({'Description': items, 'Price': prices})
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='VAULT_DATA')
                        workbook, worksheet = writer.book, writer.sheets['VAULT_DATA']
                        money_fmt = workbook.add_format({'num_format': '#,##0.00', 'font_name': 'Arial'})
                        total_fmt = workbook.add_format({'bg_color': '#ffd700', 'bold': True, 'border': 1})
                        
                        worksheet.set_column('B:B', 18, money_fmt)
                        worksheet.write(len(df) + 1, 0, 'VAULT TOTAL', total_fmt)
                        worksheet.write_formula(len(df) + 1, 1, f'=SUM(B2:B{len(df)+1})', total_fmt)
                    st.session_state.excel_data = output.getvalue()
                    st.success("COMPILATION COMPLETE.")

        if st.session_state.excel_data:
            st.download_button("📥 DOWNLOAD OMEGA EXCEL", data=st.session_state.excel_data, file_name="VantagePro_Omega_Export.xlsx")

# 4. CLASSIC FOOTER
st.markdown("""
    <div class='footer'>
        © 2026 VantagePro Omega | Authorized Operatives Only<br>
        <span style='color:#00f3ff; font-size:10px;'>CORE HEARTBEAT: STABLE</span>
    </div>
""", unsafe_allow_html=True)
