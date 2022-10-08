from data.datasource.StockRemoteDataSource import StockRemoteDataSource
from domain.model.Stock import Stock
from domain.repository.StockRepository import StockRepository


class StockRepositoryImpl(StockRepository):
    def __init__(self, stock_remote_data_source: StockRemoteDataSource):
        self._stock_remote_data_source = stock_remote_data_source

    def get_stock_price(self, stock: Stock) -> float:
        return self._stock_remote_data_source.get_stock_price(stock)

    def get_stock_info(self, stock: Stock) -> str:
        return self._stock_remote_data_source.get_stock_info(stock)