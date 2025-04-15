import streamlit as st

# Injecting custom CSS for a girly, aesthetic design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
        background: linear-gradient(to right, #fdfbfb, #ebedee);
        color: #4B4453;
    }

    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        padding: 0.5em 1em;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #FF69B4;
        transform: scale(1.05);
    }

    .stSelectbox, .stNumberInput, .stTextInput {
        background-color: white;
        border-radius: 10px;
        padding: 8px;
    }

    .stMarkdown h1, .stMarkdown h3 {
        color: #FF69B4;
        text-align: center;
    }

    .stSuccess {
        background-color: #ffe0ec;
        color: #c2185b;
        border-radius: 10px;
        padding: 10px;
        font-weight: bold;
    }

    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 120px;
        border-radius: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Cute Logo/Image at the Top (You can replace the URL with your own image)
st.markdown(
    '<img src="https://cdn-icons-png.flaticon.com/512/2947/2947975.png" alt="cute globe" width="100">',
    unsafe_allow_html=True
)

# App Title and Intro
st.title("🌎 Unit Converter App")
st.markdown("### Converts Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time 💫")

# Category Selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Conversion Logic
def convert_units(category, value, unit):
    if category == "Length": 
        if unit == "Kilometer to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometer":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

    return 0

# Unit Selection Based on Category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Miles to Kilometer", "Kilometer to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("🕒 Select Conversion", [
        "Seconds to minutes", "Minutes to seconds",
        "Minutes to hours", "Hours to minutes",
        "Hours to days", "Days to hours"
    ])

# Input and Button
value = st.number_input("Enter the value to convert", min_value=0.0)

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
