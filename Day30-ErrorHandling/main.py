from tkinter import *
from tkinter import messagebox
import os, password_generator, pyperclip, json

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
            # Generate dictionary with data
            new_data = {
                website: {
                    "username":username, 
                    "password":password,
                }
            }
            write_data(new_data)
            # Delete the inputs to be ready for another round
            website_input.delete(0, END)
            password_input.delete(0, END)
        
def write_data(new_data):
        try:
            # Open file and read data inside file
            with open(THIS_FOLDER + '\data.json', mode='r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            # If there is no data, create new data
            data = new_data
        finally:
            # Write the data to the file        
            with open(THIS_FOLDER + '\data.json', mode='w') as file:
                json.dump(data, file, indent=4)

# ---------------------------- READ PASSWORD ------------------------------- #
def read_data():
    # Get search term from user input
    search_term = website_input.get()
    title = 'Error'
    # Validation presence check for input 
    if len(search_term) == 0:
        messagebox.showwarning('Warning', 'Please enter a website name.')
    else:
        try:
            # Open file and read data to dictionary 'data'
            with open(THIS_FOLDER + '\data.json', mode='r') as file:
                data = json.load(file)
        except FileNotFoundError:
            # If no file found, output error message
            output = 'No information found in database!'
        else:
            if search_term in data:
                # Search for information of search term in dictionary
                password = data[search_term]['password']
                username = data[search_term]['username']
                # If information found, copy password and output information
                pyperclip.copy(password)
                title = 'Your Information'
                output = f'Website: {search_term}\nUsername: {username}\nPassword: {password}\nPassword copied to clipboard!'
            else:
                # If no information found in dictionary, output error message
                output = f'{search_term} not found in database!'                
        finally: 
            # Show the message to the user
            messagebox.showinfo(title, output)

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
search_btn = Button(text='Search', font=FONT, command=read_data)

# Position screen elements
canvas.grid(row=0, column=0, columnspan=3)
website_label.grid(row=1, column=0, sticky=(E))
website_input.grid(row=1, column=1, sticky=(W, E), pady=5)
search_btn.grid(row=1, column=2, padx=(10, 0), sticky=(W, E))
username_label.grid(row=2, column=0, sticky=(E))
username_input.grid(row=2, column=1, columnspan=2, sticky=(W, E), pady=5)
password_label.grid(row=3, column=0, sticky=(E))
password_input.grid(row=3, column=1, pady=5)
generate_btn.grid(row=3, column=2, padx=(10, 0), sticky=(E))
save_btn.grid(row=4, column=1, columnspan=3, sticky=(W, E), pady=5)


window.mainloop()