from flask import Flask

app = Flask(__name__)
your_name = "Dan"

@app.route('/')
def get_welcome():
    return f'Welcome to {your_name}’s web site!'

if __name__ == '__main__':
    app.run(debug=True)
