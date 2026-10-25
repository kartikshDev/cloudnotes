import json

with open("groups.json") as f:
    groups = json.load(f)

for group in groups:
    print(group["name"], group["location"])