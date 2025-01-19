from bs4 import BeautifulSoup
# from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

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

WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "MarketCard-row")))
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

market_banner = soup.find("div", class_ = "MarketsBanner-marketData").prettify()

resp = requests.get(url)
latest_soup = BeautifulSoup(resp.text, "html.parser")
latest_news = latest_soup.find("ul", class_="LatestNews-list").prettify()

raw_data_path = "../data/raw_data/web_data.html"
with open(raw_data_path, "w", encoding = 'utf-8') as file:
	# file.write(soup.prettify())
	file.write(market_banner)
	file.write("\n\n")
	file.write(latest_news)



