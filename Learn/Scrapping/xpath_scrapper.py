import requests
from bs4 import BeautifulSoup
from lxml import html

page = requests.get('https://alternativeto.net/software/adobe-photoshop/')
tree = html.fromstring(page.content)

software = tree.xpath('/html/body/form/section/div[2]/header/div[1]/div/h1')

software2 = tree.xpath('//*[@id="appHeader"]/div[1]/div/h1')

software3 = tree.xpath('//*[@id="appHeader"]/div[1]/div/h1/text()')

likes = tree.xpath('/html/body/form/section/div[2]/header/div[1]/div/div/div[2]/span/text()')

description = tree.xpath('/html/body/form/section/div[2]/header/div[1]/div/p/text()')

'/html/body/form/div[3]/main/div/div[3]/div/div/ul/li[1]/article/div[1]/h3/a/text()'
tree.xpath('/html/body/form/div[3]/main/div/div[3]/div/div/ul/li[1]/article/div[1]/h3/a/text()')


'/html/body/form/div[3]/main/div/div[3]/div/div/ul/li[17]/article/div[1]/h3/a/text()'
print software