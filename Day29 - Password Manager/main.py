from tkinter import *
from tkinter import messagebox
import os, password_generator, pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
BGCOLOR = '#222222'
FONT=('Calibri', 12, 'normal')
CANVAS_SIZE = 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_password():
    new_password = password_generator.generate_password()
    password_input.delete(0, END)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    # Grab the user inputs
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning('Warning', 'Please ensure no entries are blank.')
    else: 
        confirm_message = f'Website: {website}\nUsername: {username}\nPassword: {password}\nIs this information correct?'
        confirm = messagebox.askyesno(title='Confirm', message=confirm_message)
        # Append the inputs to our text file
        if confirm:
            with open(THIS_FOLDER + '\passwords.txt', mode='a') as file:
                file.write(f'{website} | {username} | {password}\n')
            # Delete the inputs to be ready for another round
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=BGCOLOR)

# Load image to a canvas
lock = PhotoImage(file=THIS_FOLDER+'\logo.png')
canvas = Canvas(width=CANVAS_SIZE, height=CANVAS_SIZE, bg=BGCOLOR, highlightthickness=0)
canvas.create_image(CANVAS_SIZE / 2, CANVAS_SIZE / 2, image=lock)

# Input fields w/ labels
website_input = Entry()
website_input.focus()
website_label = Label(text='Website: ', font=FONT, fg='white', background=BGCOLOR)
username_input = Entry()
username_input.insert(0, 'testemail@hmail.com')
username_label = Label(text='Email/Username: ', font=FONT, fg='white', background=BGCOLOR)
password_input = Entry(width=32)
password_label = Label(text='Password: ', font=FONT, fg='white', background=BGCOLOR)

# Buttons
generate_btn = Button(text='Generate Password', font=FONT, command=new_password)
save_btn = Button(text='Add', font=FONT, command=save_data)

# Position screen elements
canvas.grid(row=0, column=0, columnspan=3)
website_label.grid(row=1, column=0, sticky=(E))
website_input.grid(row=1, column=1, columnspan=2, sticky=(W, E), pady=5)
username_label.grid(row=2, column=0, sticky=(E))
username_input.grid(row=2, column=1, columnspan=2, sticky=(W, E), pady=5)
password_label.grid(row=3, column=0, sticky=(E))
password_input.grid(row=3, column=1, pady=5)
generate_btn.grid(row=3, column=2, padx=(10, 0), sticky=(E))
save_btn.grid(row=4, column=1, columnspan=3, sticky=(W, E), pady=5)


window.mainloop()