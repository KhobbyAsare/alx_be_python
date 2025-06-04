import requests

x = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=0aacbeedbc806a3c45b071cf322f85e6')

print(x.text)
