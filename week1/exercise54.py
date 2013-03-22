# This is where Exercise 5.4 goes
# Name: Anthony Leonardi

def is_triangle(x,y,z):
	if (((x+y)>z) and ((y+z)>x) and ((z+x)>y)):
		print "Yes"
	else:
		print "No"

def prompt_for_sticks():
	stick1 = int(raw_input("Enter the length of stick one:\n"))
	stick2 = int(raw_input("Enter the length of stick two:\n"))
	stick3 = int(raw_input("Enter the length of stick three:\n"))

	print "Will these lengths create a triangle? "
	is_triangle(stick1, stick2, stick3)
	return

prompt_for_sticks()