#3.
#This program tests various functions that use a list as an argument
def main():
	#Define constant variables(list hardcoded)
	ONE_TEN = [1,2,3,4,5,6,7,8,9,10]
	print("The original data for all functions is:", ONE_TEN)

	#Demonstrate swapping the first and last element
	data = list(ONE_TEN)
	print("List with first and last elements swapped:",swapFirstLast(data))

	#Demonstrate all elements set to zero
	data1 = list(ONE_TEN)
	print("List with even elements set to zero:",zeroReplace(data1))

	#Demonstrate print the second largest element
	data2 = list(ONE_TEN)
	print("The second largest element:",secondLargest(data2))

	#Demonstrate print the second largest element
	data3 = list(ONE_TEN)
	print("Lists are sorted:",checkSort(data3))

#Function swaps first and last elements in the list
def swapFirstLast(firstLast):
    last = firstLast[len(firstLast)-1]
    first = firstLast[0]
    firstLast.pop()
    firstLast.pop(0)
    firstLast.insert(0,last)
    firstLast.append(first)
    return firstLast

#Function replaces all even elements with zero

def zeroReplace(listzero):
	for i in range(len(listzero)):
		if i%2 !=0:
			listzero[i] = 0
	return listzero

#Function returns second largest element in the list

def secondLargest(listSecond):
	listSecond.sort()
	return listSecond[len(listSecond)-2]
   
#Function returns true if list is sorted in increasing order

def checkSort(sortList):
	checkList = list(sortList)
	if sortList == checkList:
		return True 
	else:
		return False
main()

