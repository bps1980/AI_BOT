def stochastic_oscillator(df, k_window=14, d_window=3):
    low_min = df['low'].rolling(window=k_window).min()
    high_max = df['high'].rolling(window=k_window).max()

    df['%K'] = 100 * ((df['close'] - low_min) / (high_max - low_min))
    df['%D'] = df['%K'].rolling(window=d_window).mean()

stochastic_oscillator(df)
