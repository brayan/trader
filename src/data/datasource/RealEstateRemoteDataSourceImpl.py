import bs4
import requests
from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.mapper.RealEstateToInfoMoneyMapper import map_real_estate_to_info_money
from data.model.StockInfoMoneyData import StockInfoMoneyData
from domain.model.RealEstate import RealEstate
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning


class RealEstateRemoteDataSourceImpl(RealEstateRemoteDataSource):
    _URL = "https://www.infomoney.com.br/cotacoes/b3/fii/"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_real_estate_stock(self, real_estate: RealEstate) -> StockInfoMoneyData:
        try:
            real_estate_info_money = map_real_estate_to_info_money(real_estate)

            result = requests.get(self._URL + real_estate_info_money.value, verify=False)
            soup = bs4.BeautifulSoup(result.text, "html.parser")
            price_div = soup.find('div', attrs={'class': "cotacoes__header-price"})
            price = price_div.find_next('span').get_text(strip=True)

            price_change_div = soup.find('div', attrs={'class': "cotacoes__header-change"})
            price_change = price_change_div.find_next("span").get_text(strip=True)
            price_change_formatted = price_change.strip().replace("%", "").replace(",", ".")

            negative_checker = price_change_div.find_next("i").get_text(strip=True)

            if negative_checker == "arrow_downward":
                price_change_formatted = "-" + price_change_formatted

            return StockInfoMoneyData(current_price=float(price.replace(",", ".")),
                                      price_change_percentage=float(price_change_formatted))
        except ValueError:
            print("Error parsing " + str(real_estate.value))
