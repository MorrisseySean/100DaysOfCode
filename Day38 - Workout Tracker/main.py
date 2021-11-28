import requests, datetime, json, os

NUTRITIONIX_ID = "aabb0604"
NUTRITIONIX_KEY = os.environ["NUTRITIONIX_KEY"]
SHEETY_KEY = os.environ['SHEETY_KEY']

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/"

def get_workout_data(message:str, weight:float, height:float, age:int, gender='male') -> dict:
    """ 
    Takes a user message [message] and generates a dict containing time,
    date, exercise, calories spent and duration of exercise using the 
    nutritionix API. 
    """
    # Gender input for nutriotionix only allows two genders, if another is input, assign female as a temporary work around.
    if gender.lower() != "male" or gender.lower() != "female":
        gender = 'female'

    # Get the url for getting the exercise data from a string
    workout_endpoint = "natural/exercise"
    url = nutritionix_endpoint+workout_endpoint
    
    # Generate the headers and params 
    headers = { 
    "x-app-id":NUTRITIONIX_ID,
    "x-app-key":NUTRITIONIX_KEY
    }
    params = {
        "query":message,
        "gender":gender.lower(),
        "weight_kg":weight,
        "height_cm":height,
        "age":age
    }
    
    # Extract the dictionary containing the exercise data
    response = requests.post(url=url, data=params, headers=headers)
    data = response.json()['exercises'][0]
    
    # Get the current date and time
    cur_time = datetime.datetime.now()
    date = cur_time.strftime("%d/%m/%Y")
    time = cur_time.strftime("%X")

    # Prepare and output data
    exercise = {
        "date":date,
        "time":time,
        "exercise":data["name"],
        "duration":data["duration_min"],
        "calories":data["nf_calories"]
    }
    return exercise


def post_workout_data(data:dict):
    """ Posts workout data [data] to a google spreadsheet using Sheety"""
    sheety_endpoint = "https://api.sheety.co/6df1c16ff973894c505e64a79ec29361/workoutTracker/workouts"
    header = {
        "Content-Type":"application/json",
        "Authorization":f"Bearer {SHEETY_KEY}"
    }
    params = {
        "workout": data
    }
    # Convert params to json data
    params = json.dumps(params, indent=4)
    response = requests.post(sheety_endpoint, params, headers=header)
    # Output error code if something went wrong, otherwise output success string
    if response.status_code == 200:
        print(f"Successfully added workout: {data['exercise'].capitalize()}!")
    else:
        print(f"Something went wrong, please try again later.")

# Get user input
message = input("What did you do for your workout?: ")
# Find exercise information
exercise_info = get_workout_data(message, 72, 172, 28)
# If information found process the info to the spreadsheet
if len(exercise_info) > 0:
    post_workout_data(exercise_info)
# Otherwise, output error message.
else: 
    print("Something went wrong. Please try again.")
