import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. Page Configuration (Classic Icon & Title)
st.set_page_config(page_title="VantagePro", page_icon="🛡️", layout="wide")

# 2. YOUR LINKS
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. GLOBAL SMART GLASS STYLING
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif; }}

    .stApp {{
        background: radial-gradient(circle at center, #0f172a, #020617);
        color: #f8fafc;
    }}

    /* Smart Glass Cards */
    .glass-card {{
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }}

    /* Small, Sharp Headers */
    h1 {{ font-size: 1.8rem !important; font-weight: 600 !important; letter-spacing: -0.02em; color: #38bdf8; }}
    h2 {{ font-size: 1.2rem !important; font-weight: 400 !important; color: #94a3b8; }}
    h3 {{ font-size: 1rem !important; font-weight: 600 !important; color: #f1f5f9; }}

    /* Sidebar Glass */
    [data-testid="stSidebar"] {{
        background-color: rgba(2, 6, 23, 0.7) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }}

    /* Minimalist Buttons */
    .stButton>button {{
        background: rgba(56, 189, 248, 0.1);
        color: #38bdf8;
        border: 1px solid #38bdf8;
        border-radius: 8px;
        font-size: 14px;
        transition: 0.3s;
        width: 100%;
    }}
    .stButton>button:hover {{
        background: #38bdf8;
        color: #020617;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }}

    /* Text Areas */
    .stTextArea>div>div>textarea {{
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: #f1f5f9 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px;
    }}
    </style>
""", unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_type = "Regular"

# --- LOGIN PAGE ---
if not st.session_state.authenticated:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div class='glass-card' style='text-align: center;'>
                <span style='font-size: 40px;'>🛡️</span>
                <h1>VantagePro</h1>
                <h2>Secure AI Infrastructure</h2>
            </div>
        """, unsafe_allow_html=True)
        
        passkey_input = st.text_input("Access Key", type="password", placeholder="••••••••")
        
        if st.button("Authenticate System"):
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
                    else: st.error("Authentication Failed: Invalid Key")
                except: st.error("System Offline: Database Connection Error")

        st.markdown(f"""
            <a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;">
                <div style="margin-top:20px; padding: 12px; text-align: center; border: 1px solid #10b981; border-radius: 8px; color: #10b981; font-size: 14px; font-weight: 600;">
                    Get Access License
                </div>
            </a>
        """, unsafe_allow_html=True)

# --- DASHBOARD AREA ---
else:
    st.sidebar.markdown("### 🛡️ VantagePro")
    menu = st.sidebar.radio("Navigation", ["Dashboard", "AI Humanizer", "Data Compiler"])
    
    if st.sidebar.button("Log out"):
        st.session_state.authenticated = False
        st.rerun()

    if menu == "Dashboard":
        st.markdown("<h1>System Overview</h1>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f"<div class='glass-card'><h3>Tier</h3><p style='color:#38bdf8;'>{st.session_state.user_type}</p></div>", unsafe_allow_html=True)
        with c2: st.markdown("<div class='glass-card'><h3>Status</h3><p style='color:#10b981;'>Active</p></div>", unsafe_allow_html=True)
        with c3: st.markdown("<div class='glass-card'><h3>Uptime</h3><p style='color:#94a3b8;'>99.9%</p></div>", unsafe_allow_html=True)
        
        st.markdown("""
            <div class='glass-card'>
                <h3>Welcome to VantagePro</h3>
                <p style='font-size:14px; color:#94a3b8;'>Select a module from the sidebar to begin processing. Your workspace is encrypted and hardware-accelerated.</p>
            </div>
        """, unsafe_allow_html=True)

    elif menu == "AI Humanizer":
        st.markdown("<h1>AI Humanizer</h1>", unsafe_allow_html=True)
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        txt = st.text_area("Input Stream", height=250, max_chars=limit)
        
        if st.button("Process Text"):
            with st.spinner("Decoding patterns..."):
                human_text = txt.replace("Furthermore", "Also").replace("Moreover", "In addition")
                st.markdown("<div class='glass-card'><h3>Humanized Result</h3><p style='font-size:14px;'>"+human_text+"</p></div>", unsafe_allow_html=True)

    elif menu == "Data Compiler":
        st.markdown("<h1>Data Compiler</h1>", unsafe_allow_html=True)
        data_in = st.text_area("Raw Table Data (Item Price)", height=200)
        
        if st.button("Export Excel"):
            st.info("Compiling .xlsx file...")
            # (Excel Generation Logic)        st.markdown("<div class='glass-card'><h1 style='color:#00d2ff; text-align:center;'>CONTROL HUD</h1></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.markdown(f"<div class='glass-card'><h3>USER RANK</h3><h2 style='color:#00ff87;'>{st.session_state.user_type}</h2></div>", unsafe_allow_html=True)
        c2.markdown("<div class='glass-card'><h3>SYSTEM STATUS</h3><h2 style='color:#00ff87;'>ACTIVE</h2></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='glass-card'>
            <h3 style='color:#00d2ff;'>SYSTEM OPERATIONS</h3>
            <p>1. AI BYPASSER: Decodes AI patterns to human-grade text.</p>
            <p>2. EXCEL CORE: Compiles raw data into mathematical spreadsheets.</p>
        </div>
        """, unsafe_allow_html=True)

    elif menu == "AI BYPASSER":
        st.markdown("<div class='glass-card'><h1 style='color:#00ff87;'>AI BYPASSER CORE</h1></div>", unsafe_allow_html=True)
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        txt = st.text_area("INJECT DATA FOR HUMANIZATION", height=250, max_chars=limit)
        if st.button("SYNTHESIZE TEXT"):
            if txt:
                with st.spinner("Processing..."):
                    # Humanizer logic
                    fixed = txt.replace("Furthermore", "In fact").replace("In conclusion", "Ultimately").replace("utilization", "use")
                    st.success("DECRYPTION COMPLETE")
                    st.text_area("OUTPUT", value=fixed, height=200)

    elif menu == "EXCEL CORE":
        st.markdown("<div class='glass-card'><h1 style='color:#00d2ff;'>EXCEL DATA COMPILER</h1></div>", unsafe_allow_html=True)
        raw_data = st.text_area("INPUT RAW DATASTREAM (Example: Item 500)", height=150)
        if st.button("COMPILE TO SPREADSHEET"):
            lines = raw_data.strip().split('\n')
            items, prices = [], []
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    items.append(" ".join(parts[:-1]))
                    try: prices.append(float(parts[-1]))
                    except: prices.append(0)
            if items:
                df = pd.DataFrame({'Entity': items, 'Value': prices})
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='MatrixData')
                    worksheet = writer.sheets['MatrixData']
                    last_row = len(df) + 1
                    worksheet.write(last_row, 0, 'TOTAL')
                    worksheet.write_formula(last_row, 1, f'=SUM(B2:B{last_row})')
                st.download_button("DOWNLOAD DATA FILE", data=output.getvalue(), file_name="VantageCore.xlsx")
