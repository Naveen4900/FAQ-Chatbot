# 🤖 AI FAQ Chatbot

## 📌 Project Overview

The AI FAQ Chatbot is an NLP-powered question-answering system developed as part of the CodeAlpha Artificial Intelligence Internship Program. The application allows users to ask AI-related questions and receive relevant answers by matching user queries against a predefined FAQ knowledge base using Natural Language Processing techniques.

The chatbot leverages TF-IDF Vectorization and Cosine Similarity to identify the most relevant response, providing an interactive and user-friendly experience through a Streamlit web interface.

---

## 🚀 Features

* Interactive web-based chatbot interface using Streamlit
* FAQ question matching using Natural Language Processing (NLP)
* TF-IDF Vectorization for text feature extraction
* Cosine Similarity for semantic question matching
* Real-time response generation
* Lightweight and easy-to-use architecture
* Beginner-friendly implementation of NLP concepts

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NLTK (Natural Language Toolkit)
* Scikit-Learn
* NumPy
* JSON

---

## 📂 Project Structure

```text
CodeAlpha_ChatbotFAQ/
│
├── app.py
├── faq.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/CodeAlpha_ChatbotFAQ.git
cd CodeAlpha_ChatbotFAQ
```

### Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python -m streamlit run app.py
```

After running the command, the application will open automatically in your default browser.

---

## 💡 Sample Questions

Try asking:

* What is Artificial Intelligence?
* What is Machine Learning?
* What is Deep Learning?
* What is NLP?
* What is Computer Vision?

---

## 📈 NLP Techniques Implemented

### TF-IDF Vectorization

Converts textual questions into numerical feature vectors based on term importance.

### Cosine Similarity

Measures similarity between the user's query and stored FAQ questions to identify the most relevant answer.

---

## 🎯 Learning Outcomes

Through this project, the following concepts were implemented and explored:

* Natural Language Processing (NLP)
* Text Preprocessing
* Information Retrieval
* Similarity-Based Search
* Streamlit Application Development
* Python-Based AI Applications

---

## 📜 Internship Information

This project was developed as part of the Artificial Intelligence Internship Program offered by CodeAlpha.

---

## 👨‍💻 Author

Naveen Chowdary

Artificial Intelligence & Machine Learning Enthusiast

CodeAlpha AI Intern
