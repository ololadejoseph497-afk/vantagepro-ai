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

# --- DATABASE CONFIG (HARDWIRED) ---
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 2. THE GENIUS OMEGA UI (GLASS CIRCUITS & 3D GRID)
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

    @keyframes gridMove {{ 0% {{ background-position: 0 0; }} 100% {{ background-position: 0 1000px; }} }}

    /* TRANSPARENT GLASS BUTTONS WITH ELECTRIC CIRCUIT EFFECT */
    .stButton>button {{
        background: rgba(255, 215, 0, 0.03) !important;
        color: #ffd700 !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        backdrop-filter: blur(12px);
        border-radius: 10px !important;
        padding: 18px !important;
        font-family: 'Orbitron', sans-serif !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        width: 100%;
    }}

    .stButton>button:hover {{
        background: rgba(255, 215, 0, 0.1) !important;
        border: 1px solid #ffd700 !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.2);
    }}

    /* CIRCUIT FLOW EFFECT ON PRESS */
    .stButton>button:active {{
        transform: translateY(6px) scale(0.97);
        background: rgba(0, 243, 255, 0.2) !important;
        border-color: #00f3ff !important;
        color: #00f3ff !important;
        box-shadow: 0 0 30px #00f3ff, inset 0 0 15px #00f3ff;
    }}

    .glass-card {{
        background: rgba(0, 15, 30, 0.8) !important;
        backdrop-filter: blur(25px);
        border: 1px solid rgba(0, 243, 255, 0.2);
        border-radius: 20px;
        padding: 35px;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }}

    h1, h2, h3 {{ font-family: 'Orbitron', sans-serif !important; color: #00f3ff !important; text-shadow: 0 0 10px rgba(0,243,255,0.3); }}
    p, span {{ font-family: 'JetBrains Mono', monospace !important; color: #e2e8f0; }}

    /* TABS STYLING */
    .stTabs [data-baseweb="tab-list"] {{ gap: 10px; }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255,255,255,0.05) !important;
        border-radius: 5px 5px 0 0;
        color: #e2e8f0 !important;
    }}
    </style>
""", unsafe_allow_html=True)

if "authenticated" not in st.session_state: st.session_state.authenticated = False

# --- SIDEBAR ---
st.sidebar.markdown("<h1 style='color:#00f3ff; font-family:Orbitron; font-size:1.5rem;'>VANTAGE Ω</h1>", unsafe_allow_html=True)
menu = st.sidebar.radio("CORE SYSTEMS", ["DASHBOARD", "AI HUMANIZER (FREE)", "DATA VAULT (PRO)"])

if st.session_state.authenticated:
    if st.sidebar.button("TERMINATE SESSION"):
        st.session_state.authenticated = False
        st.rerun()

# --- MODULE 1: DASHBOARD ---
if menu == "DASHBOARD":
    st.markdown("<h1>Command Center</h1>", unsafe_allow_html=True)
    st.markdown("""<div class='glass-card'><h3>Status: ZAP-LINK ACTIVE</h3><p>Neural interface connected. Grid stabilizers operating at 100%. All glass circuits are capacitive and responsive.</p></div>""", unsafe_allow_html=True)
    st.code(f"[{datetime.now().strftime('%H:%M:%S')}] Pinging Gateway...\n[{datetime.now().strftime('%H:%M:%S')}] Neural Link Stable\n[{datetime.now().strftime('%H:%M:%S')}] Syncing with Google Cloud...")

# --- MODULE 2: AI HUMANIZER ---
elif menu == "AI HUMANIZER (FREE)":
    st.markdown("<h1>Neural Humanizer</h1>", unsafe_allow_html=True)
    txt = st.text_area("INJECT DATA STREAM", height=200, placeholder="Paste AI text here...")
    if st.button("EXECUTE HUMANIZATION"):
        if txt:
            with st.spinner("Scrubbing AI Signatures..."):
                time.sleep(1)
                res = txt.replace("Furthermore", "Also").replace("Moreover", "In addition").replace("utilization", "use").replace("In conclusion", "Ultimately")
                st.markdown(f"<div class='glass-card'><h3>Result</h3><p>{res}</p></div>", unsafe_allow_html=True)

# --- MODULE 3: DATA VAULT (THE VISION UPDATE) ---
elif menu == "DATA VAULT (PRO)":
    if not st.session_state.authenticated:
        st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:#ffd700;'>🔐 ENCRYPTED VAULT</h2>", unsafe_allow_html=True)
        pk = st.text_input("Enter Passkey", type="password")
        
        if st.button("VERIFY IDENTITY"):
            k = pk.strip()
            if k == "Joseph": 
                st.session_state.authenticated = True
                st.rerun()
            else:
                try:
                    # FORCED CACHE CLEAR FOR INSTANT ZAP-LINK SYNC
                    st.cache_data.clear()
                    df = pd.read_csv(SHEET_URL)
                    df.columns = df.columns.str.strip().str.capitalize()
                    user_match = df[df['Passkey'].astype(str) == k]
                    
                    if not user_match.empty:
                        expiry_val = str(user_match.iloc[0]['Date']).strip()
                        expiry_date = datetime.strptime(expiry_val, '%Y-%m-%d').date()
                        if datetime.now().date() <= expiry_date:
                            st.session_state.authenticated = True
                            st.rerun()
                        else: st.error("KEY EXPIRED")
                    else: st.error("INVALID KEY")
                except: st.error("DATABASE CONNECTION FAILURE")
        
        st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="margin-top:20px; padding:15px; border:1px solid #ffd700; color:#ffd700; border-radius:10px; font-weight:700;">REQUEST ACCESS KEY</div></a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    else:
        st.markdown("<h1>Secure Intelligence Center</h1>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📸 Neural Vision & File Scan")
        
        tab1, tab2, tab3 = st.tabs(["📁 File Upload", "📷 Camera Scanner", "⌨️ Manual Stream"])
        
        with tab1:
            uploaded_file = st.file_uploader("Upload Intel (Excel, CSV, TXT)", type=["csv", "txt", "xlsx"])
            if uploaded_file: st.success(f"Captured: {uploaded_file.name}")

        with tab2:
            cam_image = st.camera_input("Neural Scanner Active")
            if cam_image: st.image(cam_image, caption="Neural Capture Recorded")

        with tab3:
            raw_data = st.text_area("Input Raw Stream (Name Price)", height=150)
        
        st.markdown("</div>", unsafe_allow_html=True)

        if st.button("COMPILE OMEGA REPORT"):
            if raw_data:
                lines = raw_data.strip().split('\n')
                items, prices = [], []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append(" ".join(parts[:-1]))
                        try: prices.append(float(parts[-1].replace(',', '')))
                        except: prices.append(0.0)
                
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
                
                st.download_button("📥 DOWNLOAD OMEGA REPORT", data=output.getvalue(), file_name="Vantage_Omega.xlsx")
                st.success("Extraction Complete.")

st.markdown("<p style='text-align:center; color:grey; margin-top:50px;'>© 2026 VANTAGEPRO OMEGA | ZAP-LINK NEURAL INTERFACE ACTIVE</p>", unsafe_allow_html=True)
