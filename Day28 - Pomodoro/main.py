from tkinter import *
import os
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = '✔'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text='00:00', fill='white')
    title.config(fg=GREEN)
    progress.config(text='')
    window.after_cancel(timer)    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, progress
    reps+=1
    color = GREEN
    secs = 60
    if reps%8 == 0:
        secs*= LONG_BREAK_MIN
        color=RED
    elif reps%2 == 0:
        secs *= SHORT_BREAK_MIN
        color = PINK
    else:
        secs *= WORK_MIN
    title.config(fg=color)

    # Bring window in to focus
    window.lift()
    window.attributes('-topmost',True)
    window.focus_force()
    window.after_idle(window.attributes,'-topmost',False)

    tick(secs, color)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def tick(counter, timecolor):
    global timer
    # Format to look like a timer
    minutes = floor(counter/60)
    seconds = round(counter%60)
    if seconds < 10: 
        seconds = '0' + str(seconds)
    
    # Change the text on the timer
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}', fill=timecolor)
    # Only tick if counter is more than 0
    if counter > 0:
        timer = window.after(1000, tick, counter - 1, timecolor)
    else:
        checks = ''
        for _ in range(floor((reps/2) % 4)):
            checks += TICK_MARK
        progress.config(text=checks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Title text
title = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
# Progress label
progress = Label(text='', font=(FONT_NAME, 20, 'normal'), bg=YELLOW, fg=GREEN)
# Load tomato image to a var
tomato = PhotoImage(file=THIS_FOLDER + '/tomato.png')
# Create a new canvas to draw a layered image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 135, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
# -- Buttons -- #
startbtn = Button(text='Start', command=start_timer)
resetbtn = Button(text='Reset', command=reset_timer)

# Position elements on the screen
title.grid(column=1, row=0)
startbtn.grid(column=0, row = 3)
resetbtn.grid(column=2, row=3)
canvas.grid(column=1, row=1, rowspan=2)
progress.grid(column=1, row=4)

window.mainloop()
