import streamlit as st
import json
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

with open("faq.json", "r") as file:
    faq_data = json.load(file)

questions = list(faq_data.keys())

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)

def get_response(user_question):

    user_vector = vectorizer.transform([user_question])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()

    confidence = similarity_scores[0][best_match_index]

    if confidence < 0.2:
        return "Sorry, I could not find a suitable answer."

    return faq_data[questions[best_match_index]]

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI FAQ Chatbot")

st.write("Ask any AI related question")

user_input = st.text_input(
    "Enter your question"
)

if st.button("Ask"):

    if user_input:

        response = get_response(user_input)

        st.success(response)
