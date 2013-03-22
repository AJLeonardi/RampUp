# Enter your answrs for chapter 7 here
# Name: Anthony Leonardi


# Ex. 7.5
import math
def estimate_pi():
	k = 0
	currSum = 0
	SR = 0
	multiplier = ((2*math.sqrt(2))/9801.0)
	while True:
		print k
		term = ((math.factorial(4*k) *(1103 + 26390*k))/float(((math.factorial(k)**4) * 396**(4*k))))
		currSum = currSum + term
		SR =  multiplier * currSum
		if(abs(term) < 1e-15):
			break
		k = k+1
		print 1/SR
	return 1/SR

print estimate_pi()
print math.pi

# How many iterations does it take to converge?
# it takes 4 iterations before the term is less than 1e-15, but it takes only two iterations before the pi estimate converges on pi to 11 places.

#as a note I think the sample solution in the book is wrong. It looks like it's including the multiplier in the sum, rather than summing the terms,
# and applying the multiplier to the current sum alone.