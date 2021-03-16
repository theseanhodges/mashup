from bs4 import BeautifulSoup
import requests

html = requests.get('http://unkno.com/')
parser = BeautifulSoup(html.content, 'html.parser')

quote = parser.find('div', id='content').getText().strip()