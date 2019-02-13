#1. Program writes into a file and then reads the file's content
def main():
    #Open file to write then close
	outfile = open("hello.txt", "w")
	outfile.write("Hello, World!")
	outfile.close()
    #Open file to read and print content then close
	infile = open("hello.txt", "r")
	line = infile.readline()
	print(line)
	infile.close()
main()
