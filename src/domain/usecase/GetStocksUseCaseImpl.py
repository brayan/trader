from src.domain.model.Company import Company
from src.domain.model.RealEstate import RealEstate
from src.domain.repository.StockRepository import StockRepository
from src.domain.usecase.GetStocksUseCase import GetStocksUseCase


class GetStocksUseCaseImpl(GetStocksUseCase):
    def __init__(self, stock_repository: StockRepository):
        self._stock_repository = stock_repository

    def execute(self) -> list:
        stocks = []

        for company in Company:
            company_stock = self._stock_repository.get_stock_from_company(company)
            company_stock.average_price_variation = round(
                ((company_stock.price / company_stock.average_price) - 1) * 100, 2)
            stocks.append(company_stock)

        for real_estate in RealEstate:
            real_estate_stock = self._stock_repository.get_stock_from_real_estate(real_estate)
            real_estate_stock.average_price_variation = round(
                ((real_estate_stock.price / real_estate_stock.average_price) - 1) * 100, 2)
            stocks.append(real_estate_stock)

        return stocks
