# FAQ Chatbot

## Project Description

The FAQ Chatbot is a web-based application that automatically answers frequently asked questions.

The chatbot processes the user's question and finds the most similar FAQ using TF-IDF and cosine similarity. It then displays the most suitable answer.

## Features

- FAQ-based question answering
- Text preprocessing using NLTK
- TF-IDF text vectorization
- Cosine similarity matching
- Best matching answer selection
- Professional web interface
- Handles questions that are not available in the FAQ list

## Technologies Used

- Python
- Flask
- NLTK
- Scikit-learn
- HTML
- CSS

## How It Works

1. User enters a question.
2. The question is preprocessed using NLTK.
3. TF-IDF converts the questions into numerical vectors.
4. Cosine similarity compares the user's question with stored FAQ questions.
5. The chatbot selects the best matching FAQ.
6. The corresponding answer is displayed.

## Project Structure

```text
CodeAlpha_FAQChatbot_Chandana
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates
    └── index.html
    How to Run
Install the required libraries:
pip install -r requirements.txt
Run the application:
python app.py
Open the application in a web browser:
http://127.0.0.1:5000
Internship
This project is developed as part of the CodeAlpha Artificial Intelligence Internship.
