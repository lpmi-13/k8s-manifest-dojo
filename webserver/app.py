from flask import Flask
import os
import requests

# we can just use the name of the service, due to DNS record creation on service creation
LOG_PROCESSOR_DNS_NAME = "logs-processor"
ENVIRONMENT = os.getenv("ENVIRONMENT", default="DEVELOPMENT")


app = Flask(__name__)


@app.route("/")
def log_info():

    try:
        response = requests.get(f"http://{LOG_PROCESSOR_DNS_NAME}/log-count")
        log_count = response.json()["log_count"]
        print(f"received a total log count of: {log_count}")

        return f"environment is: {ENVIRONMENT}, and we have {log_count} total log lines"
    except Exception as e:
        print(f"received an error: {e}")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
