# Get route by ORS API
import requests

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}

API_KEY = "5b3ce3597851110001cf62485ffdfeda16fc426ebf09e2a68aa4de91"
START = {
    "longitude": 8.681495,
    "latitude": 49.41461
}
END = {
    "longitude": 8.687872,
    "latitude": 49.420318
}

url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={API_KEY}&start={START['longitude']},{START['latitude']}&end={END['longitude']},{END['latitude']}"
call = requests.get(url, headers=headers)

print(call.status_code, call.reason)
print(call.text) # geojson format

# Get route by OSRM API
import requests

START = {
    "longitude": 8.681495,
    "latitude": 49.41461
}
END = {
    "longitude": 8.687872,
    "latitude": 49.420318
}

url = f"http://router.project-osrm.org/route/v1/driving/{START['longitude']},{START['latitude']};{END['longitude']},{END['latitude']}?geometries=geojson"
osrm = requests.get(url)

print(osrm.status_code, osrm.reason)
print(osrm.json()) # geojson format routes