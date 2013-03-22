# Enter your answrs for chapter 6 here
# Name: Anthony Leonardi


# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if(len(word) < 2 ):
		return True
	elif(first(word) == last(word)):
		return is_palindrome(middle(word))
	else:
		return False

print is_palindrome('heh')
print is_palindrome('het')
print is_palindrome('anthony')
print is_palindrome('abcddcba')
print is_palindrome('')
print is_palindrome('a')


# Ex 6.8
def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a%b)

print gcd(1, 3)
print gcd(5,3)
print gcd(10,2)
print gcd(5,15)