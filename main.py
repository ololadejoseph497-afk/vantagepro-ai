import streamlit as st
import pandas as pd
from datetime import datetime

# 1. PAGE CONFIG & THEME
st.set_page_config(page_title="VantagePro Omega", page_icon="🌌", layout="centered")

# --- ADVANCED CSS FOR MOVING 3D GRADIENT & GLOW ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #050a30, #000c66, #000000, #050a30);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .glow-title {
        font-size: 45px;
        font-weight: bold;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 10px #00d4ff, 0 0 20px #00d4ff, 0 0 30px #00d4ff;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 5px;
    }
    /* Simple hide of Streamlit elements */
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 2. YOUR DATABASE & LINKS
# I have plugged your specific links in here:
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/1TIf1Z7R-bLeavsHfC6GLoszM42N1iblpVL6s-ZLaFUU/export?format=csv"
PAYSTACK_LINK = "https://paystack.shop/pay/vantagepro-ai"

# 3. PASSKEY SECURITY CHECK
def verify_access(entered_key):
    try:
        # Pulling live data from your Google Sheet
        df = pd.read_csv(SHEET_CSV_URL)
        df.columns = df.columns.str.strip().str.lower()
        
        # Check if key exists
        match = df[df['passkey'].astype(str) == str(entered_key)]
        
        if not match.empty:
            expiry_str = str(match.iloc[0]['date'])
            expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
            if expiry_date >= datetime.now().date():
                return True, expiry_date
            return False, "Key Expired"
        return False, "Invalid Key"
    except Exception:
        return False, "Database Connection Error"

# 4. SESSION STATE (Keeping user logged in)
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- UI LOGIC ---
st.markdown('<p class="glow-title">VANTAGEPRO OMEGA</p>', unsafe_allow_html=True)

if not st.session_state.auth:
    # --- LOCKED SCREEN ---
    st.write("---")
    st.info("🔐 Restricted Access. Please authenticate with your 8-digit passkey.")
    
    # Typing area for the key
    user_input = st.text_input("ENTER PASSKEY", type="password", help="Sent to your email after payment")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 UNLOCK OMEGA"):
            valid, result = verify_access(user_input)
            if valid:
                st.session_state.auth = True
                st.success(f"Access Granted. Valid until {result}")
                st.rerun()
            else:
                st.error(result)
                
    with col2:
        # LINKED DIRECTLY TO YOUR PAYSTACK
        st.link_button("💳 BUY PASSKEY (N1,000)", PAYSTACK_LINK, use_container_width=True)
    
    st.write("---")
    st.caption("Don't have a key? Click 'Buy Passkey' and check your email instantly.")

else:
    # --- UNLOCKED WORKSPACE ---
    st.markdown("### ⚡ System Status: **ACTIVE**")
    
    # ➕ THE PLUS (+) MENU FOR UPLOADS
    with st.popover("➕ Advanced Tools"):
        st.markdown("**Multimedia Inputs**")
        st.file_uploader("Upload Data/Images", type=['png', 'jpg', 'pdf', 'csv'])
        st.camera_input("Scanner Active")
        st.info("Pro Tip: Use the scanner for physical trading charts.")

    # CHAT INTERFACE (The only thing outside the menu)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if user_prompt := st.chat_input("Command VantagePro Omega..."):
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.write(user_prompt)

        with st.chat_message("assistant"):
            st.write("Omega Brain is processing...")
            # Here is where we will later add the GPT brain connection
    
    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
