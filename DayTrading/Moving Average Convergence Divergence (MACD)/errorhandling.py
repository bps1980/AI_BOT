def execute_trade_with_error_handling(signal, last_order=None):
    try:
        return execute_trade(signal, last_order)
    except ccxt.InsufficientFunds:
        print("Insufficient funds!")
    except ccxt.NetworkError:
        print("Network Error!")
    except ccxt.ExchangeError as e:
        print(f"Exchange error: {e}")
    except Exception as e:
        print(f"Error executing trade: {e}")
    return last_order, None
