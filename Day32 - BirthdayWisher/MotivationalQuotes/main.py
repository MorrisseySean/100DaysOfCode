import smtplib, datetime, random, os
from data import my_pass, my_email

def send_quote(quote):
    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        print(f'Sending quote:\n{quote}')
        connection.sendmail(from_addr=my_email, 
                            to_addrs='morrisseyjsean@protonmail.com', 
                            msg=f'Subject:Motivational Quote\n\n{quote}')


# Get quotes
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
with open(THIS_FOLDER + "/quotes.txt") as file:
    quotes = file.readlines()

now = datetime.datetime.now()
if now.weekday() == 0:
    send_quote(random.choice(quotes))
else:
    print("It's not Monday")
