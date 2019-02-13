#3. Program reads two strings for lowercase letters,
#prints missing lowercase letters from alphabet
#take user input and print result
def main():
	userIn = (input("Enter the first string:"))
	userIn2 = (input("Enter the second string:"))
	print (notInEither(userIn,userIn2))
#takes two string's letters and compares them to alphabet to find missing ones
	#returns a set of missing lowercase letters
def notInEither(str1,str2):
	fullSet = letters("abcdefghijklmnopqrstuvwxyz")
	commonSet = letters(str1).union(letters(str2))
	missingSet = fullSet.difference(commonSet)
	return missingSet
#function turns strings into set of lowercase letters
def letters(str1):
        #initialize set
	validchar = set()
	#traverse string and check for lowercase letters. Add letters to set
	for character in str1:
		if character.isalpha():
			if character.islower():
				validchar.add(character)
	#return set with letters from string
	return validchar
main()

