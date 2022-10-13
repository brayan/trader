from domain.usecase.calculate_price_change_percentage_use_case import CalculatePriceChangePercentageUseCase


class CalculatePriceChangePercentageUseCaseImpl(CalculatePriceChangePercentageUseCase):
    @staticmethod
    def execute(current_price: float, price_change: float) -> float:
        return round(((current_price / price_change) - 1) * 100, 2)
