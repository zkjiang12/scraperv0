import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.instagram.com/")
content = BeautifulSoup(r.text, 'html.parser')

print(content.get_text())
# print(r.text.)