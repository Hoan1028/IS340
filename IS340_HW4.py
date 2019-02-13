'''
#2.
#Take user input of type integer
int1 = int(input("Enter any integer:"))
#set sentinel value and initialize variables
sent1 = -1
min = 0
first = True
#while loop is not broken replace min if input is smaller
while int1 != -1:
    if first == True:
        min = int1
        first = False
    elif int1 < min:
        min = int1
    int1 = int(input("Enter any integer:"))
#print minimum
print("The smallest number is:",min)

#3.
#initialize variables
#take user input of type float
large = 0.0
counter = 1
int2 = float(input("Enter any decimal value, -1 to quit:"))
small = int2
total = int2
#update variables and take user input until sentinel
while int2 != -1:
    int2 = float(input("Enter any decimal value, -1 to quit:"))
#break while loop if -1 detected
    if int2 == -1:
        break
    counter = counter + 1
    total = total + int2
    if int2 > large:
        large = int2
    elif int2<small:
        small = int2
#calculate range of current max and min before printing
rnge = abs(large)-abs(small)
#print calculations
print("average:",total/counter," smallest:",small," largest:",large,"range:",rnge)

#4.
#take user input and initialize index counter
str1 = input('Enter a word:')
indx = 0
#while index has not reached string length value, print char at index position
while indx != len(str1):
    print(str1[indx])
    #update index position
    indx = indx+1

#5.
#define and initialize variables
multcand = 1
#while loop for 10 multiplicands
while multcand <=10:
    multplr = 1
    #while loop for 10 multipliers
    while multplr <=10:
            print(multcand*multplr)
            multplr = multplr+1
    print("")
    multcand=multcand+1
    '''
#6.
#take user input string
str2 = input("Enter a string:")
counter = 0
#for loop goes through each index and prints uppercase letters
for i in range(len(str2)):
    if str2[i].isupper():
        print(str2[i])




    
    
