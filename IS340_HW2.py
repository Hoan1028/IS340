#Hoan Nguyen MIS340 Assignment 2
#013422030

#2.
#Define Constant
CONST_NUM = 8
#Print Constant with power operators
print("\n2.")
print (CONST_NUM,"squared is:", CONST_NUM**2,"\n",
       CONST_NUM,"cubed is:", CONST_NUM**3,"\n",
       CONST_NUM,"to the fourth power is:", CONST_NUM**4)

#3.
#Define variables for width and height in inches
widthIn  =  8.5
heightIn =  11.0
#Print height and width in millimeters
print("\n3.")
print("The height in mm is", heightIn*24.3,"\n The width in mm is", widthIn*24.3)

#4.
#Prompt user input
print("\n4.")
int1 = int(input("Enter an Integer:"))
int2 = int(input("Enter an Integer:"))
#Print results from two integer inputs
print("The sum is", int1+int2,"\nThe difference is",int1-int2,
      "\nThe product is",int1*int2, "\nThe average is", (int1+int2)/2,
       "\nThe distance is", abs(abs(int1)-abs(int2)) ,
      "\nThe maximum is",max(int1,int2),"\nThe minimum is",min(int1,int2))

#5.
#Prompt a user to enter a string type
print("\n5.")
str1 = input("Please enter an integer between 10,000 and 99,999:")
#remove commas then parse string into int value
int3 = str1.replace(",","")
print(str(int3))

#6.
#Prompt user input and assign to variables
print("\n6.")
car_cost       = float(input("Enter cost of a new car:"))
miles_per_year = float(input("Estimate miles driven per year:"))
gas_price      = float(input("Estimate gas price:"))
efficiency     = float(input("Car's MPG:"))
resale         = float(input("Estimate 5 year resale value:"))
#Constant variable: 5 years
NUM_YEARS      = 5
#calculate total cost of hybrid
total_cost     = car_cost - resale + ((NUM_YEARS * miles_per_year)/(efficiency * gas_price))
#print total cost
print("Estimated 5 year total cost for your hybrid:",total_cost)
