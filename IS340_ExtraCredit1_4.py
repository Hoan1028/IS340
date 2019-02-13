#Ch 4. Loops Problem 4 
#Program prompts user tickets to be sold and displays remaining tickets until all are sold
def main():
	tixTotal = 20
	buyerCtr = 0
	while tixTotal != 0:
		print("There are currently",tixTotal,"tickets remaining.")
		buy = int(input("How many tickets would you like to purchase?"))
		if buy <=4:
			tixTotal = tixTotal - buy 
			buyerCtr = buyerCtr + 1
		else:
			print("Tickets limited to four per customer.")
	print("Total number of buyers was",buyerCtr)
main()
