from flask import Flask, render_template, request, redirect, session, url_for

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
    }
]

@app.route('/')
def index():
    session['score'] = 0
    session['question_index'] = 0
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
        return redirect(url_for('quiz'))

    current_question = questions[index]
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
