from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded users dictionary
USERS = {
    "port": "port123",
    "kazman": "kazman123"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if USERS.get(username) == password:
            return redirect(url_for('success'))
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>"
    return render_template('login.html')

@app.route('/success')
def success():
    return "<h1>Login Successful!</h1><p>Welcome to the site.</p>"

if __name__ == '__main__':
    app.run(debug=True)
