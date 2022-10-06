import requests
import bs4
from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.mapper.RealEstateToInfoMoneyMapper import map_real_estate_to_info_money
from domain.model.RealEstate import RealEstate
from domain.model.Stock import Stock

URL = "https://www.infomoney.com.br/cotacoes/b3/fii/"

class RealEstateRemoteDataSourceImpl(RealEstateRemoteDataSource):
    
    def get_real_estate_price(self, realEstate: RealEstate) -> float:
        real_estate_info_money = map_real_estate_to_info_money(realEstate)
        
        result = requests.get(URL + real_estate_info_money.value)
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        section = soup.find('div', attrs={ 'class':"cotacoes__header-price" })
        price = section.find_next('span').get_text(strip=True)

        return price

    def get_real_estate_info(self, realEstate: RealEstate) -> str:
        price = self.get_real_estate_price(realEstate)
        return realEstate.name + ": " + price