import requests as r
from bs4 import BeautifulSoup as b

requête = r.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
html = requête.content

soup = b(html, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
today = forecast_items[0]
print(today.text)
