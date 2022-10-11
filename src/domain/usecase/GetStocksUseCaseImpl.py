from domain.model.Company import Company
from domain.model.RealEstate import RealEstate
from domain.repository.StockRepository import StockRepository
from domain.usecase.GetStocksUseCase import GetStocksUseCase


class GetStocksUseCaseImpl(GetStocksUseCase):
    def __init__(self, stock_repository: StockRepository):
        self._stock_repository = stock_repository
    
    def execute(self) -> list:
        stocks = []

        for company in Company:
            company_stock = self._stock_repository.get_stock_from_company(company)
            stocks.append(company_stock)

        for real_estate in RealEstate:
            real_estate_stock = self._stock_repository.get_stock_from_real_estate(real_estate)
            stocks.append(real_estate_stock)
        
        return stocks