def execute_trade(signal, last_order=None):
    order_amount = 0.01  # e.g., 0.01 BTC
    if signal == 1 and (last_order == 'sell' or last_order is None):
        order = binanceus.create_market_buy_order(symbol, order_amount)
        return 'buy', order
    elif signal == -1 and (last_order == 'buy' or last_order is None):
        order = binanceus.create_market_sell_order(symbol, order_amount)
        return 'sell', order
    return last_order, None
