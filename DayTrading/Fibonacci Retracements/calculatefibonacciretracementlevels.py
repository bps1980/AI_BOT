high_price = df['high'].max()
low_price = df['low'].min()

fib_levels = {
    '38.2%': high_price - 0.382 * (high_price - low_price),
    '50%': high_price - 0.5 * (high_price - low_price),
    '61.8%': high_price - 0.618 * (high_price - low_price)
}
