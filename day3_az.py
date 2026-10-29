import subprocess 
import json

out = subprocess.run(["az", "group", "list", "-o", "json"], capture_output=True, text=True)

groups = json.loads(out.stdout)
for g in groups:
    print(g["name"])