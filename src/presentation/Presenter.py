from datetime import datetime
import time
import schedule
from data.datasource.RealEstateRemoteDataSource import RealEstateRemoteDataSource
from data.datasource.CompanyRemoteDataSource import CompanyRemoteDataSource
from domain.model.B3StockExchange import B3StockExchange
from domain.model.RealEstate import RealEstate
from domain.model.Company import Company
from domain.service.StockExchangeService import StockExchangeService
from domain.usecase.GetStocksUseCase import GetStocksUseCase


class Presenter:
    def __init__(self,
                stock_exchange_service: StockExchangeService,
                get_stocks_use_case: GetStocksUseCase):
        self._stock_exchange_service = stock_exchange_service
        self._get_stocks_use_case = get_stocks_use_case

    def start(self):
        self._get_info()
        schedule.every(5).minutes.do(self._get_info)
        b3 = B3StockExchange()
        while True:
            if self._stock_exchange_service.is_stock_exchange_open(b3.opening_time, b3.closing_time):
                schedule.run_pending()
                
            time.sleep(1)

    def _get_info(self):
        print("Getting Info... " + str(datetime.now()))
        print()
        stocks = self._get_stocks_use_case.execute()
        for stock in stocks:
            print("# "+ stock.name + " - " + stock.ticker + " #")
            print("Price: R$"+ str(stock.price) + ", Average Price: R$" + str(stock.average_price))
            print()
        # self._get_all_stocks_info()
        # self._get_all_real_estate_info()
        print()
        print()
        
    def _get_all_stocks_info(self):
        for stock in Company:
            info = self._company_remote_data_source.get_stock_info(stock)
            print(info)
    
    def _get_all_real_estate_info(self):
        for realEstate in RealEstate:
            info = self._real_estate_remote_data_source.get_real_estate_info(realEstate)
            print(info)