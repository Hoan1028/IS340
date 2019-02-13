#Hoan Nguyen
#013422030
'''
print("2.")
#2.
#Read float-type user input
num1 = float(input("Please enter any real number:"))
#compare and print zero if equal to 0
if num1 == 0:
    print(num1,"is zero")
#compare and print positive if greater than 0
if num1>0:
    print(num1,"is positive")
    if num1<1:
        print("and small")
    else:
        print("and large")
#compare and print negative if less than 0
if num1<0:
    print(num1,"is negative")
    if num1>-1:
        print("and small")
    else:
        print("and large")

print("3.")
#3.
#Read integer-type user input
num2 = abs(int(input("Enter any integer:")))
if num2<10:
    print("1 digit")
elif num2<100:
    print("2 digits")
elif num2<1000:
    print("3 digits")   
elif num2<10000:
    print("4 digits")
elif num2<100000:
    print("5 digits")
elif num2<1000000:
    print("6 digits")
elif num2<10000000:
    print("7 digits")
elif num2<100000000:
    print("8 digits")
elif num2<1000000000:
    print("9 digits")
elif num2<10000000000:
    print("10 digits")
else:
    print("number greater than 10 digits")
'''
print("4.")
#4.
#define variables that take input 
int1 = int(input("Enter the first digit:"))
int2 = int(input("Enter the second digit:"))
int3 = int(input("Enter the last digit:"))
#compare inputs
print(int1,int2,int3)
if int1 == int2 and int2 == int3:
    print("all are the same")
elif int1 == int2 or int1 == int3:
    print("neither")
else:
    print("all are different")
'''
print("5.")
#5.
#define input variables
time1 = input("Enter Time 1:")
time2 = input("Enter Time 2:")
#remove ':' and parse string into an integer
time1 = int(time1.replace(":",""))
time2 = int(time2.replace(":",""))
#compare integers for numerical order
if time1 < time2:
    print("Time 1 comes first")
elif time1 > time2:
    print("Time 2 comes first")
else:
    print("times are the same")

print("6.")
#6.
#Declare input variables
str1 = input("Enter a string:")
str2 = input("Enter a second string:")
str3 = input("Enter a third string:")
#Compare lexicographic priority
if str1 > str2 and str1 > str3:
    if str2 > str3:
        print(str3,str2,str1)
if str2 > str1 and str2 > str3:
    if str3 > str1:
        print(str1,str3,str2)
if str3 > str1 and str3 > str2:
    if str1 < str2:
        print(str1,str2,str3)
if str1 > str3 and str1 < str2:
    if str3 < str2:
        print(str3,str1,str2)
if str2 < str1 and str2 < str3:
    if str1 < str3:
        print(str2,str1,str3)
if str2 < str1 and str2 < str3:
    if str1 > str3:
        print(str2,str3,str1)
'''


        



