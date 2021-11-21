from Crypto import crypto
api_key = "9fce61b89dea5c79c074b135dd1b31c679f5e2019b5a2a7a1cbd5d5ebf1adba3"
req = crypto(api_key, "BTC", "EUR", "2")
print(str(req.top()).replace(',', ',\n').replace('{', '{\n'))
