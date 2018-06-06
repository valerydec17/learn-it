import pickle
import requests
from bs4 import BeautifulSoup

# Getting back the objects:
with open('objs.pkl') as f:  # Python 3: open(..., 'rb')
    content = pickle.load(f)

print content

soup = BeautifulSoup(content)
# links = soup.find_all("a")