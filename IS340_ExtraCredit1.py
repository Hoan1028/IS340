def main():
	userInput = input("Enter a letter grade:")
	letter = userInput[0]
	if len(userInput) > 1:
		sign = userInput[1]
	else:
		sign = ""
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
	else:
		print("No such grade")
	if sign == "+" and letter != "F":
		if letter != "A":
			points = points + 0.3
	elif sign == "-" and letter != "F":
		points = points - 0.3
	print(points)

main()
