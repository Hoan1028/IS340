#Ch 4. Loops 
#Program reads a word then prints it in reverse
def main():
	#assign a list to input
	values = input("Enter word:")
	#call and display reverse function
	print(listReverse(values))

#function traverses list backwards and returns a new reversed list
def listReverse(alist):
	reverse = []
	for i in range(len(alist)-1, -1, -1):
		reverse.append(alist[i])
	return reverse

main()
