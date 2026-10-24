import streamlit as st

# 1. Page Configuration & Title
st.set_page_config(
    page_title="SciLingua: Little Science Explorers",
    page_icon="🔬",
    layout="centered",
)

# Custom Styling for Kid-Friendly Bright UI
st.markdown(
    """
    <style>
    .main {
        background-color: #f7fbff;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 6px solid #ff4b4b;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        height: 45px;
        width: 100%;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 2. Curated Science Dataset (English & Tamil)
science_data = [
    {
        "term": "Magnet",
        "tamil": "காந்தம் (Kaantham)",
        "category": "Physics",
        "icon": "🧲",
        "definition": (
            "An object that attracts metals like iron. / இரும்பை ஈர்க்கும் ஒரு"
            " பொருள்."
        ),
    },
    {
        "term": "Photosynthesis",
        "tamil": "ஒளிச்சேர்க்கை (Olicherkai)",
        "category": "Biology",
        "icon": "🌿",
        "definition": (
            "How plants make food using sunlight. / தாவரங்கள் சூரிய ஒளியைப்"
            " பயன்படுத்தி உணவு தயாரிக்கும் முறை."
        ),
    },
    {
        "term": "Solar System",
        "tamil": "சூரிய குடும்பம் (Sooriya Kudumbam)",
        "category": "Space",
        "icon": "☀️",
        "definition": (
            "The Sun and all the planets revolving around it. / சூரியனும் அதைச்"
            " சுற்றும் கோள்களும்."
        ),
    },
    {
        "term": "Electricity",
        "tamil": "மின்சாரம் (Minsaram)",
        "category": "Physics",
        "icon": "⚡",
        "definition": (
            "Flow of electric power that runs appliances. / மின்சாதனங்களை"
            " இயக்கும் ஆற்றல்."
        ),
    },
    {
        "term": "Ecosystem",
        "tamil": "சூழல் மண்டலம் (Soozhal Mandalam)",
        "category": "Biology",
        "icon": "🌍",
        "definition": (
            "A community of living things interacting with their environment."
            " / உயிரினங்களும் அவற்றின் சுற்றுப்புறமும்."
        ),
    },
]

# Quiz Questions Database
quiz_questions = [
    {
        "question": (
            "What is the Tamil word for 'Magnet'? \n 'காந்தம்' எதைக் குறிக்கிறது?"
        ),
        "options": [
            "Electricity (மின்சாரம்)",
            "Magnet (காந்தம்)",
            "Force (விசை)",
            "Heat (வெப்பம்)",
        ],
        "answer": "Magnet (காந்தம்)",
    },
    {
        "question": (
            "How do plants make food using sunlight? \n தாவரங்கள் உணவு"
            " தயாரிக்க உதவும் முறை எது?"
        ),
        "options": [
            "Photosynthesis (ஒளிச்சேர்க்கை)",
            "Evaporation (நீராவிப்போக்கு)",
            "Respiration (சுவாசம்)",
            "Condensation (நீர்த்துளிதல்)",
        ],
        "answer": "Photosynthesis (ஒளிச்சேர்க்கை)",
    },
]

# App Header
st.title("🔬 SciLingua: Little Science Explorers")
st.write(
    "Welcome! Explore cool science words in **English & Tamil**, then test your"
    " skills with our fun quiz game!"
)

# Sidebar Menu for Navigation
menu = st.sidebar.radio("Choose Mode:", ["📘 Learn Words", "🎮 Quiz Challenge"])

# --- MODE 1: LEARN WORDS (Interactive Dictionary) ---
if menu == "📘 Learn Words":
    st.header("Interactive Science Dictionary")
    st.write(
        "Type a science word or browse through the cards below to learn their"
        " meanings in Tamil!"
    )

    # Real-time search filter bar
    search_query = st.text_input(
        "🔍 Search keyword (e.g., Magnet, Photosynthesis, Solar):"
    )

    # Filter data list dynamically based on search
    filtered_data = [
        item
        for item in science_data
        if search_query.lower() in item["term"].lower()
        or search_query.lower() in item["tamil"].lower()
    ]

    if not filtered_data:
        st.warning(
            "No science words found matching your search. Try another word!"
        )

    # Render dynamic UI cards for each science term
    for item in filtered_data:
        st.markdown(
            f"""
        <div class="card">
            <h3>{item['icon']} {item['term']}</h3>
            <p><b>Tamil Translation:</b> {item['tamil']}</p>
            <p><b>Category:</b> {item['category']}</p>
            <p><b>Definition:</b> {item['definition']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# --- MODE 2: QUIZ CHALLENGE ---
elif menu == "🎮 Quiz Challenge":
    st.header("Science Quiz Arena 🏆")
    st.write("Answer the questions correctly to test your science superpower!")

    # Interactive Quiz Loop with Instant Feedback
    for idx, q in enumerate(quiz_questions):
        st.subheader(f"Question {idx + 1}")
        user_choice = st.radio(q["question"], q["options"], key=f"q_{idx}")

        if st.button(f"Submit Answer {idx + 1}", key=f"btn_{idx}"):
            if user_choice == q["answer"]:
                st.success(
                    "🎉 Correct! Excellent job, you're a true science explorer!"
                )
            else:
                st.error(
                    f"❌ Not quite right! The correct answer is: {q['answer']}"
                )

        st.markdown("---")

    st.info(
        "💡 **Expo Tip:** Have visiting school students play this challenge"
        " live at your booth and see who gets both answers correct!"
    )
