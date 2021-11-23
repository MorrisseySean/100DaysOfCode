import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')

# Check for error
response.raise_for_status()

# Get API data
data = response.json()
