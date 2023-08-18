import ccxt


minAmount = 1010
maxAmount = 1050
decimal = 1

token = 'USDC'
network = 'Polygon'

# If you don't use okex, leave it intact.
okxFee = 0.8
okxPassword = ""

binance = ccxt.binance(config={
    'apiKey': "",
    'secret': "",
    'enableRateLimit': True
})

mexc = ccxt.mexc(config={
    'apiKey': "",
    'secret': "",
    'enableRateLimit': True
})

okx = ccxt.okex(config={
    'apiKey': "",
    'secret': "",
    'password': okxPassword,
    'enableRateLimit': True
})
