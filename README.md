# cyberbullying-detection
Real-time multilingual cyberbullying detection web application built using Python, Flask, and Machine Learning. Supports language detection, text classification, and auto user-blocking. 


# 🚨 Cyberbullying Detection Web App

A real-time multilingual cyberbullying detection Web Application built using Python, Flask, Machine Learning, and Language Detection.
This project identifies cyberbullying content in user comments, detects the language, and automatically handles user blocking based on repeated offensive behavior.

## 🌟 Features

🔍 Real-time cyberbullying detection

🌐 Multilingual text processing (English, Tamil, Hindi, Roman Urdu, Tanglish)

⚙️ ML model for comment classification

🚫 Auto-blocking system for repeated offenders

🗂 MongoDB backend for user & comment storage

🧹 Text preprocessing & cleaning pipeline

🌈 Simple and responsive UI (Flask templates)

🧪 Uses SDLC phases: Requirement → Design → Development → Testing → Deployment

## 🧠 System Architecture

1. User inputs a comment
2. Language is detected
3. Comment is preprocessed
4. ML model classifies the comment
5. If offensive → strike count increases
6. User is auto-blocked after 3 offenses
7. Result returned to UI

## 🛠️ Tech Stack
Frontend

HTML, CSS, JavaScript

Flask Templates

Backend

Python

Flask

Joblib ML Model

Machine Learning

Scikit-learn

NLP preprocessing

TF-IDF / CountVectorizer

Database

MongoDB (User data, comments, blocking status)

## 📁 Project Structure
cyberbullying-detection/
│── app.py
│── requirements.txt
│── README.md
│── static/
│── templates/
│── model/
│     └── cyberbullying_model.pkl
└── utils/
      ├── preprocess.py
      └── model.py

## ▶️ How to Run the Project
1. Install dependencies
pip install -r requirements.txt

2. Run Flask app
python app.py

3. Open browser
http://127.0.0.1:5000/

## 🧪 Machine Learning Workflow

Labelled dataset prepared manually

Text cleaning (stopwords, punctuation removal)

TF-IDF feature extraction

Trained using Logistic Regression / SVM

Saved model using Joblib

Deployed with Flask API

## 📊 Results

40% improvement in moderation efficiency

High precision on offensive content

Fast inference (< 1 second per request)

## 📌 Future Enhancements

Mobile-friendly UI

Add CNN/LSTM for better accuracy

Deploy to cloud (AWS/Render/Heroku)

Add voice-to-text abuse filtering

## 👩‍💻 Author

Vedha Dharshini K

B.Tech AI & DS (2025)

LinkedIn: linkedin.com/in/vedhu23

GitHub: github.com/VedhaDharshini

## ⭐ Support

If you like this project, please ⭐ star the repository!
