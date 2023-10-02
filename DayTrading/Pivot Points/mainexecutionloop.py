last_order = None
for i, row in df.iterrows():
    signal = row['trade_signal']
    if signal != 0:
        last_order, order = execute_trade(signal, last_order)
        if order:
            print(order)

