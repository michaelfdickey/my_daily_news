import requests

"""
v 1.0
get api key from secret
make a list of topics
generate an email with clickable urls
send email to recipient
news comes from https://newsapi.org/
"""

#Define the search parameters
def get_news(topic, from_date, to_date, language='en', api_key='get from secret'):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
    request_result = requests.get(url)
    content = request_result.json()
    articles = content['articles']
    for article in articles:
        print("> ", article['title'])   
        
topic_search_result = get_news(topic='covid china', from_date='2022-6-27', to_date='2022-6-28')
#print(topic_search_result)