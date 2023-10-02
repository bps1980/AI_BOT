df['trade_signal'] = 0

# Bullish Signal
df.loc[(df['close'] > df['open']) & (df['volume'] > df['avg_volume']), 'trade_signal'] = 1

# Bearish Signal
df.loc[(df['close'] < df['open']) & (df['volume'] > df['avg_volume']), 'trade_signal'] = -1
