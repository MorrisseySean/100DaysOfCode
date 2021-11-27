import requests, smtplib
from data import *

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Gets news about a specific company and returns a message with the top 3 headlines and briefs
def get_news(company):
    news_endpoint = f"https://newsapi.org/v2/everything?q={company}&from=2021-11-24&sortBy=popularity&apiKey={news_key}"
    response = requests.get(news_endpoint)
    data = response.json()
    # Get the headlines and brief description information from the data
    summary= [{'headline': article['title'], 'info': article['description'], 'url': article['url']} for article in data['articles']]
    
    # Return the top 3 articles from the data
    message = ""
    for news in summary[:3]:
        message +=f"""
        Headline: <a href='{news['url']}'>{news['headline']}</a>\n
        Brief: {news['info']} 
        """
    return message
    

def send_notification(subject, message, recepient):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=recepient, 
                            msg=f'Subject:{subject}\n\n{message}')


alpha_endpoint = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&outputsize=compact&apikey={alpha_key}"
response = requests.get(alpha_endpoint)
data = response.json()['Time Series (Daily)']
daily_data = [value for (date, value) in data.items()]
tracked = []
# Grab the close values for the past 2 days
for day in daily_data[:2]:
    tracked.append(float(day['4. close']))
        
# Get the percentage difference between the two values
difference = ((tracked[0] - tracked[1]) / tracked[1] ) * 100
# If the difference is greater than 5%, grab the 3 news articles and email them
if abs(difference) >= 5:
    # Get the subject line 
    if difference < 0:
        difference_text = f"DOWN {round(difference, 2)}%"
    else:
        difference_text = f"UP {round(difference, 2)}%"
    subject = f"{STOCK}: {difference_text}"
    # Get the news related to the company
    news = get_news(COMPANY_NAME)
    # Send an email
    send_notification(subject, news, 'morrisseyjsean@protonmail.com')




