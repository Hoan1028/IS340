#recursive function traverses through a string to find a substring

def main():
   text = "Mississippi"
   ctr = len(text)
   string = "iss"
   while ctr >= len(string):
      print(text)
      print(text[0:len(string)])
      if text[0:len(string)].lower() == string.lower():
          print(True)
      text = text[1:]
      ctr = ctr - 1


# Call the main function.  [0,len(string)]
main()
