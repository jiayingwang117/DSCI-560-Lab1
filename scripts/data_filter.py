from bs4 import BeautifulSoup
import csv

# Open raw HTML file and parse with BeautifulSoup
with open("../data/raw_data/web_data.html", "r") as file:
	soup = BeautifulSoup(file, "html.parser")

# Extract and filter market banner data
print("Filtering market banner data...")
market_data = []
market_banner = soup.find('div', class_ = "MarketsBanner-marketData")
market_cards =market_banner.find_all("a", class_ = "MarketCard-container")
#market_cards = soup.select('a.MarketCard-container')

# print(market_cards)

# Loop through each market card and extract symbol, stock position, and change percentage
for card in market_cards:
	symbol = card.find("span", class_ = "MarketCard-symbol").text
	stock_position = card.find("span", class_ = "MarketCard-stockPosition").text
	change_pct = card.find("div", class_ = "MarketCard-changeData").find("span", class_ = "MarketCard-changesPct").text
	market_data.append([symbol, stock_position, change_pct])

	# print(market_data)

# Extract and filter latest news data
print("Filtering latest news data...")
latest_news_data = []
latest_news_list = soup.find("ul", class_ = "LatestNews-list")
news_items = latest_news_list.find_all("li")

# Loop through each news and extract timestamp, title, and link
for item in news_items:
	timestamp = item.find("time", class_ = "LatestNews-timestamp").text.strip()
	title_tag = item.find("a", class_ = "LatestNews-headline")
	title = title_tag.text.strip()
	link = title_tag["href"]
	latest_news_data.append([timestamp, title, link])

# Save Data to CSV files
print("Storing Market Data...")
with open("../data/processed_data/market_data.csv", "w", newline = "") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["marketCard_symbol", "marketCard_stockPosition", "marketCard_changePct"])
	writer.writerows(market_data)
print("Market data CSV created")

print("Storing Latest News Data...")
with open("../data/processed_data/news_data.csv", "w", newline = "") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["LatestNews-timestamp", "Title", "Link"])
	writer.writerows(latest_news_data)
print("Latest News Data CSV created")
