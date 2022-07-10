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