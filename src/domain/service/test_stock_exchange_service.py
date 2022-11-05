import unittest

from freezegun import freeze_time

from src.domain.service.stock_exchange_service import StockExchangeService


class TestStockExchangeService(unittest.TestCase):
    _opening_time = "10:00"
    _closing_time = "18:00"

    @freeze_time("2022-10-13")
    def test_is_today_weekday_should_return_true_on_weekday(self):
        stock_exchange_service = StockExchangeService()
        is_today_weekday = stock_exchange_service.is_today_weekday()
        self.assertTrue(is_today_weekday)

    @freeze_time("2022-10-09")
    def test_is_today_weekday_should_return_false_on_weekend(self):
        stock_exchange_service = StockExchangeService()
        is_today_weekday = stock_exchange_service.is_today_weekday()
        self.assertFalse(is_today_weekday)

    @freeze_time("2022-10-13 10:00:00")
    def test_is_stock_exchange_open_should_return_true_on_weekday_and_on_opening_time(self):
        stock_exchange_service = StockExchangeService()
        is_open = stock_exchange_service.is_stock_exchange_open(self._opening_time, self._closing_time)
        self.assertTrue(is_open)

    @freeze_time("2022-10-13 16:59:59")
    def test_is_stock_exchange_open_should_return_true_on_weekday_and_right_before_closing_time(self):
        stock_exchange_service = StockExchangeService()
        is_open = stock_exchange_service.is_stock_exchange_open(self._opening_time, self._closing_time)
        self.assertTrue(is_open)

    @freeze_time("2022-10-13 18:00:00")
    def test_is_stock_exchange_open_should_return_false_on_weekday_and_on_closing_time(self):
        stock_exchange_service = StockExchangeService()
        is_open = stock_exchange_service.is_stock_exchange_open(self._opening_time, self._closing_time)
        self.assertFalse(is_open)

    @freeze_time("2022-10-09")
    def test_is_stock_exchange_open_should_return_false_on_weekend(self):
        stock_exchange_service = StockExchangeService()
        is_open = stock_exchange_service.is_stock_exchange_open(self._opening_time, self._closing_time)
        self.assertFalse(is_open)

    @freeze_time("2022-10-13 09:59:59")
    def test_is_stock_exchange_open_should_return_false_before_opening_time(self):
        stock_exchange_service = StockExchangeService()
        is_open = stock_exchange_service.is_stock_exchange_open(self._opening_time, self._closing_time)
        self.assertFalse(is_open)

    @freeze_time("2022-10-13 18:00:01")
    def test_is_stock_exchange_open_should_return_false_after_closing_time(self):
        stock_exchange_service = StockExchangeService()
        is_open = stock_exchange_service.is_stock_exchange_open(self._opening_time, self._closing_time)
        self.assertFalse(is_open)
