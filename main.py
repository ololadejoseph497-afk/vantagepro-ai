import streamlit as st
import pandas as pd
from datetime import datetime
import io

# 1. Page Configuration
st.set_page_config(page_title="VantagePro AI Suite", page_icon="🐲", layout="wide")

# 2. YOUR LINKS
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. FUTURISTIC UI SYSTEM
def apply_sci_fi_style(video_url):
    st.markdown(f"""
        <style>
        #video-bg {{
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            z-index: -1;
            filter: brightness(35%);
        }}
        .stApp {{ background: transparent; }}
        .glass-card {{
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 210, 255, 0.3);
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.2);
            margin-bottom: 20px;
        }}
        [data-testid="stSidebar"] {{
            background-color: rgba(5, 10, 20, 0.95) !important;
            border-right: 1px solid #00d2ff;
        }}
        .stButton>button {{
            background: transparent;
            color: #00d2ff;
            border: 2px solid #00d2ff;
            border-radius: 10px;
            font-weight: bold;
            width: 100%;
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
    # MOVING BACKGROUND: Dragon/Sci-Fi Warp
    apply_sci_fi_style("https://assets.mixkit.co/videos/preview/mixkit-flying-through-a-blue-and-purple-cosmic-nebula-31514-large.mp4")
    
    st.title("VANTAGEPRO AI: CORE TERMINAL")
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("### SYSTEM AUTHENTICATION")
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
                else: st.error("ACCESS DENIED: INVALID KEY")
            except: st.error("CONNECTION ERROR: RETRYING...")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<a href="{PAYSTACK_LINK}" target="_blank" style="text-decoration:none;"><div style="background: linear-gradient(90deg, #ff00cc, #3333ff); color: white; padding: 20px; text-align: center; border-radius: 15px; font-size: 20px; font-weight: bold; box-shadow: 0 0 30px rgba(255, 0, 204, 0.5);">GET ACCESS KEY</div></a>', unsafe_allow_html=True)

# --- DASHBOARD AREA ---
else:
    # MOVING BACKGROUND: Tech Matrix
    apply_sci_fi_style("https://assets.mixkit.co/videos/preview/mixkit-animation-of-futuristic-devices-99786-large.mp4")
    
    st.sidebar.title("VANTAGEPRO")
    menu = st.sidebar.radio("NAVIGATION", ["CONTROL HUD", "AI BYPASSER", "EXCEL CORE"])
    
    if st.sidebar.button("EXIT SYSTEM"):
        st.session_state.authenticated = False
        st.rerun()

    if menu == "CONTROL HUD":
        st.markdown("<div class='glass-card'><h1 style='color:#00d2ff; text-align:center;'>CONTROL HUD</h1></div>", unsafe_allow_html=True)
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
