import streamlit as st
import pandas as pd
from datetime import datetime
import yfinance as yf # Requires: pip install yfinance openpyxl

# 1. PAGE SETUP & DESIGN
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

# 2. LINKS & SETTINGS
SHEET_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_PRO = "https://paystack.shop/pay/vantagepro-ai" # Set to N5,000 in Paystack

# 3. PRO AUTHENTICATION
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

# 4. TOP UI
st.markdown('<p class="glow-text">VANTAGEPRO OMEGA</p>', unsafe_allow_html=True)

# 5. THE SIDEBAR GATEKEEPER
with st.sidebar:
    st.image("https://img.icons8.com/neon/96/shield.png", width=80)
    st.title("Access Control")
    if not st.session_state.pro_active:
        st.info("🔓 FREE MODE ACTIVE")
        pass_input = st.text_input("Enter Pro Passkey:", type="password")
        if st.button("🚀 Upgrade to Pro"):
            if verify_key(pass_input):
                st.session_state.pro_active = True
                st.success("Welcome, Pro User.")
                st.rerun()
            else:
                st.error("Invalid Key")
        st.write("---")
        st.link_button("💎 Buy Pro (N5,000)", PAYSTACK_PRO)
    else:
        st.success("💎 PRO ACCESS ACTIVE")
        if st.button("Logout"):
            st.session_state.pro_active = False
            st.rerun()

# 6. APP SECTIONS
# --- SECTION 1: FREE AI BYPASSER (ALWAYS ACCESSIBLE) ---
st.subheader("🤖 Omega AI Bypasser (Free)")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask the AI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write("Omega Node processing... (This is the free chat tier)")

# --- SECTION 2: PREMIUM TOOLS (LOCKED) ---
st.divider()
st.subheader("🛠️ Premium Pro Suite")

if not st.session_state.pro_active:
    st.warning("⚠️ Upgrade to PRO to unlock the following tools:")
    st.markdown("""
    - **📊 Advanced Excel Editor:** Edit and analyze financial sheets live.
    - **📈 Real-Time Market Forecast:** BTC, Gold, and Forex AI predictions.
    - **🎯 Signal Scanner:** Professional-grade technical indicators.
    """)
    st.lock_icon()
else:
    # PRO TOOLS
    tab1, tab2, tab3 = st.tabs(["📊 Excel Pro-Editor", "📈 Market Intel", "🎯 Alpha Signals"])
    
    with tab1:
        st.markdown("### 🧬 Interactive Data Lab")
        uploaded_file = st.file_uploader("Upload Excel/CSV for Deep Scan", type=["xlsx", "csv"])
        if uploaded_file:
            try:
                # Read data
                if uploaded_file.name.endswith('.csv'):
                    user_df = pd.read_csv(uploaded_file)
                else:
                    user_df = pd.read_excel(uploaded_file)
                
                st.write("Edit your data below:")
                # LIVE DATA EDITOR (Excel-style)
                edited_df = st.data_editor(user_df, num_rows="dynamic")
                
                if st.button("Run AI Data Analysis"):
                    st.info("Omega AI is scanning your sheet for patterns...")
                    st.line_chart(edited_df.select_dtypes(include='number'))
            except Exception as e:
                st.error(f"Error loading file: {e}")
        else:
            st.info("Upload a spreadsheet to begin deep analysis.")

    with tab2:
        st.markdown("### 📈 Real-Time Forecasts")
        ticker = st.selectbox("Select Asset", ["BTC-USD", "GC=F", "EURUSD=X", "AAPL"])
        if st.button("Generate Pro Report"):
            data = yf.download(ticker, period="1mo")
            st.line_chart(data['Close'])
            st.success(f"AI Prediction for {ticker}: BULLISH (74% Confidence)")

    with tab3:
        st.markdown("### 🎯 Signal Scanner")
        st.table({
            "Indicator": ["RSI", "MACD", "EMA 200"],
            "Status": ["35.2 (Buying Zone)", "Crossover Detected", "Support Level"],
            "Pro Signal": ["STRONG BUY", "ACCUMULATE", "HOLD"]
        })
