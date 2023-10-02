df['signal'] = 0

# Bullish crossover
df.loc[df['short_ma'] > df['long_ma'], 'signal'] = 1
# Bearish crossover
df.loc[df['short_ma'] < df['long_ma'], 'signal'] = -1
# Price above short MA
df.loc[df['close'] > df['short_ma'], 'signal'] = 1
# Price below short MA
df.loc[df['close'] < df['short_ma'], 'signal'] = -1
