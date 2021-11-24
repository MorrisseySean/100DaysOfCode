import requests

response = requests.get(url='https://opentdb.com/api.php?amount=20&type=boolean')
data = response.json()
question_data = data['results']

