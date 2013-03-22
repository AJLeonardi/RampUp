# Exercises for chapter 3: Problems 3.1, 3.2, 3.3, and 3.4 in Think Python

# Anthony Leonardi

#Exercise 3.1:
#code:
# repeat_lyrics()
# def print_lyrics():
#     print "I'm a lumberjack, and I'm okay."
#     print "I sleep all night and I work all day."
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
#
# what happens:
# Traceback (most recent call last):
#  File "chapter3_exercises.py", line 8, in <module>
#    repeat_lyrics()
# NameError: name 'repeat_lyrics' is not defined
#
#********************************************************************************
#
#Exercise 3.2:
#
#Code:
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# def print_lyrics():
#     print "I'm a lumberjack, and I'm okay."
#     print "I sleep all night and I work all day."
# repeat_lyrics()
#
#what happens (it works!):
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
#
# Looks like you can reference functions before the definition of them, 
# but the execution of the function must happen after they're defined. 
# Don't need to worry about a chicken/egg problem when functions reference eachother.
#
#********************************************************************************
#
#Exercise 3.3:
#Code:
# def right_justify(s):
# 	s_length = len(s)
# 	num_spaces = 70 - s_length
# 	print " " * num_spaces + s
# right_justify("allen")
#result:
#                                                                 allen
#
#********************************************************************************
#
#Exercise 3.4:
#1.)
# def do_twice(f):
# 	f()
#	f()
# def print_spam():
#    print 'spam'
# do_twice(print_spam)
#
# 1.) result: it prints:
# spam
# spam
#
# 2.)
def do_twice(f, s):
	f(s)
	f(s)
#
# 3.)
def print_twice(s):
	print s
	print s
#
# 4.)
do_twice(print_twice, 'spam')
#
# 5.)
def do_four(f, s):
	do_twice(f, s)
	do_twice(f, s)
do_four(print_twice, 'spam')

#Exercise 3.5:
def do_x_times(f,x):
	for i in range(x):
		f()
def do_x_times_p(f,p,x):
	for i in range(x):
		f(p)
def print_plus_line():
	print "+ - - - -",
def print_bar_line():
	print "|        ",
def print_full_bar_line(cols):
	do_x_times(print_bar_line, cols)
	print "|"
def draw_row(cols):
	do_x_times(print_plus_line, cols)
	print "+"
	do_x_times_p(print_full_bar_line, cols, 4)
def draw_grid(r,c):
	do_x_times_p(draw_row, c, r)
	do_x_times(print_plus_line, c)
	print "+"
draw_grid(4,4)
# had some extra time so did 3.5, decided to make my solution a bit more generic 
# to support drawing a grid of any size by passing it the num of rows and colums
# I noticed that I can create this "do_x_times" function, but passing parameters is restrictive. 
# is there a more generic way to do this? or would I have to create a "do_x_times" function for each number of params to pass?
# e.g. I've created two above, one that passes no params to the function, and one that passes one param to a function.