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
    st.write("Answer the questions below to test your understanding of key scientific concepts!")
    
    score = 0
    total_questions = 10
    
    st.divider()

    # Question 1
    st.subheader("1. Biology / உயிரினவியல்")
    q1 = st.radio("What is the Tamil term for 'Photosynthesis'?", 
                  ("Select an option", "ஈர்ப்புவிசை", "ஒளிச்சேர்க்கை", "சுவாசம்", "முடுக்கம்"))
    if q1 == "ஒளிச்சேர்க்கை":
        score += 1

    st.divider()

    # Question 2
    st.subheader("2. Biology / உயிரினவியல்")
    q2 = st.radio("Which cell organelle is known as the powerhouse of the cell?", 
                  ("Select an option", "Nucleus", "Ribosome", "Mitochondria", "Cell Wall"))
    if q2 == "Mitochondria":
        score += 1

    st.divider()

    # Question 3
    st.subheader("3. Physics / இயற்பியல்")
    q3 = st.radio("'முடுக்கம்' (Mudukkam) corresponds to which English science term?", 
                  ("Select an option", "Velocity", "Force", "Acceleration", "Density"))
    if q3 == "Acceleration":
        score += 1

    st.divider()

    # Question 4
    st.subheader("4. Chemistry / வேதியியல்")
    q4 = st.radio("What is the basic building block of all matter in the universe?", 
                  ("Select an option", "Molecule", "Atom", "Compound", "Cell"))
    if q4 == "Atom":
        score += 1

    st.divider()

    # Question 5
    st.subheader("5. Environmental Science / சூழலியல்")
    q5 = st.radio("What is the Tamil translation for 'Biodiversity'?", 
                  ("Select an option", "பல்லுயிர்ப் பெருக்கம்", "வளிமண்டலம்", "சூழலியல்", "மட்கும் திறன்"))
    if q5 == "பல்லுயிர்ப் பெருக்கம்":
        score += 1

    st.divider()

    # Question 6
    st.subheader("6. Physics / இயற்பியல்")
    q6 = st.radio("The bending of light as it passes from one medium to another is called:", 
                  ("Select an option", "Reflection", "Refraction", "Conduction", "Absorption"))
    if q6 == "Refraction":
        score += 1

    st.divider()

    # Question 7
    st.subheader("7. Biology / உயிரினவியல்")
    q7 = st.radio("Which double-helix molecule carries genetic instructions in living organisms?", 
                  ("Select an option", "Glucose", "Enzyme", "DNA", "Hormone"))
    if q7 == "DNA":
        score += 1

    st.divider()

    # Question 8
    st.subheader("8. Chemistry / வேதியியல்")
    q8 = st.radio("Substances with a pH value below 7 are classified as:", 
                  ("Select an option", "Acids", "Bases", "Alloys", "Polymers"))
    if q8 == "Acids":
        score += 1

    st.divider()

    # Question 9
    st.subheader("9. Astronomy / வானியல்")
    q9 = st.radio("What is 'கருந்துளை' (Karundhulai) in English astronomy terms?", 
                  ("Select an option", "Asteroid", "Galaxy", "Black Hole", "Nebula"))
    if q9 == "Black Hole":
        score += 1

    st.divider()

    # Question 10
    st.subheader("10. Physics / இயற்பியல்")
    q10 = st.radio("What force opposes the relative motion between two sliding surfaces?", 
                   ("Select an option", "Gravity", "Friction", "Inertia", "Buoyancy"))
    if q10 == "Friction":
        score += 1

    st.divider()

    # Score Calculation & Feedback
    if st.button("🎯 Submit Answers & See Final Score"):
        st.balloons()
        st.metric(label="Your Final Quiz Score", value=f"{score} / {total_questions}")
        
        percentage = (score / total_questions) * 100
        if percentage >= 80:
            st.success(f"🌟 Outstanding job! You scored {percentage:.0f}%. You are a Science Master!")
        elif percentage >= 50:
            st.info(f"👍 Good effort! You scored {percentage:.0f}%. Explore the dictionary to improve your score!")
        else:
            st.warning(f"📚 You scored {percentage:.0f}%. Try checking the Dictionary section and try again!")
