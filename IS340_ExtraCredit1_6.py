#Ch 5. Functions Problem 6
#Calculate ammount of financial assistance to provide
#Program continuosly prompts user until sentinel. First input is income, second is # of children
def main():
    #while loop to prompt user and call function
	print("Please enter values, -1 to quit:")
	userInput = 0
	while userInput != -1:
		userInput = input("")
		famInc = (float(userInput))
		userInput = input("")
		famChildren = (float(userInput))
		print(computeAssistance(famInc, famChildren))
#takes income and children and returns amount to grant
def computeAssistance(income, children):
	inc = income
	chd = children
	if inc >= 30000 and inc <=39999:
		return chd*1000
	elif  inc >= 20000 and inc <=29999:
		return chd*1500
	elif  inc < 20000:
		return chd*2000
	else:
		return "No assistance"
main()
