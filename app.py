# ==========================================
# QuizMind - AI Quiz Challenge
# Author: Anoosha Aman
# ==========================================

import streamlit as st
import random

# Import quiz questions
from questions import questions


# ------------------------------------------
# Page Configuration
# ------------------------------------------

st.set_page_config(
    page_title="QuizMind",
    page_icon="🧠",
    layout="centered"
)


# ------------------------------------------
# Initialize Session State
# ------------------------------------------

# Store current question number
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Store user's score
if "score" not in st.session_state:
    st.session_state.score = 0

# Store whether answer was submitted
if "answered" not in st.session_state:
    st.session_state.answered = False

# Store selected answer
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None


# ------------------------------------------
# Title
# ------------------------------------------

st.title("🧠 QuizMind")
st.subheader("AI Quiz Challenge")

st.write(
    "Test your knowledge with an interactive Python quiz!"
)


# ------------------------------------------
# Get Current Question
# ------------------------------------------

current_index = st.session_state.question_index

current_question = questions[current_index]


# ------------------------------------------
# Progress
# ------------------------------------------

total_questions = len(questions)

st.progress(
    current_index / total_questions
)

st.write(
    f"Question {current_index + 1} of {total_questions}"
)


# ------------------------------------------
# Display Question
# ------------------------------------------

st.markdown(
    f"### {current_question['question']}"
)


# ------------------------------------------
# Answer Options
# ------------------------------------------

selected_answer = st.radio(
    "Choose your answer:",
    current_question["options"],
    key=f"question_{current_index}"
)


# ------------------------------------------
# Submit Answer
# ------------------------------------------

if st.button("Submit Answer"):

    st.session_state.selected_answer = selected_answer

    # Check answer
    if selected_answer == current_question["answer"]:

        st.success("🎉 Correct answer!")

        # Increase score
        st.session_state.score += 1

    else:

        st.error(
            f"❌ Wrong! Correct answer: "
            f"{current_question['answer']}"
        )

    st.session_state.answered = True


# ------------------------------------------
# Next Question
# ------------------------------------------

if st.session_state.answered:

    if st.button("Next Question ➡️"):

        # Move to next question
        st.session_state.question_index += 1

        # Reset answer state
        st.session_state.answered = False
        st.session_state.selected_answer = None

        # Refresh page
        st.rerun()


# ------------------------------------------
# Quiz Completed
# ------------------------------------------

if current_index == total_questions - 1:

    if st.session_state.answered:

        st.divider()

        st.success("🏆 Quiz Completed!")

        st.write(
            f"Your Score: "
            f"{st.session_state.score} / {total_questions}"
        )

        # Calculate percentage
        percentage = (
            st.session_state.score / total_questions
        ) * 100

        st.write(
            f"Percentage: {percentage:.0f}%"
        )

        # Restart button
        if st.button("🔄 Restart Quiz"):

            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.selected_answer = None

            st.rerun()
            