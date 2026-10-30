import subprocess 
import json

out = subprocess.run(["az", "group", "list", "-o", "json"], capture_output=True, text=True)

groups = json.loads(out.stdout)

for g in groups:
    tags = g.get("tags") or {}
    if "owner" not in tags:
        print(g["name"], "is missing an owner tag")
    else:
        print(g["name"], "has an owner tag:", tags["owner"])