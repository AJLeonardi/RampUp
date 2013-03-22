# This is where chapter 15 exercises go.

import copy

class Point(object):
	x = 0.0
	y = 0.0
	point_string = "(" + str(x) + ", " + str(y) + ")"
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_copy(self,dx, dy):
		p_copy = copy.copy(self)
		p_copy.move(dx, dy)
		return p_copy

	def point_string(self):
		return "(" + str(self.x) + ", " + str(self.y) + ")"


class Rectangle(object):
	corner = Point()
	width = 0.0
	height = 0.0

	def rect_string(self):
		return "Point: " + self.corner.point_string() + " Width: " + str(self.width) + " Height: " + str(self.height)

	def move(self, dx, dy):
		self.corner.move(dx, dy)

	def move_copy(self, dx, dy):
		r_copy = copy.deepcopy(self)
		r_copy.corner.move(dx, dy)
		return r_copy


a = Point()
a.x = 1
a.y = 2

print a.point_string()


r1 = Rectangle()
r1.corner = a
r1.width = 4
r1.height = 5

print "r1 = " + r1.rect_string()

r2 = r1.move_copy(2, 2)
print "just moved r1 as r2"

print "r1 = " + r1.rect_string()
print "r2 = " + r2.rect_string()