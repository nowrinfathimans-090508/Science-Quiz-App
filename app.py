import streamlit as st

# Page Configuration
st.set_page_config(page_title="Multilingual Science Explorer", page_icon="🌱", layout="centered")

st.title("🌱 Multilingual Science Explorer & Quiz")
st.write("Explore key science terms in English and Tamil, and test your knowledge for the science expo!")

# ==========================================
# 📖 DICTIONARY DATABASE (ADD MORE WORDS HERE!)
# ==========================================
SCIENCE_TERMS = {
    "Photosynthesis": {
        "tamil": "ஒளிச்சேர்க்கை (Olicherkai)",
        "definition": "The process by which plants use sunlight to synthesize foods from carbon dioxide and water.",
        "category": "Biology"
    },
    "Atom": {
        "tamil": "அணு (Anu)",
        "definition": "The basic building block of all matter in the universe.",
        "category": "Chemistry"
    },
    "Gravity": {
        "tamil": "ஈர்ப்புவிசை (Irppu Visai)",
        "definition": "The natural force that attracts any two objects with mass toward each other.",
        "category": "Physics"
    },
    "Cell": {
        "tamil": "செல் / உயிரணு (Cell)",
        "definition": "The smallest structural and functional unit of all living organisms.",
        "category": "Biology"
    },
    "Mitochondria": {
        "tamil": "மைட்டோகாண்ட்ரியா (Mitochondria)",
        "definition": "Known as the powerhouse of the cell, generating chemical energy needed for biochemical reactions.",
        "category": "Biology"
    },
    "Ecosystem": {
        "tamil": "சூழலியல் (Sujaliyal)",
        "definition": "A community of living organisms interacting with each other and their physical environment.",
        "category": "Environmental Science"
    },
    "Velocity": {
        "tamil": "திசைவேகம் (Disai Vegam)",
        "definition": "The speed of an object in a specific direction.",
        "category": "Physics"
    },
    "Molecule": {
        "tamil": "மூலக்கூறு (Moolakooru)",
        "definition": "A group of two or more atoms held together by chemical bonds.",
        "category": "Chemistry"
    },
    "Respiration": {
        "tamil": "சுவாசம் (Svasam)",
        "definition": "The action of breathing; the process in living organisms involving the production of energy.",
        "category": "Biology"
    },
    "Refraction": {
        "tamil": "ஒளி விலகல் (Oli Vilagal)",
        "definition": "The bending of a wave as it passes from one medium to another.",
        "category": "Physics"
    }
}

# Sidebar Navigation
menu = st.sidebar.selectbox("Choose a Section", ["Dictionary Explorer", "Interactive Quiz"])

# ==========================================
# SECTION 1: DICTIONARY EXPLORER
# ==========================================
if menu == "Dictionary Explorer":
    st.header("📖 Bilingual Science Dictionary")
    st.write("Search or select a science term to view its Tamil translation and definition:")
    
    # Search / Selectbox dropdown of all terms
    search_term = st.selectbox("Choose a term:", list(SCIENCE_TERMS.keys()))
    
    if search_term:
        details = SCIENCE_TERMS[search_term]
        st.info(f"**English Term:** {search_term}")
        st.success(f"**Tamil Translation:** {details['tamil']}")
        st.write(f"**Category:** {details['category']}")
        st.write(f"**Definition:** {details['definition']}")

# ==========================================
# SECTION 2: INTERACTIVE QUIZ
# ==========================================
elif menu == "Interactive Quiz":
    st.header("🧠 Science Knowledge Quiz")
    st.write("Test what you've learned!")
    
    score = 0
    
    # Question 1
    q1 = st.radio("1. What is known as the powerhouse of the cell?", ("Nucleus", "Mitochondria", "Ribosome", "Atom"))
    if q1 == "Mitochondria":
        st.success("Correct! Great job!")
    elif q1:
        st.error("Incorrect. Try another option!")

    # Question 2
    q2 = st.radio("2. What is 'Photosynthesis' in Tamil?", ("ஈர்ப்புவிசை", "ஒளிச்சேர்க்கை", "சுவாசம்", "மூலக்கூறு"))
    if q2 == "ஒளிச்சேர்க்கை":
        st.success("Correct! Well done!")
    elif q2:
        st.error("Incorrect. Try another option!")
