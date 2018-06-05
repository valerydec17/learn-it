import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages.com/search?search_terms=cafe&geo_location_terms=Los+Angeles%2C+CA"
r = requests.get(url)

###
# r.content
# soup = BeautifulSoup(r.content)
# print soup.prettify()

# for link in soup.find_all("a"):
# 	print link.text


# for link in soup.find_all("a"):
# 	"<a href='%s'>%s</a>" %(link.get("href"), link.text)



soup = BeautifulSoup(r.content)
links = soup.find_all("a")

for link in links:
	print "<a href='%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("div", {"class": "info"})
#print g_data

for item in g_data:
	#print item.text
	#print item.contents[0].text
	print item.contents[0].find_all("a", {"class": "business-name"})[0].text
	
	try:
		print item.contents[0].find_all("p", {"class": "adr"})[0].text
		print item.contents[1].find_all("li", {"class": "primary"})[0].text			
	except:
		pass

	print item.contents[1].text



