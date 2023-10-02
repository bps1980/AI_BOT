avg_period = 10
df['avg_volume'] = df['volume'].rolling(window=avg_period).mean()
