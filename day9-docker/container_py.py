import subprocess, json, sys
container_info = subprocess.run(["docker", "ps", "--format", "{{json .}}"], capture_output= True, text=True)
count = 0
for line in container_info.stdout.splitlines():
    c = json.loads(line)
    print(c['Names'], c['Status'], c['State'])
    count += 1

print(f"Running containers: {count}")


