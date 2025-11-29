import requests

# Download this web page
response = requests.get("https://api.github.com")
print(response.status_code) # If it works, it should print 200 resp. code