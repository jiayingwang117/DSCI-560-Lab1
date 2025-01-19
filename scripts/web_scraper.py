import requests
from bs4 import BeautifulSoup

url = " https://www.cnbc.com/world/?region=world"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
pretty_html = soup.prettify()

raw_data_path = "../data/raw_data/web_data.html"
with open(raw_data_path, "w") as file:
	file.write(pretty_html)

