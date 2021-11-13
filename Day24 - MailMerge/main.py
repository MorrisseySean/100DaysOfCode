import os
# Get the base path to this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Variables to store the contents of the two files
namelist = []
letter_text = ""

# Read each line of the text and place it in a list
with open(THIS_FOLDER + '/Input/Names/invited_names.txt') as file:
    namelist = file.readlines()
# Read the letter text to a variable
with open(THIS_FOLDER + '/Input/Letters/starting_letter.txt') as file:
    letter_text = file.read()

for name in namelist:
    # Clear the newline char from the name
    name = name.strip('\n')
    # Create a copy of the letter text with the name correctly replaced.
    output = letter_text.replace('[name]', name)
    # Write the letter text to a new file
    with open(THIS_FOLDER + '\Output\ReadyToSend\letter_for_' + name, mode='w') as file:
        file.write(output)

