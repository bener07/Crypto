import requests
import json


class crypto:
    """
    Crypto python package using:
        Crypto-Compare API
        Examples:
             crypto(api_key, "BTC", "USD", "2")
             api_key        -The API key from your account.
             "BTC"          -The type of the coin you want to get information from. Here is the BTC meaning the Bitcoin crypto coin.
             "USD"          -The coin that you want to convert the crypto to. Example: From 'BTC'(bitcoins) to 'USD'(dollars). Default is USD
             "2"            -The time you want to get the currency. Default is 1.0

        after defining the object you just need to do the request using:
            Example:
                cr = crypto(api_key, "BTC", "USD")
                cr.price()              -This will show the price of the coin that you set in the object.
                cr.blockchain_data()    -This will return the blockchain data available from te crypto-compare API
            More features will be added later.
    """

    def __init__(self, api_key, symbol, exchange="USD", time="1"):
        self.sym = symbol
        self.exc = exchange
        self.api_key = api_key
        self.tmp = time

    def price(self):
        url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={self.sym}&tsym={self.exc}&limit={self.tmp}&api_key={self.api_key}'
        r = requests.get(url).json()
        # response = {
        #   'CoinName': r['Data'][self.sym]['CoinInfo']['Name'],
        #   'CoinFullName': r['Data'][self.sym]['CoinInfo']['FullName'],
        #   'CoinInfoURL': r['Data'][self.sym]['CoinInfo']['Url'],
        #   'RewardForEveryBlock': (r['Data'][self.sym]['CoinInfo']['BlockReward'], self.sym),
        # }
        return str(r).replace(',', ',\n').replace('{', '{\n').replace('}', '}\n').replace('[', '[\n').replace(']',
                                                                                                              ']\n')

    def blockchain_data(self):
        pass

    def mining_currency(self):
        url = f'https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms={self.sym}&tsyms={self.exc}&api_key={self.api_key}'
        r = requests.get(url).json()
        response = {
            'CoinName': r['Data'][self.sym]['CoinInfo']['Name'],
            'CoinFullName': r['Data'][self.sym]['CoinInfo']['FullName'],
            'CoinInfoURL': r['Data'][self.sym]['CoinInfo']['Url'],
            'RewardForEveryBlock': (r['Data'][self.sym]['CoinInfo']['BlockReward'], self.sym),
        }
        return str(r).replace(',', ',\n').replace('{', '{\n').replace('}', '}\n').replace('[', '[\n').replace(']',
                                                                                                              ']\n')
#        return f"""
#    Coin Name: {response['CoinName']}
#    Coin Full Name: {response['CoinFullName']}
#    Reward per block added: {response['RewardForEveryBlock']}
#    More info on: https://www.cryptocompare.com{response['CoinInfoURL']}
#        """
