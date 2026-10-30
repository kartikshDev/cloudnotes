import json , subprocess

out = subprocess.run(["terraform", "output", "-json"], capture_output=True, text=True)
outputs = json.loads(out.stdout)
print(outputs["url"]['value'])

import urllib.request
resp = urllib.request.urlopen(outputs["url"]["value"])
print("Status:", resp.status)