from data.datasource.RealEstateRemoteDataSourceImpl import RealEstateRemoteDataSourceImpl
from data.datasource.StockRemoteDataSourceImpl import StockRemoteDataSourceImpl
from domain.model.RealEstate import RealEstate
from domain.model.Stock import Stock

stockDataSource = StockRemoteDataSourceImpl()
realEstateDataSource = RealEstateRemoteDataSourceImpl()

for stock in Stock:
    info = stockDataSource.get_stock_info(stock)
    print(info)

for realEstate in RealEstate:
    info = realEstateDataSource.get_real_estate_info(realEstate)
    print(info)