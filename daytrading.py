import ccxt
import numpy as np
import time

api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

exchange = ccxt.binanceus({
    'apiKey': api_key,
    'secret': api_secret,
    'rateLimit': 1100,  # Slightly higher than the default to be safe
    'timeout': 30000,  # Timeout for requests
})

symbol = 'BTC/USD'
base_currency = symbol.split('/')[0]
quote_currency = symbol.split('/')[1]
short_window = 50
long_window = 200
stop_loss_percentage = 0.95

def get_moving_average(window, prices):
    return sum(prices[-window:]) / window

def calculate_rsi(period, prices):
    deltas = np.diff(prices)
    seed = deltas[:period+1]
    up = seed[seed >= 0].sum()/period
    down = -seed[seed < 0].sum()/period
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:period] = 100. - 100./(1.+rs)

    for i in range(period, len(prices)):
        delta = deltas[i - 1]
        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(period-1) + upval)/period
        down = (down*(period-1) + downval)/period
        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi[-1]

def create_order(side, amount, price):
    try:
        order = exchange.create_market_order(symbol, side, amount, price)
        return order
    except Exception as e:
        print(f"Error creating order: {str(e)}")
        return None

def check_stop_loss(current_price, buy_price):
    return current_price <= buy_price * stop_loss_percentage

def main():
    buy_price = None
    has_position = False

    downtime_count = 0  # Count downtime occurrences
    MAX_DOWNTIME = 3  # Stop after 3 continuous downtimes

    while True:
        if downtime_count >= MAX_DOWNTIME:
            print("Max downtime reached. Exiting...")
            break

        try:
            candles = exchange.fetch_ohlcv(symbol, '5m', rateLimit=True)
            close_prices = np.array([candle[4] for candle in candles])

            ma_short = get_moving_average(short_window, close_prices)
            ma_long = get_moving_average(long_window, close_prices)
            rsi = calculate_rsi(14, close_prices)

            balance = exchange.fetch_balance()['total'][base_currency]
            has_position = balance and balance > 0.001

            current_price = close_prices[-1]

            if has_position and buy_price and check_stop_loss(current_price, buy_price):
                print("Stop-loss triggered. Selling...")
                create_order('sell', balance, None)
                has_position = False
                buy_price = None
                downtime_count = 0
                continue

            if ma_short > ma_long and not has_position and rsi < 30:
                order = create_order('buy', None, exchange.fetch_balance()['total'][quote_currency])
                if order:
                    buy_price = order['price']
                    downtime_count = 0
            elif ma_short < ma_long and has_position and rsi > 70:
                create_order('sell', balance, None)
                buy_price = None
                downtime_count = 0

            time.sleep(exchange.rateLimit / 1000)  # Respect the rate limit

        except ccxt.RequestTimeout as e:
            print(f"Request Timeout: {e}")
            downtime_count += 1
            time.sleep(10)
        except ccxt.ExchangeNotAvailable as e:
            print(f"Exchange Not Available: {e}")
            downtime_count += 1
            time.sleep(10)
        except ccxt.ExchangeError as e:
            print(f"Exchange Error: {e}")
            downtime_count += 1
            time.sleep(10)
        except Exception as e:
            print(f"Error: {str(e)}")
            downtime_count += 1
            time.sleep(10)

if __name__ == '__main__':
    main()