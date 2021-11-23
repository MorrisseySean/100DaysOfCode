from tkinter import *
import requests, os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
def get_quote():
    # Retrieve the quote from the internet
    response = requests.get(url='https://api.kanye.rest')
    data = response.json()
    quote = data['quote']

    # Change font size to fit text in box
    font=("Arial", 30, "bold")
    if len(quote) > 100:
        font=("Arial", 16, "bold")
    elif len(quote) > 50:
        font=("Arial", 22, "bold")
    # Update the text    
    canvas.itemconfig(quote_text, text=data['quote'], font=font) 


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=THIS_FOLDER +"/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=THIS_FOLDER + "/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()