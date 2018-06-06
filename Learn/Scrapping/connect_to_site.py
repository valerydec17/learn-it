import requests
from bs4 import BeautifulSoup
import pickle

url = "https://alternativeto.net/"
r = requests.get(url)
r.content

# obj0, obj1, obj2 are created here...

# Saving the objects:
with open('objs.pkl', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([content], f)



