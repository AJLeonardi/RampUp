# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Anthony Leonardi

def read_file():
	fin =open('words.txt')
	for line in fin:
		#word =fin.readline()
		if len(line.strip()) >19:
			print line

def has_no_e(str):
	if 'e' in str:
		return False
	else:
		return True
def avoids(word, forbidden):
	for c in word:
		if c in forbidden:
			return False
	return True

def read_file_avoids(forbidden):
	fin = open('words.txt')
	count = 0
	for line in fin:
		if avoids(line.strip(), forbidden):
			count += 1
	return count

def prompt_user():
	forbidden = raw_input("enter a string of forbidden letters: ")
	print read_file_avoids(forbidden)

def uses_only(word, allowed):
	for c in word:
		if c not in allowed:
			return False
	return True

print uses_only('alfalfa', 'alf')
print uses_only('anthony', 'the')
#prompt_user()

"""read_file()
print has_no_e('this')
print has_no_e('there')
print avoids('hello', 'abcde')
print avoids('hello', 'abcd')"""