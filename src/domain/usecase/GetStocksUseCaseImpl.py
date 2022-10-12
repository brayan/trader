from domain.model.Company import Company
from domain.model.RealEstate import RealEstate
from domain.repository.StockRepository import StockRepository
from domain.usecase.CalculatePriceChangePercentageUseCase import CalculatePriceChangePercentageUseCase
from domain.usecase.GetStocksUseCase import GetStocksUseCase


class GetStocksUseCaseImpl(GetStocksUseCase):
    def __init__(self, stock_repository: StockRepository,
                 calculate_price_change_percentage_use_case: CalculatePriceChangePercentageUseCase):
        self._stock_repository = stock_repository
        self._calculate_price_change_percentage_use_case = calculate_price_change_percentage_use_case

    def execute(self) -> list:
        stocks = []

        for company in Company:
            company_stock = self._stock_repository.get_stock_from_company(company)
            company_stock.average_price_variation = self._calculate_price_change_percentage_use_case.execute(
                company_stock.price, company_stock.average_price)
            stocks.append(company_stock)

        for real_estate in RealEstate:
            real_estate_stock = self._stock_repository.get_stock_from_real_estate(real_estate)
            real_estate_stock.average_price_variation = self._calculate_price_change_percentage_use_case.execute(
                real_estate_stock.price, real_estate_stock.average_price)
            stocks.append(real_estate_stock)

        return sorted(stocks, key=lambda stock: stock.average_price_variation)
