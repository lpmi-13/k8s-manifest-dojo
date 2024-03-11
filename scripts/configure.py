#!/usr/bin/env python3
import random
import os

DIRECTORY_PATH = "./manifests/application/"

CONFIGURATION = {
    "database-service.yaml": {
        "replace": "DATABASE_PORT",
        "good": "5432",
        "bad": "4321",
    },
    "webserver-deployment.yaml": {
        "replace": "SERVICE_ACCOUNT_NAME",
        "good": "flask-webserver-service-account",
        "bad": "flask-webserver-service-account-no-access",
    },
    "webserver-serviceaccount.yaml": {
        "replace": "SECRET_NAME",
        "good": "db-credentials",
        "bad": "secret-credentials",
    },
}

FILES_TO_CONFIGURE = [file_name for file_name in CONFIGURATION]


def choose_random(item_list):
    random.seed()
    return item_list[random.randint(0, len(item_list) - 1)]


def replace_line_in_file(file_name, word_to_replace, replacement):
    contents = ""
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
            CONFIGURATION[file_name]["replace"],
            CONFIGURATION[file_name]["good"],
        )

# now we update one value to break things
replace_line_in_file(
    FILE_TO_MISCONFIGURE,
    CONFIGURATION[FILE_TO_MISCONFIGURE]["replace"],
    CONFIGURATION[FILE_TO_MISCONFIGURE]["bad"],
)
