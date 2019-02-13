#recursive function traverses through a string to find a substring
def find(text, string):
   #compares initial text characters to substring
   if text[0:len(string)].lower() == string.lower():
      return True
   #compares text to substring if text length is equal or longer
   if len(text) >= len(string):
      return find(text[1:], string)
   else:
      return False


def main() :
   # Demonstrate the find function.
   print(find("Mississippi", "sip"))
   print("Expected: True")

   print(find("Mississippi", "pip"))
   print("Expected: False")

# Call the main function.  [0,len(string)]
main()
