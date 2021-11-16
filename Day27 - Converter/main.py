from tkinter import *

CONVERSION_RATE = 0.14

def convert():
    if input.get():
        value['text'] = int(input.get()) * CONVERSION_RATE
    else:
        value['text'] = 0

# Setup window
window = Tk()
window.title("Converter")
window.config(padx=20, pady=20)

# --- Labels --- #
cny = Label(text='CNY', font=('Calibri', 12, 'bold'))
eur = Label(text='EUR', font=('Calibri', 12, 'bold'))
is_equal = Label(text='is equal to', font=('Calibri', 12, 'bold'))
value = Label(text='0', font=('Calibri', 12, 'bold'))
cny.grid(row=0, column=2)
eur.grid(row=1, column=2)
is_equal.grid(row=1, column=0)
value.grid(row=1, column=1)

# Input box
input = Entry(width=10)
input.grid(row=0, column=1)

# Button
button = Button(text='Convert', command=convert)
button.grid(row=2, column=1)



window.mainloop()