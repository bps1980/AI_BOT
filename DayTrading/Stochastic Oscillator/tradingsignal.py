df['trade_signal'] = 0
df['previous_%K'] = df['%K'].shift(1)

# Bullish signal
df.loc[(df['previous_%K'] < 20) & (df['%K'] > 20), 'trade_signal'] = 1

# Bearish signal
df.loc[(df['previous_%K'] > 80) & (df['%K'] < 80), 'trade_signal'] = -1
