from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def check_datetime():
    with open("/tmp/k3s-data/1.txt", "r") as log_file:
        log_data = log_file.readlines()

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Current date and time is: {current_time} and also {log_data[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
