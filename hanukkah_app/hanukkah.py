import streamlit as st
from PIL import Image, ImageDraw
import datetime
import random
import openai
import os
import time


# Load environment variables (for OpenAI key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title and layout
st.set_page_config(page_title="Hanukkah Menorah", page_icon="🕎", layout="centered")
st.title("🕎 Happy Hanukkah! 🕯️")

# Display Beautiful Menorah Image
menorah_image = Image.open("Pictures/menorah.jpg") # Replace with path to your menorah image
st.image(menorah_image, caption="Beautiful Hanukkah Menorah", use_container_width=True)

# Blessings
st.subheader("🕯️ Hanukkah Blessings")
st.write("""
**Blessing Over the Candles (Nightly):**  
*Baruch atah Adonai Eloheinu, Melech ha'olam,  
asher kid'shanu b'mitzvotav, v'tzivanu l'hadlik ner shel Hanukkah.*  
""")

# Hanukkah Fact
st.subheader("🧆 Fun Hanukkah Fact")
facts = [
    "Hanukkah means 'dedication' in Hebrew.",
    "Latkes and sufganiyot are traditional Hanukkah foods.",
    "Hanukkah is celebrated for eight nights to commemorate the oil miracle.",
    "The dreidel was used to hide Torah study from Greek soldiers.",
    "Hanukkah is also called the Festival of Lights."
]
if st.button("Tell me a Fact"):
    st.write(f"**{random.choice(facts)}**")

# Quiz Section
st.subheader("🧠 Hanukkah Quiz")
quiz_questions = [
    {
        "question": "What is the name of the traditional Hanukkah game played with a spinning top?",
        "options": ["Dreidel", "Yarmulke", "Latke"],
        "answer": "Dreidel"
    },
    {
        "question": "Which oil-based food is commonly eaten during Hanukkah?",
        "options": ["Latkes", "Matzah", "Bagels"],
        "answer": "Latkes"
    },
    {
        "question": "Hanukkah celebrates the rededication of which temple?",
        "options": ["First Temple", "Second Temple", "Western Wall"],
        "answer": "Second Temple"
    },
    {
        "question": "What does the word 'Hanukkah' mean?",
        "options": ["Festival of Lights", "Dedication", "Miracle of Oil"],
        "answer": "Dedication"
    },
    {
        "question": "How long does Hanukkah last?",
        "options": ["7 days", "8 days", "9 days"],
        "answer": "8 days"
    },
    {
        "question": "Which color is often associated with Hanukkah decorations?",
        "options": ["Blue and White", "Red and Green", "Gold and Silver"],
        "answer": "Blue and White"
    },
    {
        "question": "What is the candle in the center of the menorah called?",
        "options": ["Shamash", "Maccabee", "Chai"],
        "answer": "Shamash"
    },
    {
        "question": "Who were the heroes of the Hanukkah story?",
        "options": ["Levites", "Maccabees", "Pharaohs"],
        "answer": "Maccabees"
    },
    {
        "question": "Which ancient empire did the Maccabees fight against?",
        "options": ["Roman Empire", "Greek Empire", "Persian Empire"],
        "answer": "Greek Empire"
    },
    {
        "question": "What item is traditionally placed in windows during Hanukkah?",
        "options": ["Dreidel", "Menorah", "Torah"],
        "answer": "Menorah"
    }
]

# Initialize session state
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Quiz logic
if st.session_state.question_index < len(quiz_questions):
    q = quiz_questions[st.session_state.question_index]
    user_answer = st.radio(q['question'], q['options'])

    if not st.session_state.submitted:
        if st.button("Submit Answer"):
            st.session_state.submitted = True
            if user_answer == q['answer']:
                st.success("Correct! 🎉")
                st.session_state.quiz_score += 1
            else:
                st.error("Incorrect! 😞")

    if st.session_state.submitted:
        if st.button("Next Question"):
            st.session_state.question_index += 1
            st.session_state.submitted = False
            st.rerun()
else:
    st.session_state.quiz_complete = True

if st.session_state.quiz_complete:
    st.write(f"🎉 Quiz complete! Your score: {st.session_state.quiz_score}/{len(quiz_questions)}")

    # Score Visualization
    st.subheader("📊 Quiz Results")
    st.bar_chart({"Correct Answers": [st.session_state.quiz_score], "Incorrect Answers": [len(quiz_questions) - st.session_state.quiz_score]})

    if st.button("Restart Quiz"):
        st.session_state.quiz_score = 0
        st.session_state.question_index = 0
        st.session_state.quiz_complete = False
        st.rerun()


# Hanukkah Q&A with OpenAI
st.subheader("🕯️ Ask Me Anything About Hanukkah")
st.write("Feel free to ask any question about Hanukkah!")

user_question = st.text_input("Your Question:")
if st.button("Get Answer"):
    if user_question:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant knowledgeable about Hanukkah."},
                      {"role": "user", "content": user_question}]
        )
        st.write(response.choices[0].message.content.strip())
    else:
        st.warning("Please enter a question!")
