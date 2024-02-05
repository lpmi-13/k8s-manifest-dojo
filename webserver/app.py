from flask import Flask
import requests

# we can just use the name of the service, due to DNS record creation on service creation
BACKEND_DNS_NAME = "flask-backend"

app = Flask(__name__)

@app.route('/')
def check_datetime():
    with open("/tmp/k3s-data/1.txt", "r") as log_file:
        log_data = log_file.readlines()

    response = requests.get(f"http://{BACKEND_DNS_NAME}")
    current_time = response.json()["current_time"]
    print(f"received a time of: {current_time}")

    return f'Current date and time is: {current_time} and also {log_data[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
