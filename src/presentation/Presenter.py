from datetime import datetime
import time
import schedule
from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.datasource.StockRemoteDataSource import StockRemoteDataSource
from domain.model.B3StockExchange import B3StockExchange
from domain.model.RealEstate import RealEstate
from domain.model.Stock import Stock
from domain.service.StockExchangeService import StockExchangeService


class Presenter:
    def __init__(self,
                stock_exchange_service: StockExchangeService,
                stock_remote_data_source: StockRemoteDataSource, 
                real_estate_remote_data_source: RealEstateRemoteDataSource):
        self.stock_exchange_service = stock_exchange_service
        self.stock_remote_data_source = stock_remote_data_source
        self.real_estate_remote_data_source = real_estate_remote_data_source

    def start(self):
        schedule.every(5).minutes.do(self._get_info)
        b3 = B3StockExchange()
        while True:
            if self.stock_exchange_service.is_stock_exchange_open(b3.opening_time, b3.closing_time):
                schedule.run_pending()
                
            time.sleep(1)

    def _get_info(self):
        print("Getting Info... " + str(datetime.now()))
        print()
        self._get_all_stocks_info()
        self._get_all_real_estate_info()
        print()
        print()
        
    def _get_all_stocks_info(self):
        for stock in Stock:
            info = self.stock_remote_data_source.get_stock_info(stock)
            print(info)
    
    def _get_all_real_estate_info(self):
        for realEstate in RealEstate:
            info = self.real_estate_remote_data_source.get_real_estate_info(realEstate)
            print(info)