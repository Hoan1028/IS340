#recursive function traverses through an array to find the largest element
def largest(data) :
   if len(data) == 1 :
      return data[0]
   
   largestRest = largest(data[0 : -1])
   if largestRest < data[-1] :
      return data[-1]
   else :
      return largestRest

#recursive function traverses through an array to find the smallest element
def smallest(data):
   if len(data) == 1 :
      return data[0]
   
   smallestRest = smallest(data[0 : -1])
   if smallestRest > data[-1] :
      return data[-1]
   else :
      return smallestRest

def main() :
   # Demonstrate the largest function.
   print(largest([10, 12, 33, 8, 52, 49, 23, 14, 1]))
   print("Expected: 52")    
   # Demonstrate the smallest function.
   print(smallest([10, 12, 33, 8, 52, 49, 23, 14, 1]))
   print("Expected: 1")

# Call the main function.
main()
