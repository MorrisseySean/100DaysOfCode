import os, pandas, random
from tkinter import *

# --- CONSTANTS --- #
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_COLOR = "#B1DDC6"
FONT_COLORS = ['white', 'black']
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 525
SMALL_FONT = ('Arial', 40, 'italic')
LARGE_FONT = ('Arial', 60, 'bold')

timer = None
counter = 0

# --- Load Data --- #
try: 
    data = pandas.read_csv(THIS_FOLDER + '/data/chinese_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv(THIS_FOLDER + '/data/chinese_eng.csv')
finally: 
    chinese_dict = data.to_dict(orient='records')
    current_card = random.choice(chinese_dict)

# --- Generate New Card --- #
def new_card():
    global current_card
    # Change the card back
    canvas.itemconfig(card_image, image=card_images[counter%2])
    if counter%2 == 0:
        # Choose a random card
        current_card = random.choice(chinese_dict)    
        canvas.itemconfig(language_text, text='Chinese', fill=FONT_COLORS[counter%2])
        canvas.itemconfig(word_text, text=current_card["Chinese Char"], fill=FONT_COLORS[counter%2])
        canvas.itemconfig(pinyin_text, text='', fill=FONT_COLORS[counter%2])
    else:
        # Show other face        
        canvas.itemconfig(language_text, text='English', fill=FONT_COLORS[counter%2])
        canvas.itemconfig(word_text, text=current_card['English Translation'], fill=FONT_COLORS[counter%2])
        canvas.itemconfig(pinyin_text, text=current_card['Pinyin'], fill=FONT_COLORS[counter%2])

# --- Remove Words --- #
def remove_card():
    global current_card, counter
    chinese_dict.remove(current_card)
    new_word()

# --- Timer --- #
def change_card():
    global counter, timer
    new_card()
    counter += 1
    timer = window.after(5000, change_card)

# --- Next Word Func --- #
def new_word():
    global counter    
    window.after_cancel(timer)
    counter = 0
    change_card()

# --- UI --- #
# Window setup
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Load images
card_front = PhotoImage('Card Front', file=THIS_FOLDER + '/images/card_front.png')
card_back = PhotoImage('Card Back', file=THIS_FOLDER + '/images/card_back.png')
card_images = [card_back, card_front]
right_image = PhotoImage('Right', file=THIS_FOLDER + '/images/right.png')
wrong_image = PhotoImage('Wrong', file=THIS_FOLDER + '/images/wrong.png')

# Generate the canvas
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=card_front)
language_text = canvas.create_text(400, 150, text='Chinese', font=SMALL_FONT)
word_text = canvas.create_text(400, 260, text='wo', font=LARGE_FONT)
pinyin_text = canvas.create_text(400, 340, text='wo', font=SMALL_FONT)

# Buttons
right_btn = Button(image=right_image, command=remove_card, highlightthickness=0)
wrong_btn = Button(image=wrong_image, command=new_word, highlightthickness=0)

# Place items in window
canvas.grid(row=0, column=0, columnspan=2)
right_btn.grid(row=1, column=0)
wrong_btn.grid(row=1, column=1)

change_card()
window.mainloop()
output = pandas.DataFrame(chinese_dict)    
output.to_csv(THIS_FOLDER + '/data/chinese_to_learn.csv', index=False)
