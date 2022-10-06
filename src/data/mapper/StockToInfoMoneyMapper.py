from data.model.StockInfoMoney import StockInfoMoney
from domain.model.Stock import Stock

def map_stock_to_info_money(company: Stock) -> StockInfoMoney:
    if company == Stock.BRASILAGRO:
        return StockInfoMoney.BRASILAGRO
    elif company == Stock.BANCO_DO_BRASIL:
        return StockInfoMoney.BANCO_DO_BRASIL
    elif company == Stock.BB_SEGURIDADE:
        return StockInfoMoney.BB_SEGURIDADE
    elif company == Stock.COPEL:
        return StockInfoMoney.COPEL
    elif company == Stock.ENGIE_BRASIL:
        return StockInfoMoney.ENGIE_BRASIL
    elif company == Stock.MAHLE_METAL_LEVE:
        return StockInfoMoney.MAHLE_METAL_LEVE
    elif company == Stock.PETROBRAS:
        return StockInfoMoney.PETROBRAS
    elif company == Stock.TUPY:
        return StockInfoMoney.TUPY
    elif company == Stock.VALE:
        return StockInfoMoney.VALE