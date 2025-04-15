import streamlit as st
import re

# Page config
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Custom CSS styling with gradient background and animation
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

        html, body, .stApp {
            height: 100%;
            background: linear-gradient(145deg, #00000c, #e0c3fc);
            background-attachment: fixed;
            font-family: 'Quicksand', sans-serif;
        }

        h1 {
            font-family: 'Pacifico', cursive;
            color: #ff66a3;
            text-align: center;
            font-size: 3em;
            text-shadow: 0 0 10px #fff, 0 0 20px #ff69b4;
            margin-bottom: 10px;
        }

        .stTextInput > div > div > input {
            border: 2px solid #ffb6c1;
            border-radius: 10px;
            padding: 10px;
            background-color: fff0f5;
        }

        .stButton > button {
            background-color: #ff66a3;
            color: white;
            font-weight: bold;
            padding: 10px 24px;
            border-radius: 30px;
            border: none;
            box-shadow: 0 4px 10px rgba(255, 105, 180, 0.5);
            transition: all 0.3s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #ff3385;
            transform: scale(1.05);
        }

        .emoji-animate {
            animation: bounce 1.2s infinite;
            display: inline-block;
        }

        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-8px);
            }
        }

        .feedback {
            padding: 10px;
            border-radius: 10px;
            margin-top: 10px;
            font-weight: bold;
            text-align: center;
        }

        .strong {
            background-color: #d4edda;
            color: #155724;
        }

        .medium {
            background-color: #fff3cd;
            color: #856404;
        }

        .weak {
            background-color: #f8d7da;
            color: #721c24;
        }

        .suggestion {
            padding: 6px 12px;
            margin-bottom: 5px;
            background-color: #ffe4ec;
            border-left: 5px solid #ff69b4;
            border-radius: 5px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Title with emoji
st.markdown("<h1><span class='emoji-animate'>🔐</span> Password Strength Checker</h1>", unsafe_allow_html=True)

# Description
st.markdown("""
<div style='text-align: center; font-size:18px;'>
    Welcome to the <b>ultimate password strength checker</b>! <span class='emoji-animate'>👑</span><br>
    Use this cute and helpful tool to check how strong your password is.<br>
    We’ll give you <b>tips</b> to improve it if needed. 💡💪
</div>
""", unsafe_allow_html=True)

# Password input
password = st.text_input("Enter your password", type="password")

# Logic
feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Include both UPPER and lower case letters.")
    
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")
    
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$%&*).")

    # Strength message
    if score == 4:
        st.markdown('<div class="feedback strong">✅ Your password is <b>Strong</b>! 🎉✨</div>', unsafe_allow_html=True)
    elif score == 3:
        st.markdown('<div class="feedback medium">🟡 Medium Strength. You can still improve it!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="feedback weak">🔴 Weak Password. Try improving it.</div>', unsafe_allow_html=True)

    # Show suggestions
    if feedback:
        st.markdown("### 🔧 Improvement Suggestions")
        for tip in feedback:
            st.markdown(f"<div class='suggestion'>{tip}</div>", unsafe_allow_html=True)
else:
    st.info("Please enter your password to get started 📝")
