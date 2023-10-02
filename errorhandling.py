import ccxt
import sys
import smtplib
from email.message import EmailMessage

# Initialization
exchange = ccxt.binanceus({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
})

# Email settings for notification
EMAIL = {
    'sender': 'youremail@gmail.com',
    'receiver': 'youremail@gmail.com',
    'subject': 'Trading Bot Alert',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'login': 'youremail@gmail.com',
    'password': 'yourpassword'
}

def send_email_notification(message):
    """ Send an email to the operator """
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = EMAIL['subject']
    msg['From'] = EMAIL['sender']
    msg['To'] = EMAIL['receiver']
    
    try:
        server = smtplib.SMTP(EMAIL['smtp_server'], EMAIL['smtp_port'])
        server.starttls()
        server.login(EMAIL['login'], EMAIL['password'])
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def fetch_data(symbol, lookback=500):
    try:
        return exchange.fetch_ohlcv(symbol, '1d', limit=lookback)
    except ccxt.NetworkError as e:
        print(f'fetch_data failed due to a network error: {e}')
        send_email_notification(f'fetch_data failed due to a network error: {e}')
        sys.exit()
    except ccxt.ExchangeError as e:
        print(f'fetch_data failed due to exchange error: {e}')
        send_email_notification(f'fetch_data failed due to exchange error: {e}')
        sys.exit()
    except Exception as e:
        print(f'fetch_data failed due to {e}')
        send_email_notification(f'fetch_data failed due to {e}')
        sys.exit()

def trading_logic(data):
    # ... Your trading logic here

def execute_trade(action):
    try:
        if action == 'buy':
            order = exchange.create_market_buy_order('BTC/USDT', 0.01)
        elif action == 'sell':
            order = exchange.create_market_sell_order('BTC/USDT', 0.01)
    except ccxt.InsufficientFunds as e:
        print(f'Insufficient funds to complete the trade: {e}')
        send_email_notification(f'Insufficient funds to complete the trade: {e}')
    except ccxt.InvalidOrder as e:
        print(f'Invalid order: {e}')
        send_email_notification(f'Invalid order: {e}')
    except ccxt.NetworkError as e:
        print(f'Trade execution failed due to a network error: {e}')
        send_email_notification(f'Trade execution failed due to a network error: {e}')
    except ccxt.ExchangeError as e:
        print(f'Trade execution failed due to exchange error: {e}')
        send_email_notification(f'Trade execution failed due to exchange error: {e}')
    except Exception as e:
        print(f'Trade execution failed due to {e}')
        send_email_notification(f'Trade execution failed due to {e}')

def main():
    data = fetch_data('BTC/USDT')
    action = trading_logic(data)
    execute_trade(action)

if __name__ == "__main__":
    main()
