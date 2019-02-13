#2. Program takes 2 strings and returns a set of common letters
def main():
        #take user inputs and prints result from called functions
	userIn = (input("Enter the first string:"))
	userIn2 = (input("Enter the second string:"))
	print (lettersInBoth(userIn,userIn2))
#function takes two strings and returns common letters
def lettersInBoth(str1,str2):
	commonSet = letters(str1).intersection(letters(str2))
	return commonSet
#function takes a string and returns a set of letters
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

