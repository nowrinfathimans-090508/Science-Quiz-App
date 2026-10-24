import streamlit as st
import json

# Page Config
st.set_page_config(page_title="Multilingual Science Explorer", page_icon="🌱", layout="wide")

# Function to load dictionary from JSON file
@st.cache_data
def load_dictionary():
    try:
        with open("dictionary.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

terms_data = load_dictionary()

st.title("🌱 Multilingual Science Explorer & Quiz")
st.write(f"Explore **{len(terms_data)}** essential scientific terms translated into Tamil with detailed definitions.")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["📖 Dictionary Explorer", "🧠 Interactive Quiz"])

# ==========================================
# 📱 QR CODE DISPLAY IN SIDEBAR
# ==========================================
st.sidebar.divider()
st.sidebar.subheader("📱 Scan to Open on Phone")

# 💡 PASTE your copied QR code image link inside the quotes below:
qr_image_url = "PASTE_YOUR_COPIED_IMAGE_LINK_HERE"

if qr_image_url != "PASTE_YOUR_COPIED_IMAGE_LINK_HERE":
    st.sidebar.image(qr_image_url, width=180, caption="Scan for Mobile Expo View")
else:
    st.sidebar.info("Paste your QR image link in app.py to display it here!")


# ==========================================
# SECTION 1: DICTIONARY EXPLORER
# ==========================================
if menu == "📖 Dictionary Explorer":
    st.header("📖 Science Terms Dictionary")
    
    if not terms_data:
        st.error("dictionary.json file not found. Please make sure dictionary.json is committed to your repository.")
    else:
        categories = ["All"] + sorted(list(set(item["category"] for item in terms_data)))
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            selected_category = st.selectbox("Filter by Category:", categories)
        
        if selected_category != "All":
            filtered_terms = [t for t in terms_data if t["category"] == selected_category]
        else:
            filtered_terms = terms_data
            
        term_names = [t["term"] for t in filtered_terms]
        
        with col2:
            search_selection = st.selectbox("Type or select a term to inspect:", term_names)
            
        selected_data = next((item for item in filtered_terms if item["term"] == search_selection), None)
        
        if selected_data:
            st.divider()
            st.subheader(f"🔍 {selected_data['term']}")
            
            c1, c2 = st.columns(2)
            with c1:
                st.info(f"**Tamil Translation:**\n### {selected_data['tamil']}")
            with c2:
                st.warning(f"**Category:** {selected_data['category']}")
                
            st.write(f"**Scientific Definition:** {selected_data['definition']}")

# ==========================================
# SECTION 2: INTERACTIVE QUIZ
# ==========================================
elif menu == "🧠 Interactive Quiz":
    st.header("🧠 Science Expo Knowledge Quiz")
    st.write("Answer the questions below to test your understanding of key scientific concepts!")
    
    score = 0
    total_questions = 3
    
    st.divider()

    q1 = st.radio("1. What is the Tamil term for 'Photosynthesis'?", 
                  ("Select an option", "ஈர்ப்புவிசை", "ஒளிச்சேர்க்கை", "சுவாசம்"))
    if q1 == "ஒளிச்சேர்க்கை":
        score += 1

    st.divider()

    q2 = st.radio("2. Which cell organelle is known as the powerhouse of the cell?", 
                  ("Select an option", "Nucleus", "Ribosome", "Mitochondria"))
    if q2 == "Mitochondria":
        score += 1

    st.divider()

    q3 = st.radio("3. 'முடுக்கம்' (Mudukkam) corresponds to which English science term?", 
                  ("Select an option", "Velocity", "Force", "Acceleration"))
    if q3 == "Acceleration":
        score += 1

    st.divider()

    if st.button("🎯 Submit Answers & See Final Score"):
        st.balloons()
        st.metric(label="Your Final Quiz Score", value=f"{score} / {total_questions}")
