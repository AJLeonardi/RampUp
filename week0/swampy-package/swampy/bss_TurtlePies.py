from TurtleWorld import *
from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polyline(t, n, length, angle):
	innerL = (length/2.0)/cos(radians((180.0-angle)/2))
   	for i in range(n):
		fd(t, length)
		lt(t, angle)
		lt(t, (180-angle)/2.0)
		fd(t, innerL)
		pu(bob)
		bk(t,innerL)
		pd(bob)
		rt(t, (180-angle)/2.0)

def polyPie(t,n,length):
    angle = 360.0/n
    polyline(t, n, length, angle)

polyPie(bob, 400, 2)

wait_for_user()