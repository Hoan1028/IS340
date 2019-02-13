#program reads from a list of contacts to search for a name/number

#test block
def main():
   #open file
   openfile = open("contacts.txt","r")
   read = openfile.readlines()
   #creates two arrays and splits names from numbers
   names = []
   numbers = []
   for i in range(len(read)):
      string = read[i]
      result = string.split("|")
      names.append(result[0])
      numbers.append(result[1])
   #while loop that prompts user until user quits
   while(1):
      options = input("L)ookup Name, Lookup N)umber or Q)uit?")

      if options == "L" or options == "l":
         findName = input("Enter the Name:")
         if(binarySearch(names,findName)):
            print("Phone number is", numbers[names.index(findName)] )
      elif options == "N" or options == "n":
         findNum = input("Enter the number:")
         if(binarySearch(numbers,findName)):
            print("Name is:", names[numbers.index(findNum)])
         else:
            print("Not Found.")
      elif options == "Q" or options == "q":
         break

#Sort through a list by using binary search algorithm
def binarySearch(array,find):
   if len(array) == 0:
      return False
   else:
      mid = len(array)//2
      if array[mid] == find:
         return True
      else:
         if find < array[mid]:
            return binarySearch(array[:mid],find)
         else:
            return binarySearch(array[mid+1:],find)


main()
