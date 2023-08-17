import random

import withdraw
import setting


def main():
    with open('addresses.txt', 'r') as f:
        for line in f:
            address = line.rstrip()
            amount = round(random.uniform(setting.maxAmount, setting.minAmount), setting.decimal)

            withdraw.binance_withdraw(setting.token, amount, address, setting.network)
            # withdraw.mexc_withdraw(setting.token, amount, address, setting.network)
            # withdraw.okx_withdraw(setting.token, amount, address, setting.network)


main()
