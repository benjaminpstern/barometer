import requests

weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

sf_lat = "37.7749"
sf_lon = "-122.4194"
wl_lat = "43.4668"
wl_lon = "-80.5164"
low_pressure = 1000
PRESSURE_LOW = "LOW"
PRESSURE_HIGH = "HIGH"
PRESSURE_MID = "MID"
high_pressure = 1030

def main():
    api_key = input("Your openweathermap.org API key:")
    pressure = pressure_for_coords(sf_lat, sf_lon)
    print("SF Pressure: " + str(pressure) + " which is " + pressure_heuristic(pressure))
    pressure = pressure_for_coords(wl_lat, wl_lon)
    print("Waterloo Pressure: " + str(pressure) + " which is " + pressure_heuristic(pressure))

def pressure_heuristic(pressure):
    if pressure < low_pressure:
        return PRESSURE_LOW
    if pressure > high_pressure:
        return PRESSURE_HIGH
    return PRESSURE_MID

def pressure_for_coords(lat, lon):
    request_url = weather_api_url + "?" + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key
    r = requests.get(request_url)
    data = r.json()
    return data.get("main").get("pressure")

main()
