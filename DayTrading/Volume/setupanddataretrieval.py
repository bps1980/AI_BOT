import ccxt
import pandas as pd

# Initialize Binance US client
binanceus = ccxt.binanceus({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
})

symbol = 'BTC/USD'
timeframe = '1d'
ohlcv = binanceus.fetch_ohlcv(symbol, timeframe)

df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

