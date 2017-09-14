import sys
sys.path.append('../../')

from devices.distancesensors import hcsr04

distance = hcsr04.get_distance()
