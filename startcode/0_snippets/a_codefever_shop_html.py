import requests
response = requests.get("https://shop.codefever.rocks/")

print(response.text)