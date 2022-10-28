from data.model.company_info_money import CompanyInfoMoney
from domain.model.company import Company


def map_company_to_info_money(company: Company) -> CompanyInfoMoney:
    if company == Company.BRASILAGRO:
        return CompanyInfoMoney.BRASILAGRO
    elif company == Company.BANCO_DO_BRASIL:
        return CompanyInfoMoney.BANCO_DO_BRASIL
    elif company == Company.BB_SEGURIDADE:
        return CompanyInfoMoney.BB_SEGURIDADE
    elif company == Company.COPEL:
        return CompanyInfoMoney.COPEL
    elif company == Company.ENGIE_BRASIL:
        return CompanyInfoMoney.ENGIE_BRASIL
    elif company == Company.MAHLE_METAL_LEVE:
        return CompanyInfoMoney.MAHLE_METAL_LEVE
    elif company == Company.PETROBRAS:
        return CompanyInfoMoney.PETROBRAS
    elif company == Company.IRANI:
        return CompanyInfoMoney.IRANI
    elif company == Company.TUPY:
        return CompanyInfoMoney.TUPY
    elif company == Company.VALE:
        return CompanyInfoMoney.VALE
