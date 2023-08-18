import setting


def binance_withdraw(token, amount, address, network):
    print(amount, token, 'to', address)
    try:
        setting.binance.withdraw(code=token, amount=amount, address=address, params={"network": network})
        print("Withdraw successful.\n")
    except Exception as e:
        print(e)


def mexc_withdraw(token, amount, address, network):
    print(amount, token, 'to', address)
    try:
        setting.mexc.withdraw(code=token, amount=amount, address=address, params={"network": network})
        print("Withdraw successful.\n")
    except Exception as e:
        print(e)


def okx_withdraw(token, amount, address, network):
    print(amount, token, 'to', address)
    try:
        setting.okx.withdraw(code=token, amount=amount, address=address, params={"network": network, "fee": setting.okxFee, "password": setting.okxPassword})
        print("Withdraw successful.\n")
    except Exception as e:
        print(e)
