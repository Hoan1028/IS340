#program uses mergesort to arrange a list in descending order
from random import randint
#test block
def main():
    #create a random list and then test the mergesort function
   n = 20
   values = []
   for i in range(n):
      values.append(randint(1,100))
   print(values)
   mergeSort(values)
   print(values)
#mergeSort function sorts a list using the merge sort algorithm
def mergeSort(values):
   if len(values) <= 1: 
      return
    #split the list into halves recursively
   mid = len(values) // 2
   first = values[:mid]
   second = values[mid:]
   mergeSort(first)
   mergeSort(second)
   #rearrange and merge
   mergeLists(first,second,values)
#merge the lists, priorizing larger values to create a descending order
def mergeLists(first,second,values):
   iFirst = 0
   iSecond = 0
   j = 0
   while iFirst < len(first) and iSecond < len(second):
      if first[iFirst] > second[iSecond]:
         values[j] = first[iFirst]
         iFirst = iFirst + 1
      else:
         values[j] = second[iSecond]
         iSecond = iSecond + 1
      j = j + 1
   while iFirst < len(first):
      values[j] = first[iFirst]
      iFirst = iFirst + 1
      j = j + 1
   while iSecond < len(second):
      values[j] = second[iSecond]
      iSecond = iSecond + 1
      j = j + 1
main()
