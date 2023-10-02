df['trade_signal'] = 0
df.loc[df['macd'] > df['signal'], 'trade_signal'] = 1  # potential buy signal
df.loc[df['macd'] < df['signal'], 'trade_signal'] = -1  # potential sell signal
