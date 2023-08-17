import ccxt


minAmount = 0.01
maxAmount = 0.02
decimal = 3

token = 'BNB'
network = 'BSC'


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

okxPassword = ""
okx = ccxt.okex(config={
    'apiKey': "",
    'secret': "",
    'password': okxPassword,
    'enableRateLimit': True
})
