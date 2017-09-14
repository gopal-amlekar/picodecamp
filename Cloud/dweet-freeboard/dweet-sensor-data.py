import sys
sys.path.append('../../')

from Sensors-Actuators.Distance-Sensors import hcsr04

distance = hcsr04.get_distance()
