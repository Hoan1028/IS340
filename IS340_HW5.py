
#2. 
def main():
    #print result from function
    print(repeat("ho",3,","))
def repeat(string,n,delim):
    #initialize return variable
    newString = ""
    #loop for number in 2nd parameter, concatinate two string values
    #each loop updates newString value
    for i in range(n):
        newString = newString + string + delim
    return newString
main()

'''
#3.
def main():
    #same variable returns true when each variable equals the next
    def allTheSame(x,y,z):
        same = True
        if x == y and y == z:
            same = True
        else:
            same = False
        return same
    #diff variable returns true if each argument combo is not equal
    def allDifferent(x,y,z):
        diff = False
        if (x != y and x!=z) or (y != x and y!=z):
            diff = True
        else:
            diff = False
        return diff
    #sort returns true if each argument is smaller or equal to the next
    def sorted(x,y,z):
        sort = True
        if x<=y and y<=z:
            sort = True
        else:
            sort = False
        return sort
    #print results of different test cases
    print(allTheSame(1,2,3))
    print(allDifferent(1,2,3))
    print(sorted(1,2,3))
    print(allTheSame(2,2,2))
    print(allDifferent(2,2,2))
    print(sorted(2,2,2))
main()

#4.
def main():
    def countVowels(string):
        #initialize counter variable
        counter = 0
        #index in loop for every character in string
        #counter increases for each index detected as a vowel
        #before returning counter value
        for i in range(len(string)):
            if string[i] == 'a':
                counter = counter + 1
            elif string[i] == 'e':
                counter = counter + 1
            elif string[i] == 'i':
                counter = counter + 1
            elif string[i] == 'o':
                counter = counter + 1
            elif string[i] == 'u':
                counter = counter + 1
        return counter
    #print two example arguments
    print("The word has",countVowels("indiana"),"vowels")
    print("The word has",countVowels("california"),"vowels")
main()

#5.
def main():

    def readFloat(prompt):
        #function takes input then returns it
        floatIn = input((prompt))
        return floatIn
    #assign input to variables
    salary = readFloat("Please enter your salary:")
    percentageRaise = readFloat("What percentage raise would you like?")
    #print variable values
    print("The salary is", salary)
    print("The raise percentage is", percentageRaise)
    
main()        

#6. 
def main():
    
    def firstDigit(n):
        #parse integer into a string to extract first index
        #then parse it back into an int
        first = int(str(n)[0])
        return first
    def lastDigit(n):
        #parse integer into a string to extract last index
        #then parse it back into an int
        last = str(n)[len(str(n))-1]
        return last
    def digits(n):
        #parse integer into a string to use length function
        #then parse it back into an int
        numDig = len(str(n))
        return numDig
    #print return values
    print(firstDigit(1729))
    print(lastDigit(1729))
    print(digits(1729))

main()
'''
