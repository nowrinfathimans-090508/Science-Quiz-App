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
# SECTION 1: DICTIONARY EXPLORER
# ==========================================
if menu == "📖 Dictionary Explorer":
    st.header("📖 Science Terms Dictionary")
    
    if not terms_data:
        st.error("dictionary.json file not found. Please make sure dictionary.json is committed to your repository.")
    else:
        # Get list of categories
        categories = ["All"] + sorted(list(set(item["category"] for item in terms_data)))
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            selected_category = st.selectbox("Filter by Category:", categories)
        
        # Filter terms by category
        if selected_category != "All":
            filtered_terms = [t for t in terms_data if t["category"] == selected_category]
        else:
            filtered_terms = terms_data
            
        term_names = [t["term"] for t in filtered_terms]
        
        with col2:
            search_selection = st.selectbox("Type or select a term to inspect:", term_names)
            
        # Display selected term
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
    st.write("Test your knowledge of scientific terms and their Tamil translations!")
    
    score = 0
    
    q1 = st.radio("1. What is the Tamil term for 'Photosynthesis'?", 
                  ("ஒளிச்சேர்க்கை", "ஈர்ப்புவிசை", "சுவாசம்", "முடுக்கம்"))
    if q1 == "ஒளிச்சேர்க்கை":
        st.success("Correct!")
        score += 1

    q2 = st.radio("2. Which term describes the smallest structural unit of living organisms?", 
                  ("Atom", "Cell", "Molecule", "Tissue"))
    if q2 == "Cell":
        st.success("Correct!")
        score += 1

    q3 = st.radio("3. 'முடுக்கம்' (Mudukkam) corresponds to which English science term?", 
                  ("Velocity", "Force", "Acceleration", "Density"))
    if q3 == "Acceleration":
        st.success("Correct!")
        score += 1
        
    st.divider()
    st.metric(label="Your Total Score", value=f"{score} / 3")
