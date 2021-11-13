import os, pandas
from numpy import NAN
# Get the base path to this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# --- Test Samples --- #
# data = pandas.read_csv(THIS_FOLDER + "/weather_data.csv")

# maxTemp = data['temp'].max()
# maxTempDay = data[data.temp == maxTemp]
# print("Maximum Temperature")
# print(maxTempDay)

# monday = data[data.day == 'Monday']
# temp_in_f = (int(monday.temp) * 9/5 + 32)
# print(f"Monday was {temp_in_f} degrees fahrenheit")
# --- End Test Samples --- #

# Read data using pandas library
data = pandas.read_csv(THIS_FOLDER + "/squirrel_census.csv")
# Find the list of fur colors present in the list
fur_colors = data['Primary Fur Color'].drop_duplicates().tolist()
# Remove the no value entry
fur_colors.remove(NAN)
# Create a list with an empty count key
output = {'Fur Color': fur_colors, 'Count':[]}
# For each color, count the amount of instances 
for color in fur_colors:
    output['Count'].append(len(data[data['Primary Fur Color'] == color]))
# Process the data through pandas and output a csv file with the data
data = pandas.DataFrame(output)
data.to_csv(THIS_FOLDER + '/squirrel_fur_count.csv')
