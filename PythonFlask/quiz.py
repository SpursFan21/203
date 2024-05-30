from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "What planet is known as the red planet?",
        "choices": ["Mars", "Mercury", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Claude Monet", "Da Vinci", "Salvador Dali", "Picasso"],
        "correct_answer": "Da Vinci"
    }
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        user_answers = []
        for i in range(len(questions)):
            user_answers.append(request.form.get(f"answers{i}"))
        score = calculate_score(user_answers)
        return render_template("quiz_result.html", score=score, total=len(questions))
    return render_template("quiz.html", questions=questions, enumerate=enumerate)

def calculate_score(user_answers):
    score = 0
    for i in range(len(user_answers)):
        if user_answers[i] == questions[i]["correct_answer"]:
            score += 1
    return score

if __name__ == "__main__":
    app.secret_key = "secret_key"
    app.run(debug=True)
