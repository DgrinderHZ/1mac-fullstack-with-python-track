"""
Write a program that prints out the
distance, in meters, that light travels in one processor
cycle.
speed_of_light = 299792458 m/s
cycles_per_second = 2700000000 = 2.7 GHz

"""

def distance_in_meters():
	speed_of_light = 299792458
	cycles_per_second = 2700000000.0
	cycle_distance = speed_of_light / cycles_per_second
	
	return cycle_distance

print distance_in_meters()