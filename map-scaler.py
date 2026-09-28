import math
import urllib.request
import json

def get_country_size(country):
    url = f"https://restcountries.com/v3.1/name/{country}?fields=area"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        area = data[0]["area"]
        side_km = math.sqrt(area)
        return side_km, side_km

def get_scale(real_km, paper_cm):
    real_cm = real_km * 100000
    ratio = real_cm / paper_cm
    rounded_scale = math.ceil(ratio / 50000) * 50000
    return rounded_scale

name = input("Enter country: ")
paper = float(input("Enter paper length in cm: "))

side, _ = get_country_size(name)
scale = get_scale(side, paper)

print(f"Scale is 1:{scale:,}")
