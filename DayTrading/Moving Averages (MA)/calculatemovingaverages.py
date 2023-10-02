short_period = 10
long_period = 50

df['short_ma'] = df['close'].rolling(window=short_period).mean()
df['long_ma'] = df['close'].rolling(window=long_period).mean()
