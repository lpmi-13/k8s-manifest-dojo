from flask import Flask
import os
import requests

# we can just use the name of the services, due to DNS record creation on service creation
LOG_PROCESSOR_DNS_NAME = "logs-processor"
USER_INFO_DNS_NAME = "user-info"
ENVIRONMENT = os.getenv("ENVIRONMENT", default="DEVELOPMENT")


app = Flask(__name__)


@app.route("/")
def default_path():
    return "ready to serve content!"


@app.route("/log-info")
def log_info():

    try:
        response = requests.get(f"http://{LOG_PROCESSOR_DNS_NAME}/log-count")
        log_count = response.json()["log_count"]
        print(f"received a total log count of: {log_count}")

        return f"environment is: {ENVIRONMENT}, and we have {log_count} total log lines"
    except Exception as e:
        print(f"received an error: {e}")


@app.route("/all_users")
def all_users():
    try:
        response = requests.get(f"http://{USER_INFO_DNS_NAME}/users")
        users = response.json()

        return {"all_users": users}
    except Exception as e:
        print(f"received an error: {e}")


@app.route("/user/<int:user_id>")
def get_user_by_id(user_id):
    try:
        response = requests.get(f"http://{USER_INFO_DNS_NAME}/user/{user_id}")
        user = response.json()

        return {"user": user}
    except Exception as e:
        print(f"received an error: {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
