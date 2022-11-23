import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)
joke = response.json()["value"]
print(joke)

key = "22864cfe9725addf36bc446ab0dee2d8"
municipality = input("Enter the name of the municipality:")
request = "https://api.openweathermap.org/data/2.5/weather?q=" + municipality + "&appid="+key+"&units=metric"

try:
    response = requests.get(request)
    weather = response.json()
    print(f"The weather in {municipality} is {weather['weather']} and the temperature is"
          f"{weather ['main']['temp']} degrees Celsius")

except requests.exceptions.RequestException as e:
    print("Request could not be completed")