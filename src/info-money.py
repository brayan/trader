import requests
import bs4
  
text = "vale-vale3"
URL = 'https://www.infomoney.com.br/cotacoes/b3/acao/' + text


def search_stock_price(url: str) -> str:
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, "html.parser")

    section = soup.find('div', attrs={'class':"value"})

    price = section.find_next('p').get_text(strip=True)

    print("Vale: " + price)
    return url
