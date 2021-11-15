from tkinter import *

window = Tk()
window.title("Super Window")
window.minsize(width=600, height=400)

# Tkinter Label
my_label = Label(text='My Label', font=('Arial', 24, 'bold'))
my_label.pack()

def button_clicked():
    my_label['text'] = input.get()

input = Entry(width=10)
input.pack()

button = Button(text='Confirm', command=button_clicked)
button.pack()



window.mainloop()