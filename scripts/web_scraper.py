# from bs4 import BeautifulSoup
# from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--user-data-dir=/tmp/selenium_user_data")

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service = service, options = chrome_options)
# session = HTMLSession()
url = " https://www.cnbc.com/world/?region=world"
# session.browser_args = {'executablePath': '/usr/bin/chromium-brower'}
# r = session.get(url)
# r.html.render()
# html = r.html.raw_html
# soup = BeautifulSoup(html, "html.parser")
driver.get(url)
html = driver.page_source

raw_data_path = "../data/raw_data/web_data.html"
with open(raw_data_path, "w", encoding = 'utf-8') as file:
	# file.write(soup.prettify())
	file.write(html)
driver.quit()

