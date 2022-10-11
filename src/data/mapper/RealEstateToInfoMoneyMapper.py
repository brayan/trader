from src.data.model.RealEstateInfoMoney import RealEstateInfoMoney
from src.domain.model.RealEstate import RealEstate


def map_real_estate_to_info_money(real_estate: RealEstate) -> RealEstateInfoMoney:
    if real_estate == RealEstate.BTG_PACTUAL_LOGISTICA:
        return RealEstateInfoMoney.BTG_PACTUAL_LOGISTICA
    elif real_estate == RealEstate.IRIDIUM:
        return RealEstateInfoMoney.IRIDIUM
    elif real_estate == RealEstate.MALLS_BRASIL_PLURAL:
        return RealEstateInfoMoney.MALLS_BRASIL_PLURAL
    elif real_estate == RealEstate.MAUA_CAPITAL:
        return RealEstateInfoMoney.MAUA_CAPITAL
    elif real_estate == RealEstate.TRX_REAL_ESTATE:
        return RealEstateInfoMoney.TRX_REAL_ESTATE
