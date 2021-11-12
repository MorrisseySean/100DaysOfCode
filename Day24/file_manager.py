import os
# Get the base path to this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Open the file in python, and close it when done
# Modes r - readonly, w - write (overwrite contents), a - append
with open(THIS_FOLDER + "\my_file.txt", mode='a') as file:
    file.write("Sit amet dolor Lorem")