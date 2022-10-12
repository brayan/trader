from data.model.StockInfoMoneyData import StockInfoMoneyData
from domain.model.Company import Company


class CompanyRemoteDataSource:
    def get_company_stock(self, company: Company) -> StockInfoMoneyData:
        pass
