import sys
sys.path.append('../../')

import requests # This must be installed with pip install requests (or pip3 for python 3)

Dweet_Thing_Name = "RaspiDweets"
Dweet_Base_URL = "https://dweet.io/dweet/for/"
Dweet_For_URL = Dweet_Base_URL + Dweet_Thing_Name + "?"

dweet_data = {'Name': 'Sensors'}

from devices.distancesensors import hcsr04

distance = hcsr04.get_distance()

print ("Distance is {0} cm".format(distance))

distance.append({'Distance': distance})

r = requests.post(Dweet_For_URL, data=dweet_data)

print (r)
