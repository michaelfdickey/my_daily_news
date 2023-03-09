import os
import requests
import time
from datetime import timedelta
from datetime import date
from datetime import datetime 
import yagmail


"""
v 1.0
get api key from secret
make a list of topics
generate an email with clickable urls
send email to recipient
news comes from https://newsapi.org/
"""

# reference codespaces secret
api_key = os.getenv('APIKEY')
api_key_weather = os.getenv('API_KEY_WEATHER')
email_password = os.getenv('GMAIL_APP_PWD')
#print(api_key)
#print(api_key_weather)
#print(email_password)

# email info
sender = 'mfd.oldphones@gmail.com'
receiver = 'matus1976@gmail.com'
subject = 'my dail news'
content = ''

#Define the search parameters
def get_news(topic, from_date, to_date, language='en', api_key=api_key, content=content):
    """
    gets news results from newsapi.org
    """
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    #print("url is: ", url)
    request_result = requests.get(url)
    content_news = request_result.json()
    #print(content)
    
    articles = content_news['articles']
    
    #print("content is: ", content)
    for article in articles:
        print("> ", article['title'])
        content = content + "> " + article['title'] + "\n"
        print("   ", article['url'])
        content = content + "  " + article['url'] + "\n"
    #print("content is now: ", content)

    #for i in range(len(content['articles'])):
    #    print('> ', content['articles'][i]['title'])

    return content
        
def get_dates():
    today = date.today()
    #print(" today is: ", today)
    #print(type(today))
    today_string = str(today)
    #print(repr(today_string))
    
    from_duration = timedelta(days = 1)             #change days here to update your from date
    #print(" from_duration is: ", from_duration)
    from_date = today - from_duration
    #print(" from_date is: ", from_date)
    from_string = str(from_date)
    #print(" from string is: ", from_string)
    
    from_and_to_dates = [today_string, from_string]

    return from_and_to_dates


def get_weather(api_key_weather):
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Kent,wa,us&APPID={api_key_weather}&units=imperial'
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    return(content)

def get_forecast(api_key_weather):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=Kent,wa,us&cnt=8&APPID={api_key_weather}&units=imperial'
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    return(content)

weather_content = get_weather(api_key_weather)
forecast = get_forecast(api_key_weather)
from_and_to_dates = get_dates()

topics = ['covid china', 'nuclear energy', 'spacex', 'james webb', 'nuclear fusion', 'inflation', 'real estate', 'sp 500', 'blue origin', 'seattle']

#build temperature display lists
todays_temps = []
for n in range(8):
    #print(n, forecase['list'][n]['main']['temp'])
    todays_temps.append(forecast['list'][n]['main']['temp'])

todays_weather = []
for n in range(8):
    #print(n, forecast['list'][n]['weather'][0]['description'])
    todays_weather.append(forecast['list'][n]['weather'][0]['description'])

forecast_hours = []

for n in range(8):
    #print(n, forecast['list'][n]['dt_txt'])
    forecast_date_time = forecast['list'][n]['dt_txt']
    forecast_hour = forecast_date_time[11:16]
    #print(forecast_hour)
    forecast_hours.append(forecast_hour)

### display results  and build conent ###

print(" ")

print("Daily News Delivery for", from_and_to_dates[1])
content = "Daily News Delivery for " + from_and_to_dates[1]

print(" ")
content = content + "\n\n"

print("The current weather for ", (weather_content['name']), "is: ", weather_content['weather']
      [0]['description'], " and a temp of ", weather_content['main']['temp'], " degrees.")
content = content + "The current weather for " + weather_content['name'] + " is: " + weather_content['weather'][0]['description'] + " and a temp of " + str(weather_content['main']['temp']) + " degrees."

print(" ")
content = content + "\n\n"

for n in range(8):
    print(forecast_hours[n], " ", todays_temps[n], " degF, ", todays_weather[n])
    content = content + forecast_hours[n] + " " + str(todays_temps[n]) + " degF, " + todays_weather[n] + "\n"
    #print(" ")

print(" ")
content = content + "\n\n"

for topic in topics:
    print(topic)
    content = content + topic + "\n"
    content = get_news(topic=topic, from_date=from_and_to_dates[1], to_date=from_and_to_dates[0], content=content)
    content = content + "\n"


### create email ###
subject = 'my dail news for ' + from_and_to_dates[1]
print("subject will be: ", subject)

### check contents ###
print("content is: ", content)

### send email ###
yag = yagmail.SMTP(sender,email_password )                      # create an instance of the SMTP object isntance using the SMTP class
yag.send(to=receiver, subject=subject, contents=content)
print("email sent")