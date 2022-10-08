from data.model.RealEstateInfoMoney import RealEstateInfoMoney
from domain.model.RealEstate import RealEstate


def map_real_estate_to_info_money(realEstate: RealEstate) -> RealEstateInfoMoney:
    if realEstate == RealEstate.BTG_PACTUAL_LOGISTICA:
        return RealEstateInfoMoney.BTG_PACTUAL_LOGISTICA
    elif realEstate == RealEstate.IRIDIUM:
        return RealEstateInfoMoney.IRIDIUM
    elif realEstate == RealEstate.MALLS_BRASIL_PLURAL:
        return RealEstateInfoMoney.MALLS_BRASIL_PLURAL
    elif realEstate == RealEstate.MAUA_CAPITAL:
        return RealEstateInfoMoney.MAUA_CAPITAL
    elif realEstate == RealEstate.TRX_REAL_ESTATE:
        return RealEstateInfoMoney.TRX_REAL_ESTATE