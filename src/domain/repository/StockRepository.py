from domain.model.Company import Company
from domain.model.RealEstate import RealEstate
from domain.model.Stock import Stock


class StockRepository:
    def get_stock_from_company(self, company: Company) -> Stock:
        pass

    def get_stock_from_real_estate(self, real_estate: RealEstate) -> Stock:
        pass
