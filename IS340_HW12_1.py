#program creates a random array and uses selectionsort to rearrange elements
#from largest to smallest
from random import randint
#test block
def main():
    #declare list of 20 elements and randomly generate numbers to fill it
   n = 20
   values = []
   for i in range(n):
      values.append(randint(1,100))
   print(values)
   selectionSort(values)
   print(values)

#selectionSort function sorts a list using the selection sort algorithm
def selectionSort(values):
   for i in range(len(values)):
      maxPos = maximumPosition(values, i)
      temp = values[maxPos] #Swap the two elements
      values[maxPos] = values[i]
      values[i] = temp
#function finds index of biggest element
def maximumPosition(values,start):
   maxPos = start
   for i in range(start+1, len(values)):
      if values[i] > values[maxPos]:
         maxPos = i
   return maxPos

main()
