from data.datasource.StockRemoteDataSourceImpl import StockRemoteDataSourceImpl
from data.mapper.StockToInfoMoneyMapper import map_stock_to_info_money
from domain.model.Stock import Stock

for data in Stock:
    dataSource = StockRemoteDataSourceImpl()
    price = dataSource.get_stock_price(data)
    print(price)