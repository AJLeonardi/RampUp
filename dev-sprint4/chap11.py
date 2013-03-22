#Anthony Leonardi

def build_list_append():
	fin =open('words.txt')
	t = []
	for line in fin:
		line = line.strip()
		t.append(line)
	return t

wordList = build_list_append()

def build_dictionary(List):
	''' builds a dictionary from a list using the values in the list as keys in the dictionary and the length of the element as its value'''
	dictionary = dict()
	for item in List:
		dictionary[item] = len(item)
	return dictionary

EnglishDictionary = build_dictionary(wordList)

def invert_dict(d):
	'''takes in a dictionary, and swaps the values and keys '''
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) +1
	return d

print histogram('brontosaurus')

#11.9: has duplicates

def has_duplicates(t):
	d = dict()
	for e in t:
		if e in d:
			return True
		else:
			d[e] = ''
	return False

print has_duplicates([ 'Anthony', 'John'])

#11.10: find rotate pairs
import string

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


def find_rotate_pairs(wordList):
	'''for each word in wordList, we find if when we rotate it, it equals another word. and we return a list of those "pairs" '''
	d = invert_dict(build_dictionary(wordList)) # a dictionary with keys of word lengths, and values of words with that length
	rotate_pairs = []
	for word in wordList:
		for i in range(25):
			rword = rotate_word(word, i+1)
			if rword in d[len(word)]: #check to see if the word is a value in the list at that length -- designed to make sure the fucntion doesn't go through all words
				print word, " ", rword
				rotate_pairs.append([word, rword])
				#wordList.remove(rword)
	return rotate_pairs

def find_rotate_pairs_fast(wordList):
	'''same as above, but uses a dictionary instead of that inverted dict thing. this is much faster. '''
	d = build_dictionary(wordList)
	rotate_pairs = []
	for word in wordList:
		for i in range(25):
			rword = rotate_word(word, i+1)
			if rword in d:
				rotate_pairs.append([word, rword])
	return rotate_pairs

print find_rotate_pairs_fast(wordList)


