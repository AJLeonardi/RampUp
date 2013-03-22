# This is where chapter 14 exercises go.

import urllib

def print_secret():
	conn = urllib.urlopen('http://thinkpython.com/secret.html')
	for line in conn:
		print line.strip()

#print_secret()

def print_list_of_facts(l):
	for e in l:
		label = e[0]
		val = e[1]
		print label + " " + val

def print_zip_details(zipcode):
	zip_deets = urllib.urlopen('http://www.uszip.com/zip/' + zipcode)
	list_of_facts = []
	for line in zip_deets:
		data = get_data_from_line(line.strip())
		if data != None:
			list_of_facts.append(data)
	print_list_of_facts(list_of_facts)
	zip_deets.close()

def get_data_from_line(line):
	if '<title>' in line:
		new_line = line.replace('<title>', '').replace(' zip code</title>', '')
		tup = ('US City: ', new_line)
		return tup
	elif 'Total population' in line:
		temp = line[66:][:70]
		word_list = temp.split('<')
		new_line = word_list[0]
		tup = ('Population: ', new_line)
		return tup

def ask_for_zip():
	zip_code = raw_input('What zip do you want to look up?\n')
	print_zip_details(zip_code)


#print_zip_details('05141')
ask_for_zip()