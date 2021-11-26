import requests
from twilio.rest import Client
from data import twil_key, ow_key
TWIL_ID = 'AC1c6bb2dc46d1ffa577506b128e0fa791'
TWIL_AUTH = twil_key
API_KEY = ow_key
MY_LAT = 23.032000 # Your latitude
MY_LONG = 113.118060 # Your longitude

# Set request parameters
api_url = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid":API_KEY,
    "exclude":'current,minutely,daily'
}

# Send request to api
response = requests.get(api_url, params=weather_params)
# Get the json data
data = response.json()
# Look at only the next 12 hours
hourly = data['hourly'][:12]

# Will rain flag
will_rain = False

# For each hour in our data
for hour in hourly:
    # Check all weather conditions (Usually only 1)
    for weather in hour['weather']:
        # If the weather code is raining/snowing set flag to true
        if weather['id'] < 700:
            will_rain = True

if will_rain:
    client = Client(TWIL_ID, TWIL_AUTH)
    message_text = "Bring an umbrella. It will rain in the next 12 hours."
    message = client.messages \
                .create(
                     body=message_text,
                     from_='+12059463771',
                     to='+8618529458254'
                 )
    
    print(message.sid)
else:
    print("All Clear")

