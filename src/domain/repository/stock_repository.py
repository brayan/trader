from domain.model.company import Company
from domain.model.real_estate import RealEstate
from domain.model.stock import Stock


class StockRepository:
    def get_stock_from_company(self, company: Company) -> Stock or None:
        pass

    def get_stock_from_real_estate(self, real_estate: RealEstate) -> Stock or None:
        pass
