window = 20
num_std_dev = 2

df['SMA'] = df['close'].rolling(window=window).mean()
df['rolling_std'] = df['close'].rolling(window=window).std()
df['upper_band'] = df['SMA'] + (df['rolling_std'] * num_std_dev)
df['lower_band'] = df['SMA'] - (df['rolling_std'] * num_std_dev)
