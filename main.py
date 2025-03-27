import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


key = efe9bdc6f4f947cbad39ad0f3f217470
number = input(+15194104806)
new_number = phonenumbers.parse(number)
location = geocoder.description_for_number(new_number, "en")
print(location)

service_name = carrier.name_for_number(new_number,"en")
print(service_name)

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)
#print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat,lng)

my_map = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat, lng], popup= location).add_to(my_map)

my_map.save("location.html")

print("location tracking completed")
print("Thank you")
