import requests
print("initializing")
response = requests.post(
    "https://ntfy.sh/test_alerts",
    data="Hi gm",
    headers={
        "Title": "Test",
        "Priority": "1"
    },
    timeout=10
)
response.raise_for_status()
