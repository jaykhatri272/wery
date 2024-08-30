from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Updated questions with more entries
questions = [{
    "question":
    "What are you interested in? (e.g., Technology, Arts, Science, Business, Medicine, Social Services)",
    "options": {
        "Technology":
        ["Software Developer", "Data Scientist", "Cybersecurity Analyst"],
        "Arts": ["Graphic Designer", "Writer", "Photographer"],
        "Science": ["Biologist", "Chemist", "Astronomer"],
        "Business": ["Marketing Manager", "Financial Analyst", "Entrepreneur"],
        "Medicine": ["Doctor", "Nurse", "Pharmacist"],
        "Social Services":
        ["Social Worker", "Counselor", "Human Resources Specialist"]
    }
}, {
    "question":
    "What is your strongest skill? (e.g., Problem-solving, Creativity, Analytical thinking, Communication, Leadership, Technical skills)",
    "options": {
        "Problem-solving": ["Engineer", "Consultant", "Scientist"],
        "Creativity": ["Artist", "Designer", "Writer"],
        "Analytical thinking":
        ["Data Analyst", "Financial Analyst", "Research Scientist"],
        "Communication":
        ["Public Relations Specialist", "Sales Manager", "Teacher"],
        "Leadership": ["Project Manager", "Team Lead", "Entrepreneur"],
        "Technical skills": [
            "Software Developer", "Network Administrator",
            "Technical Support Specialist"
        ]
    }
}, {
    "question":
    "Do you prefer working in a team or alone? (Type 'team', 'alone', or 'both')",
    "options": {
        "team": ["Project Manager", "Team Lead", "Salesperson"],
        "alone": ["Freelancer", "Researcher", "Software Developer"],
        "both": ["Consultant", "Entrepreneur", "Academic"]
    }
}, {
    "question":
    "Are you interested in working in a high-stress environment? (Type 'yes' or 'no')",
    "options": {
        "yes": ["Stock Broker", "Surgeon", "Emergency Services"],
        "no": ["Librarian", "Data Entry Clerk", "Academic"]
    }
}, {
    "question":
    "Do you prefer working with people, data, or things? (Type 'people', 'data', or 'things')",
    "options": {
        "people": ["Human Resources", "Social Worker", "Customer Service"],
        "data": ["Data Analyst", "Statistician", "IT Specialist"],
        "things": ["Engineer", "Mechanic", "Architect"]
    }
}, {
    "question":
    "What level of education are you willing to pursue? (Type 'high school', 'bachelor's', 'master's', 'doctorate')",
    "options": {
        "high school":
        ["Entry-Level Positions", "Trade Skills", "Sales Representative"],
        "bachelor's": ["Manager", "Teacher", "Marketing Specialist"],
        "master's": ["Consultant", "Project Manager", "Advanced Researcher"],
        "doctorate":
        ["University Professor", "Research Scientist", "Senior Consultant"]
    }
}]


@app.route('/')
def index():
    return render_template('index.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    responses = data.get('responses', {})
    suggestions = set()

    for q, answers in responses.items():
        options = next((item["options"]
                        for item in questions if item["question"] == q), {})
        for answer in answers:
            if answer in options:
                suggestions.update(options[answer])

    return jsonify({"suggestions": list(suggestions)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
