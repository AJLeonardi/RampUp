# Flower excercise (5.5 and 5.6) from Week 1
# Name: Anthony Leonardi


from TurtleWorld import *
import math
world = TurtleWorld()			
bob = Turtle()
bob.delay = 0.001

# def draw(t, length, n):
# 	if n == 0:
# 		return
#	angle = 50
#	fd(t, length*n)
#	lt(t, angle)
#	draw(t, length, n-1)
#	rt(t, 2*angle)
#	draw(t, length, n-1)
#	lt(t, angle)

#draw(bob, 3, 20)


def is_triangle(x,y,z):
	if (((x+y)>z) and ((y+z)>x) and ((z+x)>y)):
		return True
	else:
		return False

def draw_Koch(t, length):
	if(length>3):
		tl = length/3.0
		draw_Koch(t, tl)
		lt(t, 60)
		draw_Koch(t, tl)
		rt(t, 120)
		draw_Koch(t, tl)
		lt(t, 60)
		draw_Koch(t, tl)
	else:
		fd(t,length)
		return

def draw_Koch_Triangle_Gen(t, a, b, c):
	"""takes a turtle and three lengths to draw a triangle using koch curves"""
	isTriangle = is_triangle(a,b,c)
	if(isTriangle):
		angleC = 180 - math.degrees(math.acos( (c**2 - a**2 - b**2) / float(-2*a*b) ) )
		angleA = 180 - math.degrees(math.acos( (a**2 - c**2 - b**2) / float(-2*c*b) ) )
		draw_Koch(t, a)
		rt(t, angleC)
		draw_Koch(t, b)
		rt(t, angleA)
		draw_Koch(t, c)
		rt(t, 180-180-angleC-angleA)
		return
	else:
		print("These lengths can not create a triangle")
		return

def snowflake(t, l):
	draw_Koch_Triangle_Gen(t, l, l, l)
	return

def snowflake_HC(t,l):
	for i in range(3):
		draw_Koch(t, l)
		rt(t, 120)

#draw_Koch_Triangle(bob, 200, 200, 390)

bob.x = -150
bob.y = 90
bob.redraw()

snowflake(bob, 100)

#draw_Koch(bob, 500)

wait_for_user()	