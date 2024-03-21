from flask import Flask
import json
import os
import sys

LOGS_DIRECTORY = "/tmp/k3s-data/"
ENVIRONMENT = os.getenv("ENVIRONMENT", default="DEVELOPMENT")

app = Flask(__name__)

log_files = os.listdir(LOGS_DIRECTORY)

all_logs = []

for file in log_files:
    with open(f"{LOGS_DIRECTORY}/{file}", "r") as log_file:
        log_data = log_file.readlines()
        for log_line in log_data:
            all_logs.append(json.loads(log_line))

# we're doing this inner loop madness to simulate a very long execution time, since we want
# the application to not be ready immediately.
indexes_to_delete = []
try:
    for i in range(len(all_logs)):
        for j in range(len(all_logs)):
            if i != j and all_logs[i] == all_logs[j]:
                if i not in indexes_to_delete:
                    indexes_to_delete.append(i)
except:
    print("received error while processing")

for index in indexes_to_delete:
    all_logs.pop(index)

LOGS_FOR_ENVIRONMENT = list(
    filter(lambda x: x["environment"] == ENVIRONMENT.lower(), all_logs)
)


@app.route("/log-count")
def log_count():
    try:
        response = {"log_count": len(LOGS_FOR_ENVIRONMENT), "environment": ENVIRONMENT}
        return json.dumps(response)

    except Exception as e:
        print(f"received an error: {e}")
        # forces the error to stop the gunicorn process, making it more obvious
        sys.exit(4)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
