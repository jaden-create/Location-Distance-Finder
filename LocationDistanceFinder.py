{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "61f3701b-6798-476c-aa0a-c3d0a3cfc8ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi, I will find the distance between two locations for you in Kilometers\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter 'm' for Miles or 'km' for Kilometers m\n",
      "please enter your first location: india\n",
      "please enter your second location: Russia\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3048.9719 Miles\n"
     ]
    }
   ],
   "source": [
    "#Find the distance between any two locations\n",
    "#must install geopy before running code\n",
    "from geopy import Nominatim\n",
    "from geopy.distance import geodesic\n",
    "geolocator = Nominatim(user_agent = \"Your@email.com\")\n",
    "print(\"Hi, I will find the distance between two locations for you in Kilometers\")\n",
    "while True:\n",
    "    unit = input(\"Please enter 'm' for Miles or 'km' for Kilometers\").lower()\n",
    "    if unit == 'm' or unit == 'km':\n",
    "        break\n",
    "    else:\n",
    "        print(\"Please follow the instructions and choose a unit of measurment\")\n",
    "while True:\n",
    "    location1 = input(\"please enter your first location:\")\n",
    "    if geolocator.geocode(location1) is None:\n",
    "        print(\"You did not enter a valid location, please try again :)\")\n",
    "    else:\n",
    "        l1 = (geolocator.geocode(location1).latitude,geolocator.geocode(location1).longitude)\n",
    "        break\n",
    "while True:\n",
    "    location2 = input(\"please enter your second location:\")\n",
    "    if geolocator.geocode(location2) is None:\n",
    "        print(\"You did not enter a valid location, please try again :)\")\n",
    "    else:\n",
    "        l2 = (geolocator.geocode(location2).latitude,geolocator.geocode(location2).longitude)\n",
    "        break\n",
    "if unit =='m':\n",
    "    print(str(geodesic(l1,l2).miles)[:9]+\" Miles\")\n",
    "else:\n",
    "    print(str(geodesic(l1,l2).km)[:9]+\" Kilometers\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdbd7ffa-6a40-4be3-8f94-a5b211fc1837",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
