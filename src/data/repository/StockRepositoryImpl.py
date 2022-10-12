from data.datasource.CompanyRemoteDataSource import CompanyRemoteDataSource
from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.datasource.StockPortfolioRemoteDataSource import StockPortfolioRemoteDataSource
from domain.model.Company import Company
from domain.model.RealEstate import RealEstate
from domain.model.Stock import Stock
from domain.repository.StockRepository import StockRepository


class StockRepositoryImpl(StockRepository):
    def __init__(self,
                 company_remote_data_source: CompanyRemoteDataSource,
                 real_estate_data_source: RealEstateRemoteDataSource,
                 stock_portfolio_remote_data_source: StockPortfolioRemoteDataSource):
        self._company_remote_data_source = company_remote_data_source
        self._real_estate_data_source = real_estate_data_source
        self._stock_portfolio_remote_data_source = stock_portfolio_remote_data_source

    def get_stock_from_company(self, company: Company) -> Stock:
        company_stock_data = self._company_remote_data_source.get_company_stock(company)
        stock_portfolio = self._stock_portfolio_remote_data_source.get_stock_info(company.value)

        return Stock(name=stock_portfolio.name,
                     ticker=company.value,
                     price=company_stock_data.current_price,
                     average_price=stock_portfolio.average_price,
                     ceiling_price=stock_portfolio.ceiling_price,
                     price_variation=company_stock_data.price_change_percentage,
                     average_price_variation=0.0)

    def get_stock_from_real_estate(self, real_estate: RealEstate) -> Stock:
        real_estate_stock_data = self._real_estate_data_source.get_real_estate_stock(real_estate)
        stock_portfolio = self._stock_portfolio_remote_data_source.get_stock_info(real_estate.value)

        return Stock(name=stock_portfolio.name,
                     ticker=real_estate.value,
                     price=real_estate_stock_data.current_price,
                     average_price=stock_portfolio.average_price,
                     ceiling_price=stock_portfolio.ceiling_price,
                     price_variation=real_estate_stock_data.price_change_percentage,
                     average_price_variation=0.0)
