import urllib.request, time, sys

url = "https://www.google.com"

for attempt in range(1, 4):
    try:
        resp = urllib.request.urlopen(url, timeout=5)
        if resp.status == 200:
            print("UP on attempt", attempt)
            sys.exit(0)
    except Exception as e:
        print("Attempt", attempt, "failed:", e)
        time.sleep(5)

print("DOWN after 3 attempts")
sys.exit(1)