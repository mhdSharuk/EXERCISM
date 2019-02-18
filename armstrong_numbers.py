
def is_armstrong(number):
	sum = 0
	string = str(number)
	length = len(string)
	for num in string:
		sum = sum + int(num) ** length
	return number == sum


	
