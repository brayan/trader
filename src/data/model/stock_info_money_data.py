class StockInfoMoneyData:
    def __init__(self, current_price: float, price_change_percentage: float):
        self._current_price = current_price
        self._price_change_percentage = price_change_percentage

    @property
    def current_price(self) -> float:
        return self._current_price

    @property
    def price_change_percentage(self) -> float:
        return self._price_change_percentage
