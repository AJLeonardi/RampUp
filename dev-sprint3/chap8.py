# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Anthony Leonardi

def rotate_word(str, x):
	newString = ''
	for c in str:
		temp=ord(c)
		temp += x
		temp = chr(temp)
		newString += temp
	return newString

print rotate_word('cheer', 7)
