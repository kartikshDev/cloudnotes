import json , subprocess
result = subprocess.run(["terraform" ,"show", "-json", "tfplan"], capture_output=True, text=True)
plan = json.loads(result.stdout)
counts = {"create": 0, "update": 0, "delete": 0}

for rc in plan["resource_changes"]:
    for action in rc["change"]["actions"]:
        if action in counts:
            counts[action] += 1

print(f"Add: {counts['create']}, Change: {counts['update']}, Destroy: {counts['delete']}")