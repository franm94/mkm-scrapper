# Import Libraries
import requests
from bs4 import BeautifulSoup
from Card import Card


DEBUG = True
# min_condition ---> 3 = EX ; 2 = NM ; 1 = M
min_condition = "2"
collection = "Alpha"
card_name = "Island-V-1"
cards = []

def getData(card_name, min_condition):
  url = "https://www.cardmarket.com/es/Magic/Products/Singles/"+ collection + "/" + card_name +"?minCondition=" + min_condition
  print (url)
  web = requests.get(url)

  # Parse web_page
  soup = BeautifulSoup(web.text, "lxml")

  # Create set of results based on HTML tags with desired data
  results = soup.find_all(class_='row no-gutters article-row')
  print ("Se han encontrado " + str(len(results)) + " ofertas diferentes")
  for result in results:
    description = result.find_all(class_='d-block text-truncate text-muted font-italic small')
    description = [d.text for d in description]
    print(len(description))

    units = result.find_all(class_='item-count small text-right')
    units = [u.text for u in units]

    language = result.find_all('span', class_='icon mr-2')
    language = [l.get('data-original-title') for l in language]

    condition = result.find_all('span', class_='icon')
    condition = [c.get('data-original-title') for c in condition]

    location = result.find_all('span', class_='icon d-flex has-content-centered mr-1')
    location = [la.get('title').replace("Ubicación del artículo: ", "") for la in location]

    price_item = result.find_all(class_='price-container d-none d-md-flex justify-content-end')
    price_card = [float(p.text.replace(".", "").replace(" €", "").replace(",", ".")) for p in price_item]

    if not description:
      card = Card("", location[0],"Not description",language[0],condition[2],price_card[0],units[0])
    else:
      card = Card("", location[0],description[0],language[0],condition[2],price_card[0],units[0])
  
    if (DEBUG):
      print (card.description)
      print (card.language)
      print (card.condition)
      print (card.location)
      print (card.units)
      print (card.price)

      print("")
  #numbers = [d.text for d in results]


getData(card_name, min_condition)
