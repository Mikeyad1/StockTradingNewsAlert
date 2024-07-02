
# Stock News Email Notifier

This Python script tracks daily stock prices and sends email notifications when significant changes occur for a specified company (e.g., Tesla Inc). It utilizes Alpha Vantage for stock data and NewsAPI for relevant news updates.

# Features:
- Retrieves daily stock prices and calculates percentage changes.
- Fetches latest news articles related to the company.
- Sends concise email notifications with stock updates and news headlines.

# Setup:
1. Replace placeholders for API keys (`STOCK_API_KEY`, `NEWS_API_KEY`) and email credentials (`MY_EMAIL`, `PASSWORD`, `TO_EMAIL`) with your own.
2. Install required Python libraries:
   ```
   pip install requests smtplib email
   ```
3. Run the script to monitor and receive updates on stock and news changes.


