import requests
import bs4
from data.datasource.StockRemoteDataSource import StockRemoteDataSource
from data.mapper.StockToInfoMoneyMapper import map_stock_to_info_money
from data.model.StockInfoMoney import StockInfoMoney
from domain.model.Stock import Stock
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


class StockRemoteDataSourceImpl(StockRemoteDataSource):
    _URL = "https://www.infomoney.com.br/cotacoes/b3/acao/"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_stock_price(self, stock: Stock) -> float:
        stock_info_money = map_stock_to_info_money(stock)

        result = requests.get(self._URL + stock_info_money.value, verify=False)
        
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        section = soup.find('div', attrs={ 'class':"value" })
        price = section.find_next('p').get_text(strip=True)

        return price

    def get_stock_info(self, stock: Stock) -> str:
        price = self.get_stock_price(stock)
        return stock.name + ": " + price