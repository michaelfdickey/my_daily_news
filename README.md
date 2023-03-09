# my_daily_news

Program that emails you a clean text only list of news by topic on a scheduled interval, daily, weekly, monthly. 

## notes

getting actions secrets and using them in codespace env:
https://github.com/michaelfdickey/CIS553-CurrencyConverter-statuschecks
https://github.com/michaelfdickey/CIS553-CurrencyConverter

```
import os
# reference codespaces secret
APIKEY = os.getenv('API_KEY')
```

To use:

1) create API key for news from https://newsapi.org/ and enter the API key as an Actions secret called `APIKEY` just to run the program and as a codespaces secret `APIKEY` if you want to develop
2) create an API for weather at https://openweathermap.org/api and create `API_KEY_WEATHER`
3) create a gmail app password and put it in a secret `GMAIL_APP_PWD`
