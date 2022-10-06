import requests
import bs4
  
text = "vale3"
url = 'https://google.com/search?q=' + text

result = requests.get(url)
  
soup = bs4.BeautifulSoup(result.text, "html.parser")
# print(soup)

# span_objects = soup.find_all('span', attrs={"jsname": "vWLAgc"})
span_objects = soup.find_all('span')

for info in span_objects:
	print(info)
	print("------")


# print(info)


# input_tag = soup.find(attrs={"jsname": "vWLAgc"})
# output = input_tag['value']
# print(soup.prettify())