import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)

response2= requests.get("https://api.github.com/users/torvalds")
print("public_repos", response2.json()["public_repos"])