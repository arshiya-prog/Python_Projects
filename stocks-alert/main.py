import requests
import os
from datetime import datetime, timedelta
import requests_cache
from smtplib import SMTP
from email.message import EmailMessage

requests_cache.install_cache("stocks_cache")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_vantage_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"tsla",
    "apikey":os.environ.get("alpha_vantage_api"),
}
news_parameters = {
    "q":"Tesla",
    "apiKey":os.environ.get("news_api")
}
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url=ALPHA_VANTAGE_URL, params=alpha_vantage_parameters)
stock_data = response.json()
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

yesterdays_close = float(stock_data["Time Series (Daily)"][yesterday_str]["4. close"])
day_before_yesterdays_close = float(stock_data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])

if yesterdays_close > day_before_yesterdays_close:
    diff = yesterdays_close - day_before_yesterdays_close
    diff_percent = (diff / yesterdays_close) * 100
else:
    diff = day_before_yesterdays_close - yesterdays_close
    diff_percent = (diff / day_before_yesterdays_close) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if diff_percent > 5:
    data = requests.get(url=NEWS_URL, params=news_parameters)
    news_articles = data.json()
    news_list = {
        news_articles["articles"][0]["title"]: news_articles["articles"][0]["description"],
        news_articles["articles"][1]["title"]: news_articles["articles"][1]["description"],
        news_articles["articles"][2]["title"]: news_articles["articles"][2]["description"]
    }

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    with SMTP("smtp.mail.yahoo.com", 587, timeout=30) as connection:
        connection.starttls()
        connection.login(
            user=os.environ.get("email"), 
            password=os.environ.get("password")
        )

        for title, description in news_list.items():
            direction = "🔺" if yesterdays_close > day_before_yesterdays_close else "🔻"

            message = EmailMessage()
            message["Subject"] = "Stocks Alert!"
            message["From"] = os.environ["email"]
            message["To"] = os.environ["to_email"]

            message.set_content(
            f"TSLA: {direction}{diff_percent:.2f}%\n"
            f"Headline: {title or 'No title'}\n"
            f"Brief: {description or 'No description'}",
            charset="utf-8",
        )

        connection.send_message(message)

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

