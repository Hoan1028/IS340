#recursive function traverses through a string's length,
#concatinating every last element to the front in order to reverse string
def reverse(string):

   if len(string) <= 1:
      return string
   return reverse(string[1:len(string)]) + string[0]
def main() :
   # Demonstrate the reverse function.
   r = reverse("Hello!")
   print(r)
   print("Expected: !olleH")

# Call the main function.
main()   
