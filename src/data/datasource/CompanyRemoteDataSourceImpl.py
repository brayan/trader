import requests
import bs4
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

from data.datasource.CompanyRemoteDataSource import CompanyRemoteDataSource
from data.mapper.StockToInfoMoneyMapper import map_company_to_info_money
from domain.model.Company import Company


class CompanyRemoteDataSourceImpl(CompanyRemoteDataSource):
    _URL = "https://www.infomoney.com.br/cotacoes/b3/acao/"

    def __init__(self):
        disable_warnings(InsecureRequestWarning)

    def get_company_price(self, company: Company) -> float:
        stock_info_money = map_company_to_info_money(company)

        result = requests.get(self._URL + str(stock_info_money.value), verify=False)

        soup = bs4.BeautifulSoup(result.text, "html.parser")
        section = soup.find('div', attrs={'class': "value"})
        price = section.find_next('p').get_text(strip=True)

        return float(price.replace(",", "."))
