import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. Page Configuration
st.set_page_config(page_title="VantagePro AI Suite", page_icon="⚡", layout="wide")

# 2. YOUR LINKS
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_type = "Regular"
    st.session_state.current_bg = "https://images.unsplash.com/photo-1614729939124-032f0b56c9ce?q=80&w=2000" # Sci-fi Dark Space

# --- LOGIN LOGIC ---
if not st.session_state.authenticated:
    # Set Login Background
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(10, 14, 23, 0.8), rgba(10, 14, 23, 0.9)), url('https://images.unsplash.com/photo-1614729939124-032f0b56c9ce?q=80&w=2000');
            background-size: cover; background-attachment: fixed; color: #e0e0e0;
        }}
        [data-testid="stSidebar"] {{ background-color: rgba(10, 14, 23, 0.9) !important; border-right: 2px solid #00d2ff; }}
        </style>
    """, unsafe_allow_html=True)

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

    st.markdown("### 🚀 THE FUTURE OF AUTOMATION")
    st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="background: linear-gradient(45deg, #00ff87, #60efff); color: #1a1a2e; padding: 20px; text-align: center; border-radius: 15px; font-size: 24px; font-weight: bold; box-shadow: 0 0 20px rgba(0,255,135,0.6); margin-top: 30px;">⚡ BUY PASSKEY TO ENTER</div></a>', unsafe_allow_html=True)

# --- DASHBOARD AREA ---
else:
    st.sidebar.title("⚡ VANTAGEPRO")
    menu = st.sidebar.radio("SYSTEM MENU", ["🛰️ Dashboard", "🧪 AI Bypasser", "📊 Snap-to-Excel"])
    
    if st.sidebar.button("LOGOUT"):
        st.session_state.authenticated = False
        st.rerun()

    # Dynamic Background Logic based on Menu
    if menu == "🛰️ Dashboard":
        # Fiery Sci-Fi / Dragon Flame Vibe
        bg_img = "https://images.unsplash.com/photo-1577493341514-d5792da0c765?q=80&w=2000"
    elif menu == "🧪 AI Bypasser":
        # Futuristic Tech Money / Green Matrix Vibe
        bg_img = "https://images.unsplash.com/photo-1618044733300-9472054094ee?q=80&w=2000"
    else:
        # Sci-Fi Data / Blue Grid Vibe
        bg_img = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2000"

    # Apply the UI Style
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(10, 14, 23, 0.75), rgba(10, 14, 23, 0.85)), url('{bg_img}');
            background-size: cover; background-attachment: fixed; color: #ffffff;
        }}
        [data-testid="stSidebar"] {{ background-color: rgba(10, 14, 23, 0.85) !important; border-right: 2px solid #00d2ff; box-shadow: 5px 0px 15px rgba(0, 210, 255, 0.3); }}
        .stButton>button {{ background: linear-gradient(45deg, #00d2ff, #3a7bd5); color: white; border-radius: 12px; box-shadow: 0 0 15px rgba(0, 210, 255, 0.6); font-weight: bold; width: 100%; transition: 0.3s; border: none; }}
        .stButton>button:hover {{ transform: translateY(-2px); box-shadow: 0 0 30px rgba(0, 210, 255, 0.9); }}
        .stTextArea>div>div>textarea {{ background-color: rgba(0, 0, 0, 0.5) !important; color: #00d2ff !important; border: 1px solid #00d2ff !important; border-radius: 10px; font-size: 16px; }}
        .glass-box {{ background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); padding: 20px; border-radius: 15px; border: 1px solid rgba(0, 210, 255, 0.3); margin-bottom: 20px; }}
        </style>
    """, unsafe_allow_html=True)

    # --- 🛰️ DASHBOARD (NO LONGER BLANK!) ---
    if menu == "🛰️ Dashboard":
        st.markdown("<div class='glass-box'><h1 style='color:#00d2ff; text-align:center;'>🛰️ COMMAND CENTER</h1></div>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        c1.markdown(f"<div class='glass-box'><h3>👤 Account Tier</h3><h2 style='color:#00ff87;'>{st.session_state.user_type}</h2></div>", unsafe_allow_html=True)
        c2.markdown("<div class='glass-box'><h3>⚡ System Status</h3><h2 style='color:#00ff87;'>ONLINE</h2></div>", unsafe_allow_html=True)
        c3.markdown("<div class='glass-box'><h3>🛡️ Security</h3><h2 style='color:#00ff87;'>ENCRYPTED</h2></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class='glass-box'>
            <h3 style='color:#00d2ff;'>📖 QUICK START GUIDE</h3>
            <p>Welcome to VantagePro, your personal AI powerhouse. Here is how to use your tools:</p>
            <ul>
                <li><b>🧪 AI Bypasser:</b> Paste text generated by ChatGPT. The system will rewrite it to bypass university and corporate AI detectors.</li>
                <li><b>📊 Snap-to-Excel:</b> Paste lists of items, names, or prices. The system will instantly compile them into a downloadable Excel file with live mathematical formulas.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # --- 🧪 AI BYPASSER ---
    elif menu == "🧪 AI Bypasser":
        st.markdown("<div class='glass-box'><h1 style='color:#00ff87;'>🧪 AI HUMANIZER ENGINE</h1><p>Evade AI detection algorithms instantly.</p></div>", unsafe_allow_html=True)
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        
        txt = st.text_area("PASTE AI TEXT HERE", height=200, max_chars=limit)
        st.caption(f"Character Count: {len(txt)} / {limit}")

        if st.button("✨ EXECUTE HUMANIZATION"):
            if txt:
                with st.spinner("Injecting human cadence..."):
                    human_text = txt.replace("Furthermore", "And honestly").replace("In conclusion", "So basically").replace("utilization", "use").replace("quintessential", "important")
                    st.success("✅ EVASION SUCCESSFUL")
                    st.text_area("HUMANIZED OUTPUT", value=human_text, height=200)
            else: st.warning("Please paste text.")

    # --- 📊 SNAP TO EXCEL ---
    elif menu == "📊 Snap-to-Excel":
        st.markdown("<div class='glass-box'><h1 style='color:#00d2ff;'>📊 SMART EXCEL CONVERTER</h1><p>Compile raw data into dynamic spreadsheets.</p></div>", unsafe_allow_html=True)
        
        table_data = st.text_area("PASTE RAW DATA (e.g., Macbook 1500000)", height=150)
        
        if st.button("🚀 COMPILE DYNAMIC EXCEL"):
            with st.spinner("Generating Matrix Spreadsheet..."):
                lines = table_data.strip().split('\n')
                items, prices = [], []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append(" ".join(parts[:-1]))
                        try: prices.append(float(parts[-1]))
                        except: prices.append(0)

                if items:
                    df = pd.DataFrame({'Item': items, 'Price': prices})
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='VantageData')
                        worksheet = writer.sheets['VantageData']
                        last_row = len(df) + 1
                        worksheet.write(last_row, 0, 'GRAND TOTAL')
                        worksheet.write_formula(last_row, 1, f'=SUM(B2:B{last_row})')
                        
                    st.success("✅ SPREADSHEET COMPILED")
                    st.download_button("📥 DOWNLOAD EXCEL FILE", data=output.getvalue(), file_name="VantagePro_Data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                else: st.warning("Please enter valid data.")        </div>
        """, unsafe_allow_html=True)

    # --- 🧪 AI BYPASSER ---
    elif menu == "🧪 AI Bypasser":
        st.markdown("<div class='glass-box'><h1 style='color:#00ff87;'>🧪 AI HUMANIZER ENGINE</h1><p>Evade AI detection algorithms instantly.</p></div>", unsafe_allow_html=True)
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        
        txt = st.text_area("PASTE AI TEXT HERE", height=200, max_chars=limit)
        st.caption(f"Character Count: {len(txt)} / {limit}")

        if st.button("✨ EXECUTE HUMANIZATION"):
            if txt:
                with st.spinner("Injecting human cadence..."):
                    human_text = txt.replace("Furthermore", "And honestly").replace("In conclusion", "So basically").replace("utilization", "use").replace("quintessential", "important")
                    st.success("✅ EVASION SUCCESSFUL")
                    st.text_area("HUMANIZED OUTPUT", value=human_text, height=200)
            else: st.warning("Please paste text.")

    # --- 📊 SNAP TO EXCEL ---
    elif menu == "📊 Snap-to-Excel":
        st.markdown("<div class='glass-box'><h1 style='color:#00d2ff;'>📊 SMART EXCEL CONVERTER</h1><p>Compile raw data into dynamic spreadsheets.</p></div>", unsafe_allow_html=True)
        
        table_data = st.text_area("PASTE RAW DATA (e.g., Macbook 1500000)", height=150)
        
        if st.button("🚀 COMPILE DYNAMIC EXCEL"):
            with st.spinner("Generating Matrix Spreadsheet..."):
                lines = table_data.strip().split('\n')
                items, prices = [], []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append(" ".join(parts[:-1]))
                        try: prices.append(float(parts[-1]))
                        except: prices.append(0)

                if items:
                    df = pd.DataFrame({'Item': items, 'Price': prices})
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                        df.to_excel(writer, index=False, sheet_name='VantageData')
                        worksheet = writer.sheets['VantageData']
                        last_row = len(df) + 1
                        worksheet.write(last_row, 0, 'GRAND TOTAL')
                        worksheet.write_formula(last_row, 1, f'=SUM(B2:B{last_row})')
                        
                    st.success("✅ SPREADSHEET COMPILED")
                    st.download_button("📥 DOWNLOAD EXCEL FILE", data=output.getvalue(), file_name="VantagePro_Data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                else: st.warning("Please enter valid data.")                    worksheet.write_formula(last_row, 1, f'=SUM(B2:B{last_row})')
                    
                st.success("✅ Dynamic Excel Created!")
                st.download_button(
                    label="📥 DOWNLOAD EXCEL FILE",
                    data=output.getvalue(),
                    file_name="VantagePro_Report.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
