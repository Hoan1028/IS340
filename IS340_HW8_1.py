#1. Program reads string and only returns set of a-z,A-Z characters
def main():
	userIn = (input("Enter a string:"))
	print (letters(userIn))
#declare function
def letters(str1):
        #initialize set
	validchar = set()
	#traverse string and check for letters. Add letters to set
	for character in str1:
		if character.isalpha():
			validchar.add(character)
	#return set with letters from string
	return validchar
main()

