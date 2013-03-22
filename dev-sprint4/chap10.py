#Anthony Leonardi
import time
from bisect import bisect_left
#10.4
def middle(l):
	t = l[:]
	del t[0]
	del t[-1]
	return t

#10.10
def build_list_append():
	fin =open('words.txt')
	t = []
	for line in fin:
		line = line.strip()
		t.append(line)
	return t

def build_list_add():
	fin =open('words.txt')
	t = []
	for line in fin:
		line = line.strip()
		t = t + [line]
	return t

'''
start = time.time()
t = build_list_append()
total_time = time.time() - start

print total_time, 'seconds'

start = time.time()
t = build_list_add()
total_time = time.time() - start

print total_time, 'seconds'
'''


'''
add took 77.4620380402 seconds
append took 0.0474820137024 seconds

append is much faster becasue it affects the list directly, instead of creating a new list and re-assigning it for each word.

'''

#10.7: anagrams

def is_anagram(s1, s2):
	t1 = list(s1)
	t2 = list(s2)
	t1.sort()
	t2.sort()
	return t1 == t2

#10.13: interlocking words
word_dictionary = build_list_append()

def in_bisect(word_list, word):
	i = bisect_left(word_list, word)
	if i != len(word_list) and word_list[i] == word:
		return True
	else:
		return False

def is_a_word(s):
	return in_bisect(word_dictionary, s)

def is_a_word_in_list(word_list, word):
	return in_bisect(word_list, word)

def find_interlocks():
	t = []
	for word in word_dictionary:
		word1 = word[::2]
		word2 = word[1::2]
		if is_a_word(word1) and is_a_word(word2):
			t.append([word, word1, word2])
	return t

def is_interlocked(word, n):
	for i in range(n):
		temp_word = word[i::n]
		if is_a_word(temp_word) == False:
			return False
	return True

def is_interlocked_general(word_list, word, n):
	for i in range(n):
		temp_word = word[i::n]
		if is_a_word_in_list(word_list, temp_word) == False:
			return False
	return True

def find_interlocks_general(word_list, n):
	t = []
	for word in word_list:
		if is_interlocked_general(word_list, word, n):
			t1 = []
			t1.append(word)
			for i in range(n):
				t1.append(word[i::n])
			t.append(t1)
	return t

print find_interlocks_general(word_dictionary, 2)

