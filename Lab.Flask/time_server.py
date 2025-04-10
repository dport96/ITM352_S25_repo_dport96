from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time')
def get_datetime():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Current Server Date and Time: {current_time}'

if __name__ == '__main__':
    app.run(debug=True)
