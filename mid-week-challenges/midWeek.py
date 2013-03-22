#Name: Anthony Leonardi

#2/28/2013
import math

def get_area(shapeType, base = None, height = None, radius = None):
	"""takes in a shapeType (circle, rectangle, or triangle), and returns the area of that shape -- given the correct params are passed"""
	if((shapeType == 'rectangle') and base != None and height !=None):
		area = base * height
		print "the area of your rectangle is:"
		print area
	elif((shapeType == 'triangle') and base!= None and height !=None):
		area =  .5*base*height
		print "the area of your triangle is:"
		print area
	elif((shapeType == 'circle') and radius!=None):
		area = math.pi*(radius**2)
		print "the area of your circle is:"
		print area
	else:
		print "your shape, " + shapeType + ", requires different parameters."


get_area('rectangle', base = 5, height = 6)
get_area('rectangle', base = 4, height = 5)
get_area('triangle', base = 4, height = 5)
get_area('triangle', base = 6, height = 3)
get_area('circle', radius = 5)
get_area('circle')
get_area('rectangle', radius = 6)
get_area('circle', base= 5, height = 5)