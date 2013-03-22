#Name: Anthony Leonardi


def build_list_append():
	fin =open('words.txt')
	t = []
	for line in fin:
		line = line.strip()
		t.append(line)
	return t

wordList = build_list_append()

def print_anagrams(d):
	lengths = []
	for i in d:
		if len(d[i]) > 1:
			lengths.append((len(d[i]), d[i]))
	lengths.sort(reverse = True)
	for e, i in lengths:
		print i

def print_most_bingos(d):
	lengths = []
	for i in d:
		if len(i) == 8:
			lengths.append((len(d[i]),i, d[i]))
	lengths.sort(reverse = True)
	print lengths[0]


def find_anagrams(wordList):
	d = dict()
	for word in wordList:
		tup2 = tuple(word)
		tup = tuple(sorted(tup2))
		if tup in d:
			d[tup].append(word)
		else:
			d[tup] = [word]
	return d




words = ['anthony', 'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled', 'retainers', 'ternaries', 'generating', 'greatening']
print_anagrams(find_anagrams(words))

print_most_bingos(find_anagrams(wordList))


