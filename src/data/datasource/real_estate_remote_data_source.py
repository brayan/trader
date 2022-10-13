from data.model.stock_info_money_data import StockInfoMoneyData
from domain.model.real_estate import RealEstate


class RealEstateRemoteDataSource:
    def get_real_estate_stock(self, real_estate: RealEstate) -> StockInfoMoneyData or None:
        pass
