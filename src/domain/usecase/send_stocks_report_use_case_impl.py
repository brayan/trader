from src.domain.repository.stock_repository import StockRepository
from src.domain.usecase.get_stocks_use_case import GetStocksUseCase
from src.domain.usecase.send_stocks_report_use_case import SendStocksReportUseCase


class SendStocksReportUseCaseImpl(SendStocksReportUseCase):
    def __init__(self, stock_repository: StockRepository, get_stocks_use_case: GetStocksUseCase):
        self._stock_repository = stock_repository
        self._get_stocks_use_case = get_stocks_use_case

    def execute(self):
        stocks = self._get_stocks_use_case.execute()
        self._stock_repository.send_report(stocks)
