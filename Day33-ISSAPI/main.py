import requests, smtplib, time
from datetime import datetime
from config import my_email, my_pass

def send_iss_email(recepient):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        print(f'Sending Message...')
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recepient, 
                            msg=f'Subject:ISS Overhead\n\nLook up!')

MY_LAT = 23.032000 # Your latitude
MY_LONG = 113.118060 # Your longitude

def check_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    lat_diff = abs((MY_LAT - iss_latitude))
    long_diff = abs((MY_LONG - iss_longitude))
    print(lat_diff)
    print(long_diff)
    if lat_diff <= 5 and long_diff <= 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    if time_now < sunrise and time_now > sunset:
        return True
    return False

while True:
    time.sleep(60)
    if check_overhead:
        if is_night:
            send_iss_email('morrisseyjsean@protonmail.com')
    





