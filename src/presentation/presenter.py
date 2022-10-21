import time
from datetime import datetime

import schedule
from domain.model.b3_stock_exchange import B3StockExchange
from domain.service.stock_exchange_service import StockExchangeService
from domain.usecase.get_stocks_use_case import GetStocksUseCase
from domain.usecase.send_stocks_report_use_case import SendStocksReportUseCase


class Presenter:
    def __init__(self,
                 stock_exchange_service: StockExchangeService,
                 get_stocks_use_case: GetStocksUseCase,
                 send_stocks_report_use_case: SendStocksReportUseCase):
        self._stock_exchange_service = stock_exchange_service
        self._get_stocks_use_case = get_stocks_use_case
        self._send_stocks_report_use_case = send_stocks_report_use_case

    def start(self):
        # self._send_stocks_report_use_case.execute()
        self._get_info()
        schedule.every(30).minutes.do(self._get_info)
        b3 = B3StockExchange()
        while True:
            if self._stock_exchange_service.is_stock_exchange_open(b3.opening_time, b3.closing_time):
                schedule.run_pending()

            time.sleep(1)

    def _get_info(self):
        print("Getting Info... " + str(datetime.now()))
        print()
        stocks = self._get_stocks_use_case.execute()
        print()
        for stock in stocks:
            print("# " + stock.ticker + " - " + stock.name + " #")
            print("- Price: R$" + str(stock.price))
            print("- Average Price: R$" + str(stock.average_price))
            print("- Ceiling Price: R$" + str(stock.ceiling_price))
            print("- Price Variation: " + str(stock.price_variation) + "%")
            print("- Average Price Variation: " + str(stock.average_price_variation) + "%")
            print()
        print()
        print()
