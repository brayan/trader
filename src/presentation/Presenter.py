from datetime import datetime
import time
import schedule
from domain.model.B3StockExchange import B3StockExchange
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
        print()
        print()