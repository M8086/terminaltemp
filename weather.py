import urllib.request
import json

SECRET = ""
LATITUDE = ""
LONGITUDE = ""

def temperature_report():
    weather_source = urllib.request.urlopen(f"https://api.darksky.net/forecast/{SECRET}/{LATITUDE},%20{LONGITUDE}").read() 

    weather_data = json.loads(weather_source)
    temperature = weather_data["currently"]["temperature"]
    print(int(temperature))

if __name__ == "__main__":
    temperature_report()
