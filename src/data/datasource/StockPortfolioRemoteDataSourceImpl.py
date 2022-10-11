import requests
from data.datasource.StockPortfolioRemoteDataSource import StockPortfolioRemoteDataSource
from data.model.StockData import StockData
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


class StockPortfolioRemoteDataSourceImpl(StockPortfolioRemoteDataSource):
    _URL = "https://raw.githubusercontent.com/brayan/api/master/trader/stock-portfolio.json"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_stock_info(self, ticker: str) -> StockData:
        result = requests.get(self._URL, verify = False)
        resultFromJson = result.json()
        for stock in resultFromJson["stocks"]:
            if stock["ticker"] == ticker:
                return StockData(name = stock["name"], ticker = stock["ticker"], average_price = stock["averagePrice"])