df['trade_signal'] = 0
buffer = 50  # Price buffer

# Bullish Signal
df.loc[df['close'] <= df['S1'] + buffer, 'trade_signal'] = 1

# Bearish Signal
df.loc[df['close'] >= df['R1'] - buffer, 'trade_signal'] = -1
