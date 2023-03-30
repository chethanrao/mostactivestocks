import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/most-active/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table")
rows = table.tbody.find_all("tr")

for row in rows:
    cells = row.find_all("td")
    symbol = cells[0].text.strip()
    name = cells[1].text.strip()
    price = cells[2].text.strip()
    change = cells[3].text.strip()
    percent_change = cells[4].text.strip()
    volume = cells[6].text.strip()

    print(f"{symbol} - {name}\nPrice: {price}\nChange: {change} ({percent_change})\nVolume: {volume}\n")
