import requests
import os
from datetime import datetime, timedelta
import requests_cache

requests_cache.install_cache("stocks_cache")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"tsla",
    "apikey":os.environ.get("alpha_vantage_api"),
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response = response.json()
todays_date = datetime.today().date()
# weekdays_list = [0, 1, 2, 3, 4]

if 1 < todays_date.weekday() < 6:
    yesterday = todays_date - timedelta(1)
    day_before_yesterday = todays_date - timedelta(2)
    yesterday_str = str(yesterday)
    day_before_yesterday_str = str(day_before_yesterday)
elif todays_date.weekday() == 0:
    yesterday = todays_date - timedelta(3)
    day_before_yesterday = todays_date - timedelta(4)
    yesterday_str = str(yesterday)
    day_before_yesterday_str = str(day_before_yesterday)
elif todays_date.weekday() == 1:
    yesterday = todays_date - timedelta(1)
    day_before_yesterday = todays_date - timedelta(3)
    yesterday_str = str(yesterday)
    day_before_yesterday_str = str(day_before_yesterday)
elif todays_date.weekday() == 6:
    yesterday = todays_date - timedelta(2)
    day_before_yesterday = todays_date - timedelta(3)
    yesterday_str = str(yesterday)
    day_before_yesterday_str = str(day_before_yesterday)

# print(type(response["Weekly Adjusted Time Series"]))
# print(type(yesterday), type(day_before_yesterday))
# yesterday = todays_date - timedelta(3)
# print(yesterday.weekday())

# print(yesterday.day, day_before_yesterday.day)
print(response)
# yesterdays_close = response["Time Series (Daily)"][yesterday]
# day_before_yesterdays_close = response["Time Series (Daily)"][day_before_yesterday]
# print(yesterdays_close, day_before_yesterdays_close)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

