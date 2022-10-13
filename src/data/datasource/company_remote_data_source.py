from data.model.stock_info_money_data import StockInfoMoneyData
from domain.model.company import Company


class CompanyRemoteDataSource:
    def get_company_stock(self, company: Company) -> StockInfoMoneyData or None:
        pass
