import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.yellowpages.com/search?search_terms=cafe&geo_location_terms=Los+Angeles%2C+CA")
r.content
soup = BeautifulSoup(r.content)
print soup.prettify()

for link in soup.find_all("a"):
	print link.text

