from src.data.datasource.CompanyRemoteDataSourceImpl import CompanyRemoteDataSourceImpl
from src.data.datasource.RealEstateRemoteDataSourceImpl import RealEstateRemoteDataSourceImpl
from src.data.datasource.StockPortfolioRemoteDataSourceImpl import StockPortfolioRemoteDataSourceImpl
from src.data.repository.StockRepositoryImpl import StockRepositoryImpl
from src.domain.service.StockExchangeService import StockExchangeService
from src.domain.usecase.GetStocksUseCaseImpl import GetStocksUseCaseImpl
from src.presentation.Presenter import Presenter

_stock_exchange_service = StockExchangeService()
_company_remote_data_source = CompanyRemoteDataSourceImpl()
_real_estate_remote_data_source = RealEstateRemoteDataSourceImpl()
_stock_portfolio_remote_data_source = StockPortfolioRemoteDataSourceImpl()
_stock_repository = StockRepositoryImpl(_company_remote_data_source,
                                        _real_estate_remote_data_source,
                                        _stock_portfolio_remote_data_source)
_get_stocks_use_case = GetStocksUseCaseImpl(_stock_repository)

Presenter(_stock_exchange_service, _get_stocks_use_case).start()
