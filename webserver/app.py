from flask import Flask
import os
import requests

# we can just use the name of the service, due to DNS record creation on service creation
BACKEND_DNS_NAME = "logs-processor"
ENVIRONMENT = os.getenv("ENVIRONMENT", default="DEVELOPMENT")

DB_USERNAME = os.getenv("DB_USERNAME", default="testuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="testpassword")

app = Flask(__name__)


@app.route("/")
def log_info():

    try:
        response = requests.get(f"http://{BACKEND_DNS_NAME}/log-count")
        log_count = response.json()["log_count"]
        print(f"received a total log count of: {log_count}")

        return f"environment is: {ENVIRONMENT}, and we have {log_count} total log lines"
    except Exception as e:
        print(f"received an error: {e}")


@app.route("/creds-test")
def check_creds():
    return f"username: {DB_USERNAME}, password: {DB_PASSWORD}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
