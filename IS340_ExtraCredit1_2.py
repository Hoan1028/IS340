#Ch 3. Decisions Problem 2
#Program takes user name, wage, hours and prints total pay
def main():
        #prompt user for input and initialize pay variable
	name = input("Enter name:")
	wage = float(input("Enter wage:"))
	hours = float(input("Enter hours:"))
	pay = 0.0
	#calculate wage with overtime and without
	if hours > 40:
		pay = (40*wage) + (hours-40) * (wage * 1.5)
	else:
		pay = hours * wage
	#print total pay
	print("Total pay is: $",pay)

main()
