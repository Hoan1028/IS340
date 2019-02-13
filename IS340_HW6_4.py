#6.
#Program uses a function to reverse the elements in a list without using the .reverse function from the python library
#Test Case: [1 4 16 9 7 4 9 11] output: [11 9 4 7 9 16 4 1]
def main():
	#defined list to reverse
	values = [1, 4, 16, 9, 7, 4, 9, 11]
	#call and display reverse function
	print(listReverse(values))

#function traverses list backwards and returns a new reversed list
def listReverse(alist):
	reverse = []
	for i in range(len(alist)-1, -1, -1):
		reverse.append(alist[i])
	return reverse

main()
