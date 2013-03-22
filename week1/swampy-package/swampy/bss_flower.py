# Flower excercise (4.2) from Week 0

# Name: Anthony Leonardi


from TurtleWorld import *

#using the ThinkPything polygon file so that I can keep bss_polygon as a separate testable file with function calls 
from polygon import *	
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.001




# This is where you put code to move bob

def drawPetal(t, r, angle):
	""" draws an individual petal:t is the turtle, r is the radius of the arc, 
	and angle is the degree of the arc out of 360"""
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180 - angle)

def drawFlower(t, pc, r, angle):
	"""draws a flower with t is a turle, pc is the petal count integer,
	 r is radius of arc float, and angle is degrees of arc float??"""
	for i in range(pc):
		drawPetal(t, r, angle)
		lt(t, 360/pc)

def setUpNextFlower():
	""" moves bob florward 100"""
	pu(bob)
	fd(bob, 100)
	pd(bob)

drawFlower(bob, 7, 60.0, 60.0)
setUpNextFlower()
drawFlower(bob, 10, 40.0, 80.0)
setUpNextFlower()
drawFlower(bob, 20, 140.0, 20.0)
setUpNextFlower()


wait_for_user()					

