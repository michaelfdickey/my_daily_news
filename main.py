import os
import requests

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
#print(api_key)

#Define the search parameters
def get_news(topic, from_date, to_date, language='en', api_key=api_key):
    """
    gets news results from newsapi.org
    """
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    #print("url is: ", url)
    request_result = requests.get(url)
    content = request_result.json()
    #print(content)
    
    articles = content['articles']
    
    #for article in articles:
    #    print("> ", article['title'])   

    for i in range(len(content['articles'])):
        print('> ', content['articles'][i]['title'])
        
get_news(topic='covid china', from_date='2022-6-27', to_date='2022-6-28')
#print(topic_search_result)

