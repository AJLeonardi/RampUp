# Polygon excercise from Week 0

# Name:


from TurtleWorld import * 
import math
world = TurtleWorld()			
bob = Turtle()	
bob.delay = 0.001			



# This is where you put code to move bob

#Original Answer -- but it's confusing as hell and not really correct...
#drawPolgonGen n can be a float since I pass the circumferance of the 
#circle and theta is used to figure out the perentage of the ploygon to draw.

# I also think this is technically wrong because in the polygonGen I floor the number of segments -- 
# so the circumference will be slightly off

#def drawPolygonGen(t,l,theta,n):
#	deg = 360.0/n
#	rng = (theta/360.0)*n
#	for i in range(int(rng)):
#		fd(t,l)
#		lt(t,deg)

#def drawPolygon(t, l, n):
#	drawPolygonGen(t,l,360, n)

#def circle(t,r):
#	arc(t, r, 360)

#def arc(t, r, theta):
#	c = 2*math.pi*r
#	drawPolygonGen(t, 1, theta, c)

#------------------------------------------------------------------------------------------------------


def drawPolyGen(t, l, deg, n):
#this is clearer because it asks for the degree between segments -- not the percent of the shape in degrees.
	for i in range(n):
		fd(t,l)
		lt(t,deg)

def drawPolygon(t,l,n):
	deg = 360.0/n
	drawPolyGen(t, l, deg, n)

def arc(t,r,theta):
	c = 2*math.pi*r
	arcLength = (theta/360.0)*c
	n = int(arcLength)
	segLength = arcLength/n
	deg = float(theta)/n
	drawPolyGen(t, segLength, deg, n)

def circle(t, r):
	arc(t,r,360)



drawPolygon(bob, 50, 7)
circle(bob, 40)
arc(bob, 100, 100)

wait_for_user()					
