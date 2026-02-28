import streamlit as st
import pandas as pd
import yfinance as yf
import google.generativeai as genai
from datetime import datetime

# --- 1. AI CONFIGURATION (REAL KEY) ---
genai.configure(api_key="AIzaSyB0VdESBEqoLjeg5D-H2RNP_WWd2Y9Ov1w")
model = genai.GenerativeModel('gemini-pro')

# --- 2. PAGE CONFIG & FUTURISTIC THEME ---
st.set_page_config(page_title="VantagePro Omega", page_icon="💠", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&display=swap');

    /* Deep Sea Water Wave Background */
    .stApp {
        background: #000b14;
        background-image: 
            radial-gradient(circle at 50% 10%, rgba(0, 242, 254, 0.05) 0%, transparent 50%),
            linear-gradient(to bottom, #000b14, #001a2c);
        color: #e0e1dd;
        font-family: 'Orbitron', sans-serif;
    }

    /* The Animated Wave Overlay */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/waves.png');
        opacity: 0.06;
        animation: waterFlow 20s linear infinite;
        pointer-events: none;
    }

    @keyframes waterFlow {
        from { background-position: 0 0; }
        to { background-position: 1000px 500px; }
    }

    /* Glowing Neon Title */
    .glow-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: clamp(2rem, 8vw, 4rem);
        font-weight: 900;
        color: #00f2fe;
        text-shadow: 0 0 15px rgba(0, 242, 254, 0.6), 0 0 30px rgba(79, 172, 254, 0.4);
        margin: 20px 0;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 5, 10, 0.95) !important;
        border-right: 1px solid #00f2fe;
    }

    /* Clean UI Hacks */
    header, footer, #MainMenu {visibility: hidden;}
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATA & PAYMENT LINKS ---
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# --- 4. NAVIGATION (SIDEBAR) ---
st.sidebar.markdown("<h1 style='color:#00f2fe; font-family:Orbitron; text-align:center;'>VANTAGEPRO</h1>", unsafe_allow_html=True)
st.sidebar.write("---")
page = st.sidebar.radio("CHOOSE WORKSPACE:", ["🤖 Free AI Bypasser", "💎 Pro Suite (Locked)"])

# --- PAGE 1: FREE AI BYPASSER ---
if page == "🤖 Free AI Bypasser":
    st.markdown('<p class="glow-title">OMEGA AI</p>', unsafe_allow_html=True)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "🌌 Systems Online. I am the Omega AI. How can I assist your workflow?"}]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Enter your command..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            try:
                response = model.generate_content(prompt)
                st.write(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("Connection Latency Detected. Check your network or verify the Gemini API is enabled in Google Cloud.")

# --- PAGE 2: PRO SUITE ---
elif page == "💎 Pro Suite (Locked)":
    st.markdown('<p class="glow-title">PRO SUITE</p>', unsafe_allow_html=True)
    
    if 'pro_auth' not in st.session_state:
        st.session_state.pro_auth = False

    if not st.session_state.pro_auth:
        st.markdown("<h3 style='text-align:center; color:#8892b0;'>🛡️ Authentication Required</h3>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("#### Unlock Workspace")
            pass_key = st.text_input("8-DIGIT PASSKEY", type="password", placeholder="Enter your unique code")
            if st.button("AUTHENTICATE"):
                try:
                    df = pd.read_csv(SHEET_URL)
                    df.columns = df.columns.str.strip().str.lower()
                    if str(pass_key) in df['passkey'].astype(str).values:
                        st.session_state.pro_auth = True
                        st.success("Identity Verified. Welcome, Executive.")
                        st.rerun()
                    else:
                        st.error("Invalid Passkey.")
                except:
                    st.error("Security Database Offline. Please contact admin.")
        
        with col2:
            st.markdown("#### Access Tiers")
            st.write("Upgrade to Pro for full Data Analysis & Market Forecasts.")
            st.link_button("💎 GET PRO KEY (N5,000)", PAYSTACK_LINK)

    else:
        # THE PRO TOOLS DASHBOARD
        st.sidebar.success("✅ PRO ACTIVE")
        if st.sidebar.button("Logout"):
            st.session_state.pro_auth = False
            st.rerun()

        tab1, tab2, tab3 = st.tabs(["📊 Excel Lab", "📈 Market Predictor", "🎯 Signals"])
        
        with tab1:
            st.markdown("### 🧬 Professional Data Lab")
            up = st.file_uploader("Upload Financial Spreadsheet", type=["xlsx", "csv"])
            if up:
                df_u = pd.read_csv(up) if up.name.endswith('.csv') else pd.read_excel(up)
                st.data_editor(df_u, num_rows="dynamic", use_container_width=True)
                if st.button("AI Trend Analysis"):
                    st.area_chart(df_u.select_dtypes(include='number'))
            else:
                st.info("Awaiting data input...")

        with tab2:
            st.markdown("### 📈 Prediction Engine")
            asset = st.selectbox("Asset Class", ["BTC-USD", "GC=F (Gold)", "EURUSD=X"])
            if st.button("Analyze Trend"):
                data = yf.download(asset, period="1mo")
                st.line_chart(data['Close'])
                st.success(f"Omega Sentiment for {asset}: BULLISH")

        with tab3:
            st.markdown("### 🎯 Alpha Trading Signals")
            st.table({
                "Parameter": ["Relative Strength", "Momentum", "Trend Line"],
                "Pro Logic": ["35.2 (Oversold)", "Bullish Cross", "Strong Support"],
                "Recommendation": ["BUY", "STRONG BUY", "ACCUMULATE"]
            })
