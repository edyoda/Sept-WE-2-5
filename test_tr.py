import requests 
from bs4 import BeautifulSoup
import threading

def get_data(card):
	price = card.find("div",attrs={"class":"m-srp-card__price"})
	title  = card.find("a",attrs={"class":"m-srp-card__title"})
	link = title.get("href")
	
	response2 = requests.get(link)
	soup2 = BeautifulSoup(response2.content,"html.parser")
	agent = soup2.find("span",attrs={"class":"commercialName"})
	if agent:
		agent_text = agent.text.replace("\n"," ")
	else:
		agent_text = None	
	title_text = title.text.replace("\n"," ")
	carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
	data = "{} {} {} {}".format(title_text,price.text,carpet_area.text,agent_text)
	print(data)



url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore"
response = requests.get(url)
soup = BeautifulSoup(response.content,"html.parser")
cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

for card in cards:
	t = threading.Thread(target=get_data,args=(card,))
	t.start()
	