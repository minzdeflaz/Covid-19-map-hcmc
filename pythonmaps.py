# pip install -U googlemaps (vscode)
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="INSERT_KEY_HERE_FOLKS")

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(geocode_result[0]['address_components'][1]['long_name'])

from googlemaps import convert

pos = gmaps.geocode("Ho Chi Minh City, Vietnam")
print(pos[0]['address_components'])
print(pos[0]['geometry']['location'])

# Reverse geocode
#reverse_card = gmaps.reverse_geocode((pos[0]['geometry']['location']['lat']), pos[0]['geometry']['location']['lng'])
reverse_card = gmaps.reverse_geocode([10.8230989, 106.6296638])
print(reverse_card)
