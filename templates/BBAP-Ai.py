# BBAP-AI.py

# 1. Import Libraries
import os
import spacy
from transformers import pipeline
from flask import Flask, request, jsonify

# Load NLP model and QA pipeline
nlp = spacy.load('en_core_web_sm')  # For language processing
qa_pipeline = pipeline("question-answering")  # For Q&A functionality

# Initialize Flask app
app = Flask(__name__)

# 2. Define Functions for Each Module

# Educational Resources Module
def get_resources(topic):
    resources = {
        "beginner": ["Intro to Bug Bounty", "Ethical Hacking Basics"],
        "intermediate": ["OWASP Top 10", "Web App Security"],
        "advanced": ["Advanced Exploits", "Reverse Engineering"]
    }
    return resources.get(topic, "Resources not available.")

# Mentorship Module
def connect_with_mentor(level):
    mentors = {
        "beginner": "John Doe, specializes in XSS and SQLi",
        "intermediate": "Jane Smith, expertise in CSRF and SSRF",
        "advanced": "Dr. Brown, pentesting veteran and exploit developer"
    }
    return mentors.get(level, "Mentorship not available.")

# Community Information Module
def get_community_info():
    return {
        "forums": "https://community.bugbounty.com",
        "events": "Monthly bug-bounty meetups",
        "chats": "Slack/Discord groups for collaboration"
    }

# Question Answering Module
def answer_question(question):
    context = "Bug bounty hunting focuses on finding vulnerabilities in systems..."  # This should be updated to fit more context over time.
    return qa_pipeline({'question': question, 'context': context})['answer']

# 3. Set Up API Endpoints

@app.route('/get_resources', methods=['POST'])
def resources_endpoint():
    data = request.json
    topic = data.get('topic')
    resources = get_resources(topic)
    return jsonify({"resources": resources})

@app.route('/connect_with_mentor', methods=['POST'])
def mentor_endpoint():
    data = request.json
    level = data.get('level')
    mentor_info = connect_with_mentor(level)
    return jsonify({"mentor": mentor_info})

@app.route('/community_info', methods=['GET'])
def community_endpoint():
    community_info = get_community_info()
    return jsonify(community_info)

@app.route('/answer_question', methods=['POST'])
def question_endpoint():
    data = request.json
    question = data.get('question')
    answer = answer_question(question)
    return jsonify({"answer": answer})

# 4. Run the Flask App

if __name__ == '__main__':
    app.run(debug=True)
