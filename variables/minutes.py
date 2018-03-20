"""
Write a program that prints out the number
 of minutes in seven weeks.
 """

def minutes_in_week(number):
	""" Taes number of weeks as input and returns 
	the total number of minutes """
	days = 7
	hours_in_day = 24
	minutes_in_hour = 60
	minutes_in_a_week = days *  hours_in_day * minutes_in_hour
	answer = number * minutes_in_a_week

	return answer

print minutes_in_week(7)