short_window = 12
long_window = 26
signal_window = 9

# MACD line
df['ema12'] = df['close'].ewm(span=short_window, adjust=False).mean()
df['ema26'] = df['close'].ewm(span=long_window, adjust=False).mean()
df['macd'] = df['ema12'] - df['ema26']

# Signal line
df['signal'] = df['macd'].ewm(span=signal_window, adjust=False).mean()

# Histogram (optional, but useful for visualization)
df['histogram'] = df['macd'] - df['signal']
