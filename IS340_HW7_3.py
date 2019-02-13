#3. Program reads from a text file prompted by user and prints averages
def main():
	#declare variables
	total = 0.0
	avg1 = 0.0
	avg2 = 0.0
	#open textfiles
	userfile = str(input("Enter the file name:"))
	infile = open(userfile, "r")
	#read input lines, sort column values and update column totals
	line = infile.readline()
	while line != "":
		currentline = line.split()
		avg1 = avg1 + float(currentline[0])
		avg2 = avg2 + float(currentline[1])
		total = total + 1
		line = infile.readline()
	#print avg calculations
	print("The averages are:",avg1/total,"and",avg2/total)
	#close all textfiles
	infile.close()

main()
