from datetime import datetime
from datetime import date


class StockExchangeService:
    _TIME_PATTERN = "%H:%M"

    def is_stock_exchange_open(self, opening_time: str, closing_time: str):
        return self.is_trading_time(opening_time, closing_time) and self.is_today_weekday()

    def is_trading_time(self, opening_time: str, closing_time: str) -> bool:
        opening_time_object = datetime.strptime(opening_time, self._TIME_PATTERN).time()
        closing_time_object = datetime.strptime(closing_time, self._TIME_PATTERN).time()
        
        now = datetime.now().time()

        return now >= opening_time_object and now <= closing_time_object
    
    def is_today_weekday(self) -> bool:
        today = date.today().weekday()
        return today != 5 and today != 6