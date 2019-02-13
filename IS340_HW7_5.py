#5. Program reads float-type user input, handles errors twice, prints sum 
def main():
    #define variables
	errorTotal = 2
	sumCtr = 0
	#loop for userInput, break after 2 errors
	while errorTotal != 0:
		try:
			num = float(input("Enter any number:"))
			sumCtr = sumCtr + num
		except ValueError:
			print("Error:Please only input a number", )
			errorTotal = errorTotal-1
	#print sum of floats
	print("Total sum is:"+ str(sumCtr))
main()

