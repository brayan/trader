from data.datasource.company_remote_data_source_impl import CompanyRemoteDataSourceImpl
from data.datasource.real_estate_remote_data_source_impl import RealEstateRemoteDataSourceImpl
from data.datasource.stock_portfolio_remote_data_source_impl import StockPortfolioRemoteDataSourceImpl
from data.repository.stock_repository_impl import StockRepositoryImpl
from domain.service.stock_exchange_service import StockExchangeService
from domain.usecase.calculate_price_change_percentage_use_case_impl import CalculatePriceChangePercentageUseCaseImpl
from domain.usecase.get_stocks_use_case_impl import GetStocksUseCaseImpl
from domain.usecase.send_stocks_report_use_case_impl import SendStocksReportUseCaseImpl
from presentation.presenter import Presenter

_stock_exchange_service = StockExchangeService()
_company_remote_data_source = CompanyRemoteDataSourceImpl()
_real_estate_remote_data_source = RealEstateRemoteDataSourceImpl()
_stock_portfolio_remote_data_source = StockPortfolioRemoteDataSourceImpl()
_stock_repository = StockRepositoryImpl(_company_remote_data_source,
                                        _real_estate_remote_data_source,
                                        _stock_portfolio_remote_data_source)
_calculate_price_change_percentage_use_case = CalculatePriceChangePercentageUseCaseImpl()
_get_stocks_use_case = GetStocksUseCaseImpl(_stock_repository, _calculate_price_change_percentage_use_case)
_send_stocks_report_use_case = SendStocksReportUseCaseImpl(_stock_repository, _get_stocks_use_case)

Presenter(_stock_exchange_service, _get_stocks_use_case, _send_stocks_report_use_case).start()
