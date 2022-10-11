import requests
import bs4
from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.mapper.RealEstateToInfoMoneyMapper import map_real_estate_to_info_money
from domain.model.RealEstate import RealEstate
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings


class RealEstateRemoteDataSourceImpl(RealEstateRemoteDataSource):
    _URL = "https://www.infomoney.com.br/cotacoes/b3/fii/"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_real_estate_price(self, realEstate: RealEstate) -> float:
        real_estate_info_money = map_real_estate_to_info_money(realEstate)
        
        result = requests.get(self._URL + real_estate_info_money.value, verify=False)
        soup = bs4.BeautifulSoup(result.text, "html.parser")
        section = soup.find('div', attrs={ 'class':"cotacoes__header-price" })
        price = section.find_next('span').get_text(strip=True)

        return price.replace(",", ".")

    def get_real_estate_info(self, realEstate: RealEstate) -> str:
        price = self.get_real_estate_price(realEstate)
        return realEstate.name + ": " + price