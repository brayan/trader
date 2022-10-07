from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.datasource.StockRemoteDataSource import StockRemoteDataSource
from domain.model.RealEstate import RealEstate
from domain.model.Stock import Stock


class Presentation:
    def __init__(
        self, 
        stock_remote_data_source: StockRemoteDataSource, 
        real_estate_remote_data_source: RealEstateRemoteDataSource
    ):
        self.stock_remote_data_source = stock_remote_data_source
        self.real_estate_remote_data_source = real_estate_remote_data_source

    def start(self):
        self._get_all_stocks_info()
        self._get_all_real_estate_info()
        
    def _get_all_stocks_info(self):
        for stock in Stock:
            info = self.stock_remote_data_source.get_stock_info(stock)
            print(info)
    
    def _get_all_real_estate_info(self):
        for realEstate in RealEstate:
            info = self.real_estate_remote_data_source.get_real_estate_info(realEstate)
            print(info)