#! /usr/bin/env python3

import os
import glob
import json
import random

NUMBER_OF_LOGS = 10
NUMBER_OF_LINES_PER_LOG = 100

LOG_LEVEL = ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]

USERS = [
    "alice",
    "bob",
    "carol",
    "dave",
    "eleanor",
    "frank",
    "gia",
    "harry",
    "ingrid",
    "jack",
    "kelly",
    "leo",
    "maya",
    "norman",
    "olivia",
    "pete",
    "quinn",
    "ralph",
    "stephanie",
    "travis",
    "ursula",
    "vinny",
    "willa",
    "xander",
    "yara",
    "zain",
]

AS_ADMIN = [
    True,
    False,
]

ACTIONS = [
    "create",
    "read",
    "update",
    "delete",
    "list",
]

RESOURCES = [
    "application",
    "data",
    "services",
    "compute",
    "database",
    "network",
    "firewall",
    "cdn",
    "cluster",
    "users",
    "storage",
]

REGIONS = ["us", "eu", "me", "af", "as", "au"]

ENVIRONMENTS = ["development", "staging", "production"]

PROJECTS = ["alpha", "beta", "gamma", "theta"]


def choose_random_item(item_list):
    return item_list[random.randint(0, len(item_list) - 1)]


# clear out existing file
pattern_to_delete = os.path.join("/tmp/k3s-data/", "*")
files = glob.glob(pattern_to_delete)

for file in files:
    if os.path.isfile(file):
        os.remove(file)


for i in range(NUMBER_OF_LOGS):

    with open(f"/tmp/k3s-data/log-file-{i}", "w") as output_file:
        for i in range(NUMBER_OF_LINES_PER_LOG):
            log_line = {
                "log_level": choose_random_item(LOG_LEVEL),
                "user": choose_random_item(USERS),
                "action": choose_random_item(ACTIONS),
                "as_admin": choose_random_item(AS_ADMIN),
                "resource": choose_random_item(RESOURCES),
                "region": choose_random_item(REGIONS),
                "environment": choose_random_item(ENVIRONMENTS),
                "project": choose_random_item(PROJECTS),
            }
            output_file.write(json.dumps(log_line))
            output_file.write("\n")
