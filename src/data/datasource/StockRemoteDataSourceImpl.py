from nis import match
import requests
import bs4
from data.datasource.StockRemoteDataSource import StockRemoteDataSource
from data.mapper.StockToInfoMoneyMapper import map_stock_to_info_money
from data.model.StockInfoMoney import StockInfoMoney
from domain.model.Stock import Stock

URL = "https://www.infomoney.com.br/cotacoes/b3/acao/"

# https://www.infomoney.com.br/cotacoes/b3/fii/fundos-imobiliarios-btlg11/

class StockRemoteDataSourceImpl(StockRemoteDataSource):
    
    def get_stock_price(self, company: Stock) -> float:
        stock_info_money = map_stock_to_info_money(company)
        
        result = requests.get(URL + stock_info_money.value)
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        section = soup.find('div', attrs={ 'class':"value" })
        price = section.find_next('p').get_text(strip=True)

        return price