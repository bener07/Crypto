import requests
import json


class crypto:
    def __init__(self, api_key, symbol, exchange="USD", limit="2", code=False):
        self.sym = symbol
        self.exc = exchange
        self.api_key = api_key
        self.limit = limit
        self.code = code

    def price(self):
        """
        Price function is used to return the price of a certain coin to another kind of real life money 
        EX:
            BTC -- USD :is going to return the value of bitcoin in USD dollars.
        :return: 
        """
        url = f'https://min-api.cryptocompare.com/data/price?fsym={self.sym}&tsyms={self.exc}'
        r = requests.get(url).json()
        response = {
            "Price": r[self.exc]
        }
        return f"""{self.sym} has a Price of {response['Price']} {self.exc}"""

    def topBy24HRS(self):
        url = f'https://min-api.cryptocompare.com/data/top/totaltoptiervolfull?limit={self.limit}&tsym={self.exc}'
        r = requests.get(url).json()
        return str(r).replace(',', ',\n').replace('{', '{\n').replace('[', '[\n')
    def mining_currency(self):
        """
        Mining currency function is a simple requests to the api from CryptoCompare that then returns
        a simple and readable output for the user. 
        :return: 
        """
        url = f'https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms={self.sym}&tsyms={self.exc}&api_key={self.api_key}'
        r = requests.get(url).json()
        response = {
            'CoinName': r['Data'][self.sym]['CoinInfo']['Name'],
            'CoinFullName': r['Data'][self.sym]['CoinInfo']['FullName'],
            'CoinInfoURL': r['Data'][self.sym]['CoinInfo']['Url'],
            'RewardForEveryBlock': (r['Data'][self.sym]['CoinInfo']['BlockReward'], self.sym),
        }
        return f"""
    Coin Name: {response['CoinName']}
    Coin Full Name: {response['CoinFullName']}
    Reward per block added: {response['RewardForEveryBlock']}
    More info on: https://www.cryptocompare.com{response['CoinInfoURL']}
        """

    def social(self):
        """
        The social Function is to a simple requests to the CryptoCompare API that then returns a huje amount of information
        about the social media, and of course that information has info about the crypto coin currency or something like that
        i didn't desenvolve it to much
        :return: 
        """
        url = f'https://min-api.cryptocompare.com/data/social/coin/latest?api_key={self.api_key}'
        r = requests.get(url).json()
        response = {
            'General': r['Data']['General'],
            'CryptoCompare': r['Data']['CryptoCompare'],
            'Twitter': r['Data']['Twitter'],
            'Reddit': r['Data']['Reddit'],
            'Facebook': r['Data']['Facebook'],
            'Code': r['Data']['CodeRepository']['List'],
        }
        data = f"""General info: 
      - Points: {response['General']['Points']};
      - Name: {response['General']['Name']};
      - Coin Name: {response['General']['CoinName']};

CryptoCompare:
      - Points: {response['CryptoCompare']['Points']};
      - Followers: {response['CryptoCompare']['Followers']};
      - Number of Posts: {response['CryptoCompare']['Posts']};
      - Number of Comments: {response['CryptoCompare']['Comments']};
      - Number of Markets: {response['CryptoCompare']['PageViewsSplit']['Markets']};
      - Number of Trades: {response['CryptoCompare']['PageViewsSplit']['Trades']};
      - Number of Charts: {response['CryptoCompare']['PageViewsSplit']['Charts']};
      - Number of Analysis: {response['CryptoCompare']['PageViewsSplit']['Analysis']};
      - Number of News: {response['CryptoCompare']['PageViewsSplit']['News']};

Twitter:
      - Points: {response['Twitter']['Points']};
      - Followers: {response['Twitter']['followers']};
      - Statuses: {response['Twitter']['statuses']};
      - Points: {response['Twitter']['following']};
      
Reddit:
      - Points: {response['Reddit']['Points']};
      - Posts per hour: {response['Reddit']['posts_per_hour']};
      - Comments per hour: {response['Reddit']['comments_per_hour']};
      - Comments per day: {response['Reddit']['comments_per_day']};
      - Active users: {response['Reddit']['active_users']};
      - Posts per day: {response['Reddit']['posts_per_day']};
      - Subscribers number: {response['Reddit']['subscribers']};

Facebook:
      - Points: {response['Facebook']['Points']};
      - Likes: {response['Facebook']['likes']};"""

        if self.code is True:
            return data + (
                f"\n\nCode Stuff that you might want to look at (this is all in a JSON form from the raw api "
                f"request):\n \n{response['Code']}").replace(',', ',\n').replace('{', '{\n')
        else:
            return data
