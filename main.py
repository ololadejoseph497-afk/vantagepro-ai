import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. UNIVERSAL CONFIG
st.set_page_config(
    page_title="VantagePro", 
    page_icon="https://cdn-icons-png.flaticon.com/512/2092/2092663.png", 
    layout="wide"
)

# 2. DATABASE & PAYMENT (REPLACE ID_HERE WITH YOUR SHEET ID)
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. SMART GLASS STYLING
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="st-"] {{ font-family: 'Inter', sans-serif; }}
    .stApp {{
        background: radial-gradient(circle at center, #0f172a, #020617);
        background-attachment: fixed;
        color: #f8fafc;
    }}
    .glass-card {{
        background: rgba(15, 23, 42, 0.85) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
    }}
    h1 {{ font-size: 1.6rem !important; color: #38bdf8; font-weight: 600; }}
    [data-testid="stSidebar"] {{
        background-color: rgba(2, 6, 23, 0.95) !important;
        border-right: 1px solid rgba(56, 189, 248, 0.2);
    }}
    .stButton>button {{
        background: linear-gradient(90deg, #0ea5e9, #2563eb);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        box-shadow: 0 0 20px rgba(14, 165, 233, 0.5);
        transform: translateY(-1px);
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize Session States
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_type" not in st.session_state:
    st.session_state.user_type = "Regular"
if "excel_data" not in st.session_state:
    st.session_state.excel_data = None

# --- AUTHENTICATION PAGE ---
if not st.session_state.authenticated:
    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown("""
            <div class='glass-card' style='text-align: center;'>
                <img src='https://cdn-icons-png.flaticon.com/512/2092/2092663.png' width='50'>
                <h1>VantagePro AI</h1>
                <p style='color:#94a3b8;'>Secure Infrastructure Access</p>
            </div>
        """, unsafe_allow_html=True)
        
        passkey = st.text_input("Access Passkey", type="password", placeholder="Enter License Key...")
        
        if st.button("Unlock System"):
            key = passkey.strip()
            if key == "Joseph":
                st.session_state.authenticated = True
                st.session_state.user_type = "Premium"
                st.rerun()
            else:
                try:
                    df = pd.read_csv(SHEET_URL)
                    df.columns = df.columns.str.strip().str.capitalize()
                    user_row = df[df['Passkey'].astype(str) == key]
                    if not user_row.empty:
                        st.session_state.user_type = str(user_row.iloc[0]['Type']).strip()
                        st.session_state.authenticated = True
                        st.rerun()
                    else:
                        st.error("Invalid Passkey")
                except Exception as e:
                    st.error("Database Connection Offline. Check Sheet URL.")

        st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="margin-top:10px; padding: 12px; text-align: center; border: 1px solid #10b981; border-radius: 8px; color: #10b981; font-weight: 600;">Purchase New License</div></a>', unsafe_allow_html=True)

# --- DASHBOARD AREA ---
else:
    st.sidebar.markdown("### 🛡️ VantagePro v1.0")
    menu = st.sidebar.radio("Modules", ["Home", "AI Humanizer", "Data Compiler"])
    
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.excel_data = None
        st.rerun()

    if menu == "Home":
        st.markdown("<h1>System Command Center</h1>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<div class='glass-card'><h3>User Tier</h3><h2 style='color:#38bdf8;'>{st.session_state.user_type}</h2></div>", unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='glass-card'><h3>Core Status</h3><h2 style='color:#10b981;'>Ready</h2></div>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'><h3>Active Brief</h3><p style='color:#94a3b8;'>Welcome back. Select a module from the sidebar. Premium users have bypass priority and unlimited file generation.</p></div>", unsafe_allow_html=True)

    elif menu == "AI Humanizer":
        st.markdown("<h1>AI Humanizer</h1>", unsafe_allow_html=True)
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        input_txt = st.text_area("Input Stream", height=250, max_chars=limit)
        st.caption(f"Load: {len(input_txt)} / {limit} characters")
        
        if st.button("Start Humanization"):
            if input_txt:
                with st.spinner("Processing..."):
                    res = input_txt.replace("Furthermore", "Also").replace("Moreover", "In addition").replace("utilization", "use").replace("In conclusion", "So basically")
                    st.markdown(f"<div class='glass-card'><h3>Result</h3><p>{res}</p></div>", unsafe_allow_html=True)
            else:
                st.warning("Please enter text to humanize.")

    elif menu == "Data Compiler":
        st.markdown("<h1>Data Compiler</h1>", unsafe_allow_html=True)
        st.write("Input raw list (Item Price) to generate an Excel file.")
        raw_data = st.text_area("Paste Data (Example: Bread 500)", height=200)
        
        if st.button("Generate Report"):
            if raw_data:
                lines = raw_data.strip().split('\n')
                items, prices = [], []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append(" ".join(parts[:-1]))
                        try:
                            prices.append(float(parts[-1].replace(',', '')))
                        except:
                            prices.append(0.0)
                
                if items:
                    df = pd.DataFrame({'Description': items, 'Price': prices})
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='Report')
                        workbook, worksheet = writer.book, writer.sheets['Report']
                        money_fmt = workbook.add_format({'num_format': '#,##0.00'})
                        last_row = len(df)
                        worksheet.set_column('B:B', 15, money_fmt)
                        worksheet.write(last_row + 1, 0, 'TOTAL')
                        worksheet.write_formula(last_row + 1, 1, f'=SUM(B2:B{last_row+1})', money_fmt)
                    
                    st.session_state.excel_data = output.getvalue()
                    st.success("✅ Excel Compiled Successfully!")
                else:
                    st.error("Invalid Format. Use: 'Item Price'")

        if st.session_state.excel_data:
            st.download_button(
                label="📥 DOWNLOAD EXCEL FILE",
                data=st.session_state.excel_data,
                file_name=f"VantagePro_{datetime.now().strftime('%d_%m')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
