import streamlit as st
import json

# Page Config
st.set_page_config(page_title="Science Explorer & Quiz", page_icon="🌱", layout="wide")

# Function to load dictionary from JSON file
@st.cache_data
def load_dictionary():
    try:
        with open("dictionary.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

terms_data = load_dictionary()

# App Title Update
st.title("🌱 Science Explorer & Quiz")
st.write(f"Explore **{len(terms_data)}** essential scientific terms translated into Tamil with detailed definitions.")

# Sidebar Navigation
menu = st.sidebar.radio("Navigation", ["📖 Dictionary Explorer", "🧠 Interactive Quiz"])

# ==========================================
# 📱 QR CODE DISPLAY IN SIDEBAR
# ==========================================
st.sidebar.divider()
st.sidebar.subheader("📱 Scan to Open on Phone")

# Your Postimages direct link
qr_image_url = "PASTE_YOUR_POSTIMAGES_LINK_HERE"

if qr_image_url != "PASTE_YOUR_POSTIMAGES_LINK_HERE":
    st.sidebar.image(qr_image_url, width=180, caption="Scan for Mobile Expo View")
else:
    st.sidebar.info("QR Code active.")


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
# SECTION 2: INTERACTIVE QUIZ (50+ Questions Bank)
# ==========================================
elif menu == "🧠 Interactive Quiz":
    st.header("🧠 Science Expo Knowledge Quiz")
    st.write("Test your understanding across our entire scientific database! Answer the questions below:")
    
    # Complete 50-Question Bank
    quiz_bank = [
        {"question": "1. What is the Tamil term for 'Photosynthesis'?", "options": ["ஈர்ப்புவிசை", "ஒளிச்சேர்க்கை", "சுவாசம்"], "answer": "ஒளிச்சேர்க்கை"},
        {"question": "2. Which cell organelle is known as the powerhouse of the cell?", "options": ["Nucleus", "Ribosome", "Mitochondria"], "answer": "Mitochondria"},
        {"question": "3. 'முடுக்கம்' (Mudukkam) corresponds to which English science term?", "options": ["Velocity", "Force", "Acceleration"], "answer": "Acceleration"},
        {"question": "4. What is the chemical symbol for Water?", "options": ["H2O", "CO2", "O2"], "answer": "H2O"},
        {"question": "5. What planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter"], "answer": "Mars"},
        {"question": "6. What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
        {"question": "7. What is the powerhouse of the plant cell?", "options": ["Chloroplast", "Nucleus", "Vacuole"], "answer": "Chloroplast"},
        {"question": "8. What is the center of an atom called?", "options": ["Electron", "Nucleus", "Proton"], "answer": "Nucleus"},
        {"question": "9. What force pulls objects toward the Earth?", "options": ["Magnetism", "Friction", "Gravity"], "answer": "Gravity"},
        {"question": "10. What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond"], "answer": "Diamond"},
        {"question": "11. What is the speed of light in a vacuum approximately?", "options": ["300,000 km/s", "150,000 km/s", "3,000 km/s"], "answer": "300,000 km/s"},
        {"question": "12. Which blood cells fight infections in the human body?", "options": ["Red Blood Cells", "White Blood Cells", "Platelets"], "answer": "White Blood Cells"},
        {"question": "13. What is the chemical symbol for Gold?", "options": ["Ag", "Au", "Gd"], "answer": "Au"},
        {"question": "14. How many bones are in an adult human body?", "options": ["206", "196", "215"], "answer": "206"},
        {"question": "15. What is the main gas found in the air we breathe?", "options": ["Oxygen", "Nitrogen", "Carbon Dioxide"], "answer": "Nitrogen"},
        {"question": "16. What unit is used to measure electrical resistance?", "options": ["Volt", "Ampere", "Ohm"], "answer": "Ohm"},
        {"question": "17. What type of energy does a moving car possess?", "options": ["Potential Energy", "Kinetic Energy", "Thermal Energy"], "answer": "Kinetic Energy"},
        {"question": "18. Which vitamin is produced when a person is exposed to sunlight?", "options": ["Vitamin A", "Vitamin C", "Vitamin D"], "answer": "Vitamin D"},
        {"question": "19. What is the boiling point of water in Celsius?", "options": ["90°C", "100°C", "110°C"], "answer": "100°C"},
        {"question": "20. What is the largest organ in the human body?", "options": ["Liver", "Skin", "Brain"], "answer": "Skin"},
        {"question": "21. Which instrument is used to measure earthquakes?", "options": ["Barometer", "Seismograph", "Thermometer"], "answer": "Seismograph"},
        {"question": "22. What is the chemical formula for table salt?", "options": ["NaCl", "KCl", "HCl"], "answer": "NaCl"},
        {"question": "23. Which planet has the most moons in our solar system?", "options": ["Saturn", "Jupiter", "Mars"], "answer": "Saturn"},
        {"question": "24. What is the process of liquid turning into gas called?", "options": ["Condensation", "Evaporation", "Freezing"], "answer": "Evaporation"},
        {"question": "25. Which gas is most abundant in the Sun?", "options": ["Hydrogen", "Helium", "Oxygen"], "answer": "Hydrogen"},
        {"question": "26. What part of the plant conducts water from roots to leaves?", "options": ["Xylem", "Phloem", "Cortex"], "answer": "Xylem"},
        {"question": "27. What is the pH value of pure water?", "options": ["5", "7", "9"], "answer": "7"},
        {"question": "28. Which animal is known as the 'Ship of the Desert'?", "options": ["Horse", "Camel", "Elephant"], "answer": "Camel"},
        {"question": "29. What is the primary source of energy for the Earth?", "options": ["The Moon", "The Sun", "Geothermal Core"], "answer": "The Sun"},
        {"question": "30. What subatomic particle carries a negative charge?", "options": ["Proton", "Neutron", "Electron"], "answer": "Electron"},
        {"question": "31. Which metal is liquid at room temperature?", "options": ["Iron", "Mercury", "Copper"], "answer": "Mercury"},
        {"question": "32. What is the study of heredity called?", "options": ["Genetics", "Ecology", "Botany"], "answer": "Genetics"},
        {"question": "33. What galaxy is Earth located in?", "options": ["Andromeda", "Milky Way", "Sombrero"], "answer": "Milky Way"},
        {"question": "34. What is the universal blood donor type?", "options": ["A positive", "AB positive", "O negative"], "answer": "O negative"},
        {"question": "35. Which organ purifies blood in the human body?", "options": ["Heart", "Kidney", "Lungs"], "answer": "Kidney"},
        {"question": "36. What is the chemical symbol for Iron?", "options": ["Fe", "Ir", "In"], "answer": "Fe"},
        {"question": "37. How many chambers does the human heart have?", "options": ["2", "3", "4"], "answer": "4"},
        {"question": "38. What is the freezing point of water in Fahrenheit?", "options": ["0°F", "32°F", "100°F"], "answer": "32°F"},
        {"question": "39. Which scientific law states that every action has an equal and opposite reaction?", "options": ["Newton's First Law", "Newton's Second Law", "Newton's Third Law"], "answer": "Newton's Third Law"},
        {"question": "40. What is the process of a solid turning directly into a gas called?", "options": ["Sublimation", "Melting", "Deposition"], "answer": "Sublimation"},
        {"question": "41. Which layer of the atmosphere protects Earth from UV rays?", "options": ["Troposphere", "Ozone Layer", "Mesosphere"], "answer": "Ozone Layer"},
        {"question": "42. What is the main structural component of plant cell walls?", "options": ["Starch", "Cellulose", "Protein"], "answer": "Cellulose"},
        {"question": "43. Which gas makes soda fizzy?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen"], "answer": "Carbon Dioxide"},
        {"question": "44. What is the term for animals that eat both plants and meat?", "options": ["Herbivore", "Carnivore", "Omnivore"], "answer": "Omnivore"},
        {"question": "45. Which of the following is a renewable energy source?", "options": ["Coal", "Solar Power", "Natural Gas"], "answer": "Solar Power"},
        {"question": "46. What is the closest star to Earth?", "options": ["Proxima Centauri", "The Sun", "Sirius"], "answer": "The Sun"},
        {"question": "47. What is the measurement unit of frequency?", "options": ["Hertz", "Joule", "Watt"], "answer": "Hertz"},
        {"question": "48. Which gas do humans exhale during respiration?", "options": ["Oxygen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
        {"question": "49. What is the chemical symbol for Silver?", "options": ["Si", "Ag", "Sr"], "answer": "Ag"},
        {"question": "50. What branch of science deals with the study of matter and energy?", "options": ["Chemistry", "Physics", "Biology"], "answer": "Physics"}
    ]
    
    user_answers = []
    st.divider()

    for i, q in enumerate(quiz_bank):
        ans = st.radio(q["question"], ["Select an option"] + q["options"], key=f"q_{i}")
        user_answers.append((ans, q["answer"]))
        st.divider()

    if st.button("🎯 Submit Answers & See Final Score"):
        score = sum(1 for user_ans, correct_ans in user_answers if user_ans == correct_ans)
        total_q = len(quiz_bank)
        
        st.balloons()
        st.metric(label="Your Final Quiz Score", value=f"{score} / {total_q}")
        
        if score == total_q:
            st.success("🎉 Perfect Score! You're a true science expert!")
        else:
            st.info("Great effort! Review the dictionary explorer to learn more terms.")
