#2. Program reads from a text file and sends the lines preceded by line numbers to another textfile.
def main():
	#declare variables
	linectr = 1
	#open textfiles
	infile = open("input.txt", "r")
	outfile = open("output.txt", "w")
	#read input lines, add line numbers then write to output file
	line = infile.readline()
	while line != "":
		value = "/*"+str(linectr)+"*/"
		outline = (line.rstrip())
		outfile.write(value + outline + "\n" )
		linectr = linectr+1
		line = infile.readline()

	#close all textfiles
	infile.close()
	outfile.close()

main()
