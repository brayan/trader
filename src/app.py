from domain.service.StockExchangeService import StockExchangeService
from data.datasource.CompanyRemoteDataSourceImpl import CompanyRemoteDataSourceImpl
from data.datasource.RealEstateRemoteDataSourceImpl import RealEstateRemoteDataSourceImpl
from data.datasource.StockPortfolioRemoteDataSourceImpl import StockPortfolioRemoteDataSourceImpl
from data.repository.StockRepositoryImpl import StockRepositoryImpl
from domain.usecase.GetStocksUseCaseImpl import GetStocksUseCaseImpl
from presentation.Presenter import Presenter

_stock_exchange_service = StockExchangeService()
_company_remote_data_source = CompanyRemoteDataSourceImpl()
_real_estate_remote_data_source = RealEstateRemoteDataSourceImpl()
_stock_portfolio_remote_data_source = StockPortfolioRemoteDataSourceImpl()
_stock_repository = StockRepositoryImpl(_company_remote_data_source,
                                        _real_estate_remote_data_source,
                                        _stock_portfolio_remote_data_source)
_get_stocks_use_case = GetStocksUseCaseImpl(_stock_repository)

Presenter(_stock_exchange_service, _get_stocks_use_case).start()
