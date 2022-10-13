import bs4
import requests
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning

from data.datasource.company_remote_data_source import CompanyRemoteDataSource
from data.mapper.stock_to_info_money_mapper import map_company_to_info_money
from data.model.stock_info_money_data import StockInfoMoneyData
from domain.model.company import Company


class CompanyRemoteDataSourceImpl(CompanyRemoteDataSource):
    _URL = "https://www.infomoney.com.br/cotacoes/b3/acao/"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_company_stock(self, company: Company) -> StockInfoMoneyData or None:
        try:
            stock_info_money = map_company_to_info_money(company)

            result = requests.get(self._URL + str(stock_info_money.value), verify=False)

            soup = bs4.BeautifulSoup(result.text, "html.parser")
            price_div = soup.find('div', attrs={'class': "value"})
            price = price_div.find_next('p').get_text(strip=True)

            price_change_div = soup.find('div', attrs={'class': "percentage"})
            price_change = price_change_div.find_next("p").get_text(strip=True)
            price_change_formatted = price_change.strip().replace("%", "").replace("+", "")

            return StockInfoMoneyData(current_price=float(price.replace(",", ".")),
                                      price_change_percentage=float(price_change_formatted))
        except Exception as e:
            print("[ERROR] " + str(company.value) + ": " + str(e))
            return None
