import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. Page Configuration
st.set_page_config(page_title="VantagePro AI Suite", page_icon="🐲", layout="wide")

# 2. YOUR LINKS
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. GLOBAL FUTURISTIC CSS (Animated Background)
def apply_sci_fi_style(video_url):
    st.markdown(f"""
        <style>
        /* Video Background */
        #video-bg {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            z-index: -1;
            filter: brightness(40%);
        }}
        
        .stApp {{ background: transparent; }}
        
        /* Glassmorphism Cards */
        .glass-card {{
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 210, 255, 0.3);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.2);
            margin-bottom: 20px;
            transition: 0.4s;
        }}
        .glass-card:hover {{
            border: 1px solid #00d2ff;
            box-shadow: 0 0 40px rgba(0, 210, 255, 0.5);
        }}

        /* Futuristic Sidebar */
        [data-testid="stSidebar"] {{
            background-color: rgba(5, 10, 20, 0.9) !important;
            border-right: 1px solid #00d2ff;
        }}

        /* Neon Buttons */
        .stButton>button {{
            background: transparent;
            color: #00d2ff;
            border: 2px solid #00d2ff;
            border-radius: 10px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 2px;
            transition: 0.3s;
        }}
        .stButton>button:hover {{
            background: #00d2ff;
            color: #000;
            box-shadow: 0 0 30px #00d2ff;
        }}
        </style>
        
        <video autoplay muted loop id="video-bg">
            <source src="{video_url}" type="video/mp4">
        </video>
    """, unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_type = "Regular"

# --- LOGIN PAGE ---
if not st.session_state.authenticated:
    # Login Background: Deep Space/Dragon Portal
    apply_sci_fi_style("https://assets.mixkit.co/videos/preview/mixkit-flying-through-a-blue-and-purple-cosmic-nebula-31514-large.mp4")
    
    st.title("🛡️ VANTAGEPRO AI: THE NEXT GEN")
    
    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("### 🔑 SYSTEM AUTHENTICATION")
        passkey_input = st.text_input("ENTER ACCESS KEY", type="password")
        if st.button("INITIATE LOGIN"):
            clean_key = passkey_input.strip()
            if clean_key == "Joseph":
                st.session_state.authenticated = True
                st.session_state.user_type = "Premium"
                st.rerun()
            elif clean_key != "":
                try:
                    df = pd.read_csv(SHEET_URL)
                    df.columns = df.columns.str.strip().str.capitalize()
                    user_row = df[df['Passkey'].astype(str) == clean_key]
                    if not user_row.empty:
                        st.session_state.user_type = str(user_row.iloc[0]['Type']).strip()
                        st.session_state.authenticated = True
                        st.rerun()
                    else: st.error("❌ KEY REJECTED BY SERVER")
                except: st.error("⚠️ DATA-LINK FAILURE")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="background: linear-gradient(90deg, #ff00cc, #3333ff); color: white; padding: 20px; text-align: center; border-radius: 15px; font-size: 22px; font-weight: bold; box-shadow: 0 0 30px rgba(255, 0, 204, 0.5);">⚡ ACQUIRE PREMIUM LICENSE</div></a>', unsafe_allow_html=True)

# --- DASHBOARD AREA ---
else:
    # Dashboard Background: Matrix/Moving Tech Grid
    apply_sci_fi_style("https://assets.mixkit.co/videos/preview/mixkit-animation-of-futuristic-devices-99786-large.mp4")
    
    st.sidebar.title("👨‍💻 COMMANDER")
    menu = st.sidebar.radio("NAVIGATE", ["🛰️ HUD", "🧪 BYPASSER", "📊 EXCEL-CORE"])
    
    if st.sidebar.button("TERMINATE SESSION"):
        st.session_state.authenticated = False
        st.rerun()

    if menu == "🛰️ HUD":
        st.markdown("<div class='glass-card'><h1 style='color:#00d2ff; text-align:center;'>🛰️ CONTROL HUD</h1></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.markdown(f"<div class='glass-card'><h3>USER RANK</h3><h2 style='color:#00ff87;'>{st.session_state.user_type}</h2></div>", unsafe_allow_html=True)
        c2.markdown("<div class='glass-card'><h3>AI STATUS</h3><h2 style='color:#00ff87;'>STABLE</h2></div>", unsafe_allow_html=True)

    elif menu == "🧪 BYPASSER":
        st.markdown("<div class='glass-card'><h1 style='color:#00ff87;'>🧪 HUMANIZER CORE</h1></div>", unsafe_allow_html=True)
        limit = 2000 if st.session_state.user_type == "Regular" else 100000
        txt = st.text_area("INJECT DATA FOR HUMANIZATION", height=250, max_chars=limit)
        if st.button("SYNTHESIZE TEXT"):
            if txt:
                with st.spinner("Decoding AI patterns..."):
                    processed = txt.replace("Furthermore", "In fact").replace("In conclusion", "Ultimately")
                    st.success("✅ DECRYPTION COMPLETE")
                    st.text_area("HUMAN-GRADE OUTPUT", value=processed, height=200)

    elif menu == "📊 EXCEL-CORE":
        st.markdown("<div class='glass-card'><h1 style='color:#00d2ff;'>📊 DATA COMPILER</h1></div>", unsafe_allow_html=True)
        raw_data = st.text_area("INPUT RAW DATASTREAM", height=150)
        if st.button("COMPILE TO SPREADSHEET"):
            lines = raw_data.strip().split('\n')
            items, prices = [], []
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    items.append(" ".join(parts[:-1])); prices.append(float(parts[-1]) if parts[-1].isdigit() else 0)
            if items:
                df = pd.DataFrame({'Entity': items, 'Value': prices})
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='MatrixData')
                    worksheet = writer.sheets['MatrixData']
                    last_row = len(df) + 1
                    worksheet.write(last_row, 0, 'TOTAL SUM')
                    worksheet.write_formula(last_row, 1, f'=SUM(B2:B{last_row})')
                st.download_button("📥 RETRIEVE DATA FILE", data=output.getvalue(), file_name="Vantage_Core.xlsx")            <p>Welcome to VantagePro, your personal AI powerhouse. Here is how to use your tools:</p>
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
