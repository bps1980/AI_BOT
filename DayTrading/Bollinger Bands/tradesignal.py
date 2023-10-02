df['trade_signal'] = 0
df.loc[df['close'] < df['lower_band'], 'trade_signal'] = 1  # potential buy signal
df.loc[df['close'] > df['upper_band'], 'trade_signal'] = -1  # potential sell signal
