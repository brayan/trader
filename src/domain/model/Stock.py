class Stock:
    def __init__(self, name: str, ticker: str, price: float,
                 average_price: float, ceiling_price: float,
                 price_variation: float, average_price_variation: float):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.average_price = average_price
        self.ceiling_price = ceiling_price
        self.price_variation = price_variation
        self.average_price_variation = average_price_variation
