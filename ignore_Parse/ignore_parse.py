#!/usr/bin/env python3


# Importing sys for commmand line interfacing
import sys

# Importing os.path for .isfile() func
import os.path

# Importing re to parse input document
import re

# Importing operator for sort function
import operator

# getWords() func inputs text and returns a list of words which have been lower cased and punctuation removed
def getWords(text):

	# This takes all upper case letters and lowers them
	lowered = text.lower()

	# Gets rid of all punctuation and new lines
	lowered = re.sub("[!.,?"":;\n]", " ", lowered)

	# Gets rid of -- and replaces with a space
	lowered = re.sub("--", " ", lowered)

	# Takes quotes off words
	lowered = re.sub(r"'([a-zA-Z'-]+)'", r"\1", lowered)

	# This uses findall() to create my list searching for anything that is a word containing: letters, ' and -
	words = re.findall(r"[a-zA-Z'-]+",lowered)

	return words

# Class to hold a word and count
class wordClass(object):

	# Initialize a word input and 1 count
	def __init__(self, word, count = 1):
		self.word = word
		self.count = count

	# Func to increase count
	def plusCount(self):
		self.count += 1

	# Print variables in class
	def displayData(self):
		print(self.word + ": " + str(self.count))

	# Getters to not directly call variables
	def getWord(self):
		return self.word

	def getCount(self):
		return self.count

def main():

	# Checks to ensure there are exactly two command line arguments
	if (len(sys.argv) != 3):

		print("This script needs three arguments, this, the text being read in, and the ignore file. You input: ", len(sys.argv), "arguments.")

		# Exits the script with an error number
		sys.exit(1)

	# This is a check to make sure the input is actually a file
	if (os.path.isfile(sys.argv[1])):

		# This is to save myself a local copy of the contents of the file and then close the original
		with open(sys.argv[1], mode = 'r') as READ_FILE:

			myFile = READ_FILE.read()

		READ_FILE.close()

	# An error check if the input was not a file
	else:

		print("Your input has to be a file we can access and it does not appear to be")
		sys.exit(2)

	# This is a check to make sure the input is actually a file
	if (os.path.isfile(sys.argv[2])):

		# This is to save myself a local copy of the contents of the file and then close the original
		with open(sys.argv[2], mode = 'r') as READ_FIL:

			excludeFile = READ_FIL.read()

		READ_FIL.close()

	# An error check if the input was not a file
	else:

		print("Your input has to be a file we can access and it does not appear to be")
		sys.exit(3)




	# List of wordClass to be sorted later
	wordList = []

	# dictionary, key is word string, value is wordClass
	wordDictionary = {}

	excludeDictionary = {}

	# Modifies input file, see function getWords()
	newFileList = getWords(myFile)

	excludeList = getWords(excludeFile)

	for exclude in excludeList:

		# This checks if word is already in dictionary
		if (exclude in excludeDictionary):

			pass

		# If the word is not in the dictionary it is also not in the list
		else:

			# Instances a wordClass with key: word
			excludeDictionary[exclude] = wordClass(exclude)


	# Loop through every element in modified input list
	for word in newFileList:

		if (word in excludeDictionary):
			pass

		# This checks if word is already in dictionary
		elif (word in wordDictionary):

			# If word is in dictionary increases count in wordClass for associated word
			wordDictionary[word].plusCount()

		# If the word is not in the dictionary it is also not in the list
		else:

			# Instances a wordClass with key: word
			wordDictionary[word] = wordClass(word)

			# Appends the same wordClass instance to the wordList
			wordList.append(wordDictionary[word])
	
	# Uses Python sort func, first parameter is wordList, second parameter specifies what attribute to sort by, in this case the word
	sortedList = sorted(wordList, key=operator.attrgetter('count'))


	with open("outputWithExclude2.txt", mode = 'w') as WRITE_FILE:

		# Writes sorted wordList into a document
		for wordObj in sortedList:

			WRITE_FILE.write(wordObj.getWord() + " : " + str(wordObj.getCount()) + "\n")

	WRITE_FILE.close()

	# This opens the above file and prints the contents
	with open("outputWithExclude2.txt", mode = 'r') as OUTPUT_FILE:

		print (OUTPUT_FILE.read())

	OUTPUT_FILE.close()


# This is just a check to make sure the script is being handled correctly
if (__name__ == "__main__"):
	main()

else:
	print("improper use of the script!")