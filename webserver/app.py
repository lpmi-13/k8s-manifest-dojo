from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def check_datetime():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Current date and time is: {current_time}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
