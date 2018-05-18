#!/usr/bin/env python3

# Homework Assignment 1 side project
# Requirements: Parse an input document, list the words in order, case insensitive, get rid of 
# sentence punctuation, include word punctuation
# Owner: Dominic Pontious

# Importing sys for commmand line interfacing
import sys

# Importing os.path for .isfile() func
import os.path

# Importing re to parse input document
import re

# Importing operator for sort function
import operator

def getWords(text):
	"""
	Takes in a string and edits it to have no punctuation, be all lower case, and include words that have - or '
	 then seperates each word into a list of strings and returns this list
	Input: text <str>
	Output: words [<str>]
	"""

	# This takes all upper case letters and lowers them
	lowered = text.lower()

	# Gets rid of all punctuation and new lines
	lowered = re.sub("[!.,?"":;\n]", " ", lowered)

	# Gets rid of two or more - and replaces with a space
	lowered = re.sub(r"--+", " ", lowered)

	# Takes quotes off words
	lowered = re.sub(r"'([a-zA-Z'-]+)'", r"\1", lowered)

	# This uses findall() to create my list searching for anything that is a word containing: letters, ' and -
	words = re.findall(r"[a-zA-Z'-]+", lowered)

	return words

class wordClass(object):
	"""
	Variables:
				word <str>
				count <int>
	Methods:
				__init__(self,word,count) initializes the wordClass
				plusCount(self) increments the count variable
				displayData print statement for the variables
				getWord returns word
				getCount returns count
	"""

	def __init__(self, word, count = 1):
		"""
		Initializes the wordClass with the word which was input and a count of 1 unless overridden
		Input: 	word <str>
				count <int>
		Output: None
		"""

		self.word = word
		self.count = count

	def plusCount(self):
		"""
		Increments the variable count contained in the wordClass
		Input: None
		Output: None
		"""
		self.count += 1

	def displayData(self):
		"""
		A print function to display the two variables word and count
		Input: None
		Output: None
		"""

		print(self.word + ": " + str(self.count))

	def getWord(self):
		"""
		A getter function for the word variable
		Input: None
		Output: word <str>
		"""

		return self.word

	def getCount(self):
		"""
		A getter function for the word variable
		Input: None
		Output: count <int>
		"""

		return self.count

def main():
	"""
	Takes in command line argument for the document to be read in and ignore file, checks for the correct number of arguments
	 verifies that we can work with the given files. Turns files into a list of strings
	 Turns ignoreFile into a dictionary of wordClass objects with key as word <str>
	 Reads list of strings into a dictionary and list of wordClass objects
	 If the wordClass is in the ignoreDictionary skips this word
	 If there is a duplicate word increments the count variable using the dictionary
	 Sorts the list of wordClass objects
	 Writes the sorted list to a txt document
	 Reads the written document in the command line
	"""

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

	# List of wordClass to be sorted later
	wordList = []

	# dictionary, key is a string, value is wordClass
	wordDictionary = {}

	excludeDictionary = {}

	# Modifies input file, see function getWords()
	newFileList = getWords(myFile)

	excludeList = getWords(excludeFile)

	for exclude in excludeList:

		# This checks if word is already in dictionary
		if (exclude in excludeDictionary):

			pass

		# If the word is not in the dictionary add it
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
	
	# Uses Python sort func, first parameter is wordList, second parameter specifies what attribute to sort by, in this case the count
	sortedList = sorted(wordList, key=operator.attrgetter('count'))


	with open("outputExclude.txt", mode = 'w') as WRITE_FILE:

		# Writes sorted wordList into a document
		for wordObj in sortedList:

			WRITE_FILE.write(wordObj.getWord() + " : " + str(wordObj.getCount()) + "\n")

	WRITE_FILE.close()

	# This opens the above file and prints the contents
	with open("outputExclude.txt", mode = 'r') as OUTPUT_FILE:

		print (OUTPUT_FILE.read())

	OUTPUT_FILE.close()


# This is just a check to make sure the script is being handled correctly
if (__name__ == "__main__"):
	main()

else:
	print("improper use of the script!")