#5 . Program reads from text file, creates dictionary of words with word count
from re import split

def main():
	#declare variables
	wordctr = 1
	wordDic = {}
	#open textfiles
	infile = open("input.txt", "r")
	#read textfile and sort words into dictionary
	for line in infile:
		line = line.strip()
		parts = split("[^a-zA-Z]+",line)
		for word in parts:
			if len(word) > 0:
				if word in wordDic:
					wordDic[word]= wordctr + 1
				else:
					wordDic[word]= wordctr
	#close all textfiles
	infile.close()

	print(wordDic)

main()
