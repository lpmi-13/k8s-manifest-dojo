from flask import Flask
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def check_datetime():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = {"current_time": current_time}
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
