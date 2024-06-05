"""
File: weather_master.py
Name: Jessie
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program asks weather data from user to compute the average, highest, lowest, cold days among the inputs.
	"""
	print('stanCode "Weather Master 4.0"! ')
	data = int(input('Next Temperature: (or -100 to quit)? '))
	if data == EXIT:
		print('No Temperatures were entered.')
	else:
		maximum = data
		minimum = data
		total_temperature = data
		count = 1
		cold_days = 0
		if data < 16:
			cold_days += 1
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data == EXIT:
				break
			maximum = max(maximum, data)
			minimum = min(minimum, data)
			total_temperature += data
			count += 1
			if data < 16:
				cold_days += 1
		average_temperature = total_temperature / count
		print('Highest temperature: ' + str(maximum))
		print('Lowest temperature: ' +str(minimum))
		print('Average : ' + str(average_temperature))
		print(str(cold_days)+ ' cold day(s)')





		# else:
		# 	minimum = data
		# 	while True:
		# 		data = int(input('Next Temperature: (or -100 to quit)? '))
		# 		if data == EXIT:
		# 			break
		# 		if data < minimum:
		# 			minimum = data
		# 	print('Lowest temperature: ' + str(minimum))








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
