#Name: Anthony Leonardi
import random

def build_word_list(file_obj):
	t = []
	for line in file_obj:
		for word in line.split():
			w = word.strip()
			t.append(w)
	return t

def create_Markov(pref_length, file_name):
	d = dict()
	fin = open(file_name)
	word_list = build_word_list(fin)
	for i in range(len(word_list)-pref_length):
		prefix_list = word_list[i:i+pref_length]
		delimiter = ' '
		prefix = delimiter.join(prefix_list)
		if prefix in d:
			d[prefix].append(word_list[i+pref_length])
		else:
			d[prefix] = [word_list[i+pref_length]]
	return d

def create_random_Markov_text(pref_length, num_iter, file_name):
	markov = create_Markov(pref_length, file_name)
	text = ''
	for i in range(num_iter):
		key = random.choice(markov.keys())
		phrase = key + " " + random.choice(markov[key])
		text = text + " " +  phrase
	print text


#print create_Markov(2, 'markov.txt')

create_random_Markov_text(2, 100, 'markov.txt')