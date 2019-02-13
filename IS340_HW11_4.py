#iterative function traverses through a string's length,
#concatinating every last element to the front in order to reverse string
def reverse(string):
   ctr = len(string)
   newString = ""
   for c in string:
      newString = c + newString
      ctr = ctr - 1
   return newString

def main() :
   # Demonstrate the reverse function.
   r = reverse("Hello!")
   print(r)
   print("Expected: !olleH")

# Call the main function.
main()   
