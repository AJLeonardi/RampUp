# Hello excercise from Week 0

# Name: Anthony Leonardi


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
fontHeight = 200
fontWidth = 125
fontSpace = 20


# This is where you put code to move bob

def drawH():
	fd(bob, fontHeight)
	pu(bob)
	bk(bob, fontHeight/2)
	rt(bob)
	pd(bob)
	fd(bob, fontWidth)
	lt(bob)
	pu(bob)
	fd(bob, fontHeight/2)
	pd(bob)
	rt(bob)
	rt(bob)
	fd(bob, fontHeight)
	lt(bob)
	setNewStart()

def drawE():
	fd(bob, fontHeight)
	rt(bob)
	fd(bob, fontWidth)
	pu(bob)
	bk(bob, fontWidth)
	rt(bob)
	fd(bob, fontHeight/2)
	lt(bob)
	pd(bob)
	fd(bob, fontWidth*.75)
	pu(bob)
	bk(bob, fontWidth*.75)
	rt(bob)
	fd(bob, fontHeight/2)
	lt(bob)
	pd(bob)
	fd(bob, fontWidth)
	setNewStart()

def drawL():
	fd(bob, fontHeight)
	pu(bob)
	bk(bob, fontHeight)
	pd(bob)
	rt(bob)
	fd(bob, fontWidth)
	setNewStart()

def drawOh():
	fd(bob, fontHeight)
	rt(bob)
	fd(bob, fontWidth)
	rt(bob)
	fd(bob, fontHeight)
	rt(bob)
	fd(bob, fontWidth)
	pu(bob)
	bk(bob, fontWidth)
	rt(bob)
	rt(bob)
	setNewStart()

def setNewStart():
	pu(bob)
	fd(bob, fontSpace)
	lt(bob)
	pd(bob)

def setFirstStart():
	pu(bob)
	lt(bob)
	lt(bob)
	fd(bob, 50)
	rt(bob)
	bk(bob, 50)
	pd(bob)

def writeHELLO():
	setFirstStart()
	drawH()
	drawE()
	drawL()
	drawL()
	drawOh()


writeHELLO()





wait_for_user()					
