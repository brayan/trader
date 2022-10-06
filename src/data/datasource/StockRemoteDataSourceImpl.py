import requests
import bs4
from data.datasource.StockRemoteDataSource import StockRemoteDataSource
from data.mapper.StockToInfoMoneyMapper import map_stock_to_info_money
from data.model.StockInfoMoney import StockInfoMoney
from domain.model.Stock import Stock

URL = "https://www.infomoney.com.br/cotacoes/b3/acao/"

class StockRemoteDataSourceImpl(StockRemoteDataSource):
    
    def get_stock_price(self, stock: Stock) -> float:
        stock_info_money = map_stock_to_info_money(stock)
        
        result = requests.get(URL + stock_info_money.value)
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        section = soup.find('div', attrs={ 'class':"value" })
        price = section.find_next('p').get_text(strip=True)

        return price

    def get_stock_info(self, stock: Stock) -> str:
        price = self.get_stock_price(stock)
        return stock.name + ": " + price