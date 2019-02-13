#Ch 3. Decisions Problem 1
#Program takes letter grade input with option for signs to print numeric value
def main():
    #Prompt user input and store grade letter and sign separately
	userInput = input("Enter a letter grade:")
	letter = userInput[0]
	if len(userInput) > 1:
		sign = userInput[1]
	else:
		sign = ""
    #intialize points variable. Update points according to Letter then Sign
	points = 0.0
	if letter == "A":
		points = 4.0
	elif letter == "B":
		points = 3.0
	elif letter == "C":
		points = 2.0
	elif letter == "D":
		points = 1.0
	elif letter == "F":
		points = 0.0
    #Print error for invalid letter
	else:
		print("No such grade")
	if sign == "+" and letter != "F":
		if letter != "A":
			points = points + 0.3
	elif sign == "-" and letter != "F":
		points = points - 0.3
    #Print score
	print(points)

main()
