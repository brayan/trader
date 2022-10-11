class Stock:
    def __init__(self, name: str, ticker: str, price: float, average_price: float):
        self._name = name
        self._ticker = ticker
        self._price = price
        self._average_price = average_price

    @property
    def name(self)-> str:
        return self._name
    
    @property
    def ticker(self)-> str:
        return self._ticker
    
    @property
    def price(self)-> float:
        return self._price
    
    @property
    def average_price(self)-> float:
        return self._average_price