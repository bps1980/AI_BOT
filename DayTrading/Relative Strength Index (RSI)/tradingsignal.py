df['trade_signal'] = 0
df.loc[df['rsi'] < 30, 'trade_signal'] = 1  # potential buy signal
df.loc[df['rsi'] > 70, 'trade_signal'] = -1  # potential sell signal
