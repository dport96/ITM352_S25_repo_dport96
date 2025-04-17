from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# Sample questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Madrid", "Paris"],
        "correct": "d"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct": "b"
    },
        {
        "question": "xxx?",
        "options": ["yyy", "zzz", "qqq", "Satufffrn"],
        "correct": "a"
    }
]

@app.route('/')
def index():
    session['score'] = 0
    session['question_index'] = 0
    session['questions_index'] =  random.sample(range(len(questions)), len(questions))
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    index = session.get('question_index', 0)

    if index >= len(questions):
        return redirect(url_for('result'))

    if request.method == 'POST':
        selected = request.form.get('answer')
        correct = questions[index]['correct']
        if selected == correct:
            session['score'] += 1           
        session['question_index'] += 1
        return render_template('feedback.html', feedback = f"That was {  "correct" if selected == correct else "incorrect" }! Your score is {session['score']} out of {index + 1} questions")

    index_to_ask = session['questions_index'][index]
    current_question = questions[index_to_ask]
    letters = list('abcd')
    zipped_options = zip(letters, current_question['options'])
    return render_template('quiz.html', question=current_question, index=index + 1, total=len(questions), options = zipped_options)

@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(questions)
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
