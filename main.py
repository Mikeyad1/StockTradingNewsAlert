import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "your_stock_api_key"
NEWS_API_KEY = "your_news_api_key"

# Email configuration
MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_email_password"
TO_EMAIL = "recipient_email@example.com"


def send_email(message_content):
    msg = MIMEMultipart()
    msg['From'] = MY_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = "Stock Update"
    msg.attach(MIMEText(message_content, 'plain'))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(MY_EMAIL, PASSWORD)
        server.send_message(msg)


def get_stock_data():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(STOCK_ENDPOINT, params=stock_params)
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    return data_list


def get_news():
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
        for article in articles
    ]
    return "\n\n".join(formatted_articles)


# Main logic
stock_data = get_stock_data()
yesterday_data = stock_data[0]
day_before_yesterday_data = stock_data[1]

yesterday_closing_price = float(yesterday_data["4. close"])
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = "🔺" if difference > 0 else "🔻"
diff_percent = round((difference / yesterday_closing_price) * 100)

if abs(diff_percent) > 0.01:
    message_content = get_news()
    send_email(message_content)
else:
    print("No significant change in stock price.")
