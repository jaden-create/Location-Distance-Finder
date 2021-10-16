#Find the distance between any two locations
#must install geopy before running code
from geopy import Nominatim
from geopy.distance import geodesic
geolocator = Nominatim(user_agent = "Your@email.com")#enter your email here
print("Hi, I will find the distance between two locations for you in Kilometers")
while True:
    unit = input("Please enter 'm' for Miles or 'km' for Kilometers").lower()
    if unit == 'm' or unit == 'km':
        break
    else:
        print("Please follow the instructions and choose a unit of measurment")
while True:
    location1 = input("please enter your first location:")
    if geolocator.geocode(location1) is None:
        print("You did not enter a valid location, please try again :)")
    else:
        l1 = (geolocator.geocode(location1).latitude,geolocator.geocode(location1).longitude)
        break
while True:
    location2 = input("please enter your second location:")
    if geolocator.geocode(location2) is None:
        print("You did not enter a valid location, please try again :)")
    else:
        l2 = (geolocator.geocode(location2).latitude,geolocator.geocode(location2).longitude)
        break
if unit =='m':
    print(str(geodesic(l1,l2).miles)[:9]+" Miles")
else:
    print(str(geodesic(l1,l2).km)[:9]+" Kilometers")
