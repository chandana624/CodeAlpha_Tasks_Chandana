from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import RegexpTokenizer

app = Flask(__name__)

# FAQ questions and answers
faqs = [
    {
        "question": "What is Python?",
        "answer": "Python is a popular programming language used for web development, data science, AI and machine learning."
    },
    {
        "question": "What is artificial intelligence?",
        "answer": "Artificial Intelligence is a technology that enables computers to perform tasks that normally require human intelligence."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions."
    },
    {
        "question": "What is Flask?",
        "answer": "Flask is a lightweight Python web framework used to build web applications."
    },
    {
        "question": "What is HTML?",
        "answer": "HTML is used to create the structure of web pages."
    },
    {
        "question": "What is CSS?",
        "answer": "CSS is used to style and design web pages."
    },
    {
        "question": "What is JavaScript?",
        "answer": "JavaScript is a programming language used to make web pages interactive."
    },
    {
        "question": "What is an internship?",
        "answer": "An internship provides students with practical experience and an opportunity to learn skills related to their career."
    }
]

# NLTK tokenizer for preprocessing
tokenizer = RegexpTokenizer(r'\w+')


def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    return " ".join(tokens)


faq_questions = [preprocess(faq["question"]) for faq in faqs]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)


@app.route("/", methods=["GET", "POST"])
def home():
    user_question = ""
    answer = ""

    if request.method == "POST":
        user_question = request.form.get("question", "").strip()

        if user_question:
            processed_question = preprocess(user_question)

            user_vector = vectorizer.transform([processed_question])

            similarity_scores = cosine_similarity(
                user_vector, faq_vectors
            )

            best_match_index = similarity_scores.argmax()
            best_score = similarity_scores[0][best_match_index]

            if best_score >= 0.5:
                answer = faqs[best_match_index]["answer"]
            else:
                answer = "Sorry, I could not find a suitable answer to your question."

    return render_template(
        "index.html",
        user_question=user_question,
        answer=answer
    )


if __name__ == "__main__":
    app.run(debug=True)
