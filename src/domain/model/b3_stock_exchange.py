class B3StockExchange:
    def __init__(self):
        self._name = "B3 - Bolsa, Brasil, Balcão"
        self._opening_time = "10:00"
        self._closing_time = "18:00"

    @property
    def name(self) -> str:
        return self._name

    @property
    def opening_time(self) -> str:
        return self._opening_time

    @property
    def closing_time(self) -> str:
        return self._closing_time
