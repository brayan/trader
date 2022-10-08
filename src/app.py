from data.datasource.RealEstateRemoteDataSourceImpl import RealEstateRemoteDataSourceImpl
from data.datasource.StockRemoteDataSourceImpl import StockRemoteDataSourceImpl
from domain.service.StockExchangeService import StockExchangeService
from presentation.Presenter import Presenter


stock_exchange_service = StockExchangeService()
stock_remote_data_source = StockRemoteDataSourceImpl()
real_estate_remote_data_source = RealEstateRemoteDataSourceImpl()

Presenter(stock_exchange_service, 
          stock_remote_data_source, 
          real_estate_remote_data_source).start()