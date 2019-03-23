import requests as r
from bs4 import BeautifulSoup as b



requête = r.get("http://www.meteofrance.com/previsions-meteo-france/paris-15e-arrondissement/75015")
html = requête.content

soup = b(html, 'html.parser')

temp_day = soup.select(".day-summary-temperature")[0]
ciel = soup.select(".day-summary-label")[0]
print(temp_day.text)
print(ciel.text)

