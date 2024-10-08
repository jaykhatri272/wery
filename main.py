from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Example questions and options
questions = [
    {
        "question": "What are you interested in? (e.g., Technology, Arts, Science, Business, Medicine, Social Services)",
        "options": {
            "Technology": ["Software Developer", "Data Scientist", "Cybersecurity Analyst"],
            "Arts": ["Graphic Designer", "Writer", "Photographer"],
            "Science": ["Biologist", "Chemist", "Astronomer"],
            "Business": ["Marketing Manager", "Financial Analyst", "Entrepreneur"],
            "Medicine": ["Doctor", "Nurse", "Pharmacist"],
            "Social Services": ["Social Worker", "Counselor", "Human Resources Specialist"]
        }
    },
    {
        "question": "What is your strongest skill? (e.g., Problem-solving, Creativity, Analytical thinking, Communication, Leadership, Technical skills)",
        "options": {
            "Problem-solving": ["Engineer", "Consultant", "Scientist"],
            "Creativity": ["Artist", "Designer", "Writer"],
            "Analytical thinking": ["Data Analyst", "Financial Analyst", "Research Scientist"],
            "Communication": ["Public Relations Specialist", "Sales Manager", "Teacher"],
            "Leadership": ["Project Manager", "Team Lead", "Entrepreneur"],
            "Technical skills": ["Software Developer", "Network Administrator", "Technical Support Specialist"]
        }
    },
    # Add more questions as needed
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    responses = data.get('responses', {})
    suggestions = set()
    
    for q, answers in responses.items():
        options = next((item["options"] for item in questions if item["question"] == q), {})
        for answer in answers:
            if answer in options:
                suggestions.update(options[answer])
    
    return jsonify({"suggestions": list(suggestions)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
