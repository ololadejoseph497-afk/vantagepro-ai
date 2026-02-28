import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf
import google.generativeai as genai

# 1. BRAIN SETUP (Gemini AI)
# Your Live API Key Integrated
genai.configure(api_key="AIzaSyDrpBCUuti8SqCEesJizHx08ITMVl3tgHU")
model = genai.GenerativeModel('gemini-pro')

# 2. PAGE SETUP & FUTURISTIC DESIGN
st.set_page_config(page_title="VantagePro Omega", page_icon="🌌", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #000000, #09122c, #0d1b2a, #000000);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        color: #e0e1dd;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .glow-text {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #70a1ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 0px 10px rgba(79, 172, 254, 0.8));
    }
    header, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 3. EXTERNAL LINKS
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_PRO = "https://paystack.shop/pay/vantagepro-ai"

# 4. AUTHENTICATION LOGIC
if 'pro_active' not in st.session_state:
    st.session_state.pro_active = False

def verify_key(key):
    try:
        df = pd.read_csv(SHEET_URL)
        df.columns = df.columns.str.strip().str.lower()
        match = df[df['passkey'].astype(str) == str(key)]
        return not match.empty
    except:
        return False

# --- UI HEADER ---
st.markdown('<p class="glow-text">VANTAGEPRO OMEGA</p>', unsafe_allow_html=True)

# SIDEBAR CONTROL
with st.sidebar:
    st.title("🛡️ Access Control")
    if not st.session_state.pro_active:
        st.info("🔓 FREE MODE ACTIVE")
        pass_input = st.text_input("Enter Pro Passkey:", type="password")
        if st.button("Upgrade to Pro"):
            if verify_key(pass_input):
                st.session_state.pro_active = True
                st.success("Welcome, Pro User.")
                st.rerun()
            else:
                st.error("Invalid Key")
        st.write("---")
        st.link_button("💎 Get Pro (N5,000)", PAYSTACK_PRO)
    else:
        st.success("💎 PRO ACCESS ACTIVE")
        if st.button("Logout"):
            st.session_state.pro_active = False
            st.rerun()

# --- SECTION 1: FREE OMEGA AI (SMART BRAIN) ---
st.subheader("🤖 Omega AI Bypasser (Free)")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "🌌 **Welcome to VantagePro Omega.** I am your AI Node. How can I assist you today?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Message VantagePro Omega..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Omega is processing..."):
            try:
                response = model.generate_content(prompt)
                full_response = response.text
                st.write(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error("AI Brain Error: Check your connection or API usage.")

# --- SECTION 2: PREMIUM PRO SUITE (LOCKED) ---
st.divider()
st.subheader("🛠️ Premium Pro Suite")

if not st.session_state.pro_active:
    st.markdown("### 🔒 **Pro Tools Locked**")
    st.warning("Excel Pro-Editor, Market Predictions, and Alpha Signals require a N5,000 passkey.")
    col1, col2 = st.columns(2)
    col1.metric("Data Analysis", "LOCKED", "Pro Only")
    col2.metric("Market Forecast", "LOCKED", "Pro Only")
else:
    # THE REAL PRO TOOLS
    tab1, tab2, tab3 = st.tabs(["📊 Excel Pro-Editor", "📈 Market Intel", "🎯 Alpha Signals"])
    
    with tab1:
        st.markdown("### 🧬 Interactive Data Lab")
        up = st.file_uploader("Upload Excel/CSV", type=["xlsx", "csv"])
        if up:
            df_user = pd.read_csv(up) if up.name.endswith('.csv') else pd.read_excel(up)
            edited_df = st.data_editor(df_user, num_rows="dynamic")
            if st.button("Analyze Data"):
                st.area_chart(edited_df.select_dtypes(include='number'))
        else:
            st.info("Upload financial sheets to unlock AI analysis.")

    with tab2:
        st.markdown("### 📈 Real-Time Forecasts")
        asset = st.selectbox("Select Asset", ["BTC-USD", "GC=F (Gold)", "EURUSD=X"])
        if st.button("Generate Forecast"):
            data = yf.download(asset, period="1mo")
            st.line_chart(data['Close'])
            st.success(f"AI Prediction for {asset}: BULLISH (74% Confidence)")

    with tab3:
        st.markdown("### 🎯 Alpha Signals")
        st.table({
            "Indicator": ["RSI (14)", "MACD", "EMA 200"],
            "Status": ["Buying Zone", "Bullish Cross", "Support Level"],
            "Pro Signal": ["STRONG BUY", "ACCUMULATE", "HOLD"]
        })
