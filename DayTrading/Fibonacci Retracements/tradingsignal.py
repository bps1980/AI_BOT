buffer = 50  # Price buffer to avoid too many false signals due to minor price fluctuations

df['trade_signal'] = 0

# Bullish Signal
df.loc[df['close'] < (fib_levels['61.8%'] + buffer), 'trade_signal'] = 1

# Bearish Signal
df.loc[df['close'] > (fib_levels['38.2%'] - buffer), 'trade_signal'] = -1
