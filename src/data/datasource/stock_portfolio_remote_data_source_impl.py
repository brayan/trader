import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from data.datasource.stock_portfolio_remote_data_source import StockPortfolioRemoteDataSource
from data.model.stock_data import StockData


class StockPortfolioRemoteDataSourceImpl(StockPortfolioRemoteDataSource):
    _URL = "https://raw.githubusercontent.com/brayan/api/master/trader/stock-portfolio.json"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_stock_info(self, ticker: str) -> StockData:
        result = requests.get(self._URL, verify=False)
        result_json = result.json()
        for stock in result_json["stocks"]:
            if stock["ticker"] == ticker:
                return StockData(name=stock["name"],
                                 ticker=stock["ticker"],
                                 average_price=float(stock["averagePrice"]),
                                 ceiling_price=float(stock["ceilingPrice"]))
