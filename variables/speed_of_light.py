"""
Write a program that prints out how far light travels
in a centimeters in one nanosecond.

speed of light = 299 792 458 m/s
1 meter = 100 centimeters
1 second = 1 000 000 000 nanosecond
"""
def speed_of_light(distance):
	speed_of_light = 299792458
	answer = speed_of_light * 100 # centimeters/second
	answer = answer / 1000000000 # centimeters/nanosecond

	return answer

print (str(speed_of_light(1)) + " centimeters") # 1 meter