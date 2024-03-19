#!/usr/bin/env python3
import random
import os

DIRECTORY_PATH = "./manifests/application/"

CONFIGURATION = {
    "database-secrets.yaml": [
        {
            "replace": "DATABASE_SECRET",
            "good": "c3VwZXJzZWNyZXRwcm9kdWN0aW9ucGFzc3dvcmQ=",
            "bad": "dGhpc2lzbm90dGhlcGFzc3dvcmR5b3VyZWxvb2tpbmdmb3I=",
        },
    ],
    "database-service.yaml": [
        {
            "replace": "NAMESPACE",
            "good": "dojo",
            "bad": "monitoring",
        },
    ],
    "logs-processor-deployment.yaml": [
        {
            "replace": "DELAY_IN_SECONDS",
            "good": "30",
            "bad": "1",
        },
        {
            "replace": "TIMEOUT_IN_SECONDS",
            "good": "5",
            "bad": "1",
        },
        {
            "replace": "PERIOD_IN_SECONDS",
            "good": "10",
            "bad": "1",
        },
        {
            "replace": "FAILURE_THRESHOLD",
            "good": "3",
            "bad": "1",
        },
    ],
    "logs-processor-pv.yaml": [
        {
            "replace": "STORAGE_CAPACITY",
            "good": "1Gi",
            "bad": "0.01Mi",
        },
    ],
    "network-policy-database.yaml": [
        {
            "replace": "INGRESS_FROM_POD",
            "good": "user-info",
            "bad": "user-service",
        }
    ],
    "user-info-deployment.yaml": [
        {
            "replace": "MEMORY_LIMIT",
            "good": "512Mi",
            "bad": "1Mi",
        },
        {
            "replace": "CPU_LIMIT",
            "good": "500m",
            "bad": "1m",
        },
    ],
    "user-info-service.yaml": [
        {
            "replace": "TARGET_PORT",
            "good": "8010",
            "bad": "8011",
        },
    ],
    "webserver-deployment.yaml": [
        {
            "replace": "SERVICE_ACCOUNT_NAME",
            "good": "flask-webserver-service-account",
            "bad": "flask-webserver-service-account-no-access",
        }
    ],
    "webserver-serviceaccount.yaml": [
        {
            "replace": "SECRET_NAME",
            "good": "db-credentials",
            "bad": "secret-credentials",
        }
    ],
}

FILES_TO_CONFIGURE = [file_name for file_name in CONFIGURATION]


def choose_random(item_list):
    random.seed()
    return item_list[random.randint(0, len(item_list) - 1)]


def replace_line_in_file(file_name, misconfigure=False):
    for change in CONFIGURATION[file_name]:
        contents = ""
        word_to_replace = change["replace"]
        if misconfigure:
            replacement = change["bad"]
        else:
            replacement = change["good"]

        with open(os.path.join(DIRECTORY_PATH, file_name), "r") as original_file:
            for line in original_file:
                temp_contents = line.rstrip().replace(
                    word_to_replace,
                    replacement,
                )
                contents += temp_contents + "\n"

        with open(os.path.join(DIRECTORY_PATH, file_name), "w") as updated_file:
            updated_file.write(contents)


FILE_TO_MISCONFIGURE = choose_random(FILES_TO_CONFIGURE)

for file_name in FILES_TO_CONFIGURE:
    # iterate through and update with the working values
    if file_name != FILE_TO_MISCONFIGURE:
        replace_line_in_file(
            file_name,
        )

# now we update one value to break things
replace_line_in_file(FILE_TO_MISCONFIGURE, misconfigure=True)
