class StockData:
    def __init__(self, ticker: str, 
                currentPrice: float,
                avaregePrice: float,
                 ):
        self._ticker = ticker
        self._currentPrice = currentPrice
        self._avaregePrice  = avaregePrice