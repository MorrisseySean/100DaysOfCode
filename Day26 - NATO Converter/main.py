import pandas, os
# Get the base path to this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Create a dictionary from the csv file with the format {letter: code}
data = pandas.read_csv(THIS_FOLDER + '/nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a sentence that the user inputs.
def generate_phoenetic():
    user_word = input("Please enter a word: ")
    try:
        output_code = [nato_dict[letter] for letter in user_word.upper()]
    except KeyError:
        print("Sorry, please enter only letters.")
    else:
        print(output_code)
    finally:
        generate_phoenetic()

try:
    generate_phoenetic()
except KeyboardInterrupt:
    print("\nGoodbye!")