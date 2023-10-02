import ccxt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Initialization
exchange = ccxt.binanceus({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
})

model = RandomForestRegressor()

def fetch_data(symbol, lookback=500):
    return exchange.fetch_ohlcv(symbol, '1d', limit=lookback)

def feature_engineering(data):
    closes = [x[4] for x in data]
    volumes = [x[5] for x in data]

    # Use past prices and volumes as features; this is a simple example.
    # In reality, you'd want to use more complex features, maybe derived from technical indicators.
    features = [{'close': closes[i], 'volume': volumes[i]} for i in range(len(data))]

    # Use next day's price as target for regression.
    targets = closes[1:]

    return features[:-1], targets

def train_model(features, targets):
    X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2)
    model.fit(X_train, y_train)
    print("Model Score:", model.score(X_test, y_test)) # A simple accuracy measure; consider other metrics too

def predict_next_movement(features):
    return model.predict([features[-1]])[0]  # Predicting the next movement based on the latest feature

def trading_logic(prediction, current_price):
    if prediction > current_price:
        return 'buy'
    else:
        return 'sell'

def execute_trade(action):
    if action == 'buy':
        # Dummy order; in reality, you'd need to specify more details like order size, price, etc.
        order = exchange.create_market_buy_order('BTC/USDT', 0.01) # Small amount for demonstration
    elif action == 'sell':
        order = exchange.create_market_sell_order('BTC/USDT', 0.01)

def main():
    data = fetch_data('BTC/USDT')
    features, targets = feature_engineering(data)
    train_model(features, targets)

    latest_feature = features[-1]
    current_price = latest_feature['close']
    prediction = predict_next_movement(features)
    
    action = trading_logic(prediction, current_price)
    execute_trade(action)

if __name__ == "__main__":
    main()
