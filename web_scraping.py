# HTML => BS 
# xml 
# json 
# csv files 

# Python :
# 	Beautiful Soup  lib
# 	Scrapy framework 

# request to server 
# 	1 Get 
# 	2 Post 
# server => response => html 

# <html>
# 	<head>
# 		<title>Title</title>

# 	</head>

# 	<body>
# 		<section>
# 			<div id ="" class=""name="test_div">
# 				<img src=".jpg">
# 				<p>This is sample text</p>
# 			</div>
# 		</section>


# 	</body>



# </html>

# requests => get or post 
# Beautifulsoup 

# pip install requests 
# pip install BeautifulSoup4

# import requests 
# from bs4 import BeautifulSoup
# url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore"
# response = requests.get(url)
# soup = BeautifulSoup(response.content,"html.parser")
# cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

# for card in cards:
	
# 	price = card.find("div",attrs={"class":"m-srp-card__price"})
# 	title  = card.find("a",attrs={"class":"m-srp-card__title"})
# 	link = title.get("href")
	
# 	response2 = requests.get(link)
# 	soup2 = BeautifulSoup(response2.content,"html.parser")
# 	agent = soup2.find("span",attrs={"class":"commercialName"})
# 	if agent:
# 		agent_text = agent.text.replace("\n"," ")
# 	else:
# 		agent_text = None	
# 	title_text = title.text.replace("\n"," ")
# 	carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
# 	data = "{} {} {} {}".format(title_text,price.text,carpet_area.text,agent_text)
# 	print(data)


# print(response)
# print(response.status_code)
# print(response.content)
# HTTP Status code 
# 200 ok 
# 404 Page not found 
# 400 Bad request 
# 500 Server errors 
# 403 forrbidden 

# soup = BeautifulSoup(response.content,"html.parser")
# # print(soup.prettify())
# # help(BeautifulSoup)
# # print(dir(BeautifulSoup))

# 			# 		soup 
# 			# 		HTML
# 			# head 			body 
# 			# 			section1 	section2
# 			# 		div1  div2
# 			# 		p img  a

# # price = soup.find("div",attrs={"class":"m-srp-card__price"})
# # print(price.text)


# # prices = soup.find_all("div",attrs={"class":"m-srp-card__price"})
# # # print(prices)

# # price_text = [price.text for price in prices]
# # print(price_text)

# cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})
# # print(card)

# for card in cards:
# 	price = card.find("div",attrs={"class":"m-srp-card__price"})

# 	title  = card.find("a",attrs={"class":"m-srp-card__title"})
# 	link = title.get("href")
# 	print(link)
# 	# print(title.text)


# 	title_text = title.text.replace("\n"," ")
# 	# print(title_text)

# 	carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
# 	# print(carpet_area.text)

# 	data = "{} {} {}".format(title_text,price.text,carpet_area.text)
# 	print(data)


def gen_payload(page_number):

	payload = {
		"propertyType_new":"10002_10003_10021_10022",
		"city": 3327,
		"mbTrackSrc": "homeSearchForm",
		"searchType": 1,
		"propertyType": "10002,10003,10021,10022",
		"category": "S",
		"page": page_number,
		"ltrIds": "37135469,37137229,36316913,31628459,35775147,35647279,37161547,36410767,34924657,34002751,33836989,37014165,34660657,36949791,20236698,37169509,35476813,35508537,33645591,35500143,36184143,36975103,21929323,36878073,30103997,36527847,17475128,34072951,37086683,37138757",
		}

	return payload

# payload = gen_payload(7)
# print(payload)
import requests 
from bs4 import BeautifulSoup
import csv
# help(requests.post)
# url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore"
# response = requests.post(url,data = payload)
# soup = BeautifulSoup(response.content,"html.parser")
# cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

# for card in cards:
	
# 	price = card.find("div",attrs={"class":"m-srp-card__price"})
# 	title  = card.find("a",attrs={"class":"m-srp-card__title"})
# 	# link = title.get("href")
	
# 	# response2 = requests.get(link)
# 	# soup2 = BeautifulSoup(response2.content,"html.parser")
# 	# agent = soup2.find("span",attrs={"class":"commercialName"})
# 	# if agent:
# 	# 	agent_text = agent.text.replace("\n"," ")
# 	# else:
# 	# 	agent_text = None	
# 	title_text = title.text.replace("\n"," ")
# 	carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
# 	data = "{} {} {}".format(title_text,price.text,carpet_area.text)
# 	print(data)
with open("magic_data2.csv","w",encoding = "utf-8") as fp:
	writer = csv.writer(fp,lineterminator ="\n")
	writer.writerow(['Property Title','Price','Carpet Area'])

	for page_number in range(1,11):
		payload = gen_payload(page_number)
		url = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore"
		response = requests.post(url,data = payload)
		soup = BeautifulSoup(response.content,"html.parser")
		cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

		for card in cards:
			l = []
			
			title  = card.find("a",attrs={"class":"m-srp-card__title"})
			# link = title.get("href")
			
			# response2 = requests.get(link)
			# soup2 = BeautifulSoup(response2.content,"html.parser")
			# agent = soup2.find("span",attrs={"class":"commercialName"})
			# if agent:
			# 	agent_text = agent.text.replace("\n"," ")
			# else:
			# 	agent_text = None	
			title_text = title.text.replace("\n"," ")
			l.append(title_text)
			price = card.find("div",attrs={"class":"m-srp-card__price"})
			l.append(price.text)
			carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
			l.append(carpet_area.text)
			# data = "{} {} {}".format(title_text,price.text,carpet_area.text)
			# print(data)
			writer.writerow(l)


fp.close()



