import datetime, pandas, random, os, smtplib
from data import my_email, my_pass

def send_bday_email(letter, recepient):
    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        print(f'Sending Message:\n{letter}')
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recepient, 
                            msg=f'Subject:Happy Birthday\n\n{letter}')


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
now = datetime.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv(THIS_FOLDER+'/birthdays.csv')
birthday_dict = {(row.month, row.day) : row for (index, row) in data.iterrows()}
# If there's a birthday in the list
if today in birthday_dict:
    person = birthday_dict[today]['name']
    email = birthday_dict[today]['email']
    # Pick a random letter
    letter = 'letter_' + str(random.randint(1, 3)) + '.txt'
    # Open the letter and replace the text
    with open(THIS_FOLDER + '/letter_templates/' + letter) as file:
        letter_text = file.read()
        output = letter_text.replace('[NAME]', person)
    # Send the letter text in an email
    send_bday_email(output, email)





