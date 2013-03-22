# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# Anthony Leonardi

#Exercise 2.1:
#why does the 02132 evaluate to 1114
#   it looks like python treats integers with a leading zero as a base 8 number
#   it then prints it back as base 10
#   non int values e.g. 012.2 would be read as a base ten float, 
#   and printed back as 12.2 (leading zero is stripped)

#Exercise 2.2:
# in the interpreter:
# >>>5
# 5
# >>>x=5
# >>>x+1
# 6
#
# as a script:
#code:
#   5
#   x = 5
#   x+1
# no return value
#
# same statements in a script but adding print to expressions:
print 5
x=5
print x+1
# result:
# 5
# 6

#Exercise 2.3:
# 1.) width/2 = 8 (int)
# 2.) width/2.0 = 8.5 (float)
# 3.) height/3 = 4.0 (float)
# 4.) 1+2*5 = 11 (int)
# 5.) delimiter * 5 = '.....' (string)

#Exercise 2.4:
# 1.) volume sphere (in interpreter): 
# >>> r = 5
# >>> pi = 3.14159
# >>> (4*pi*r**3)/3
# 523.5983333333332
#
# 2.) book costs
# This works, but seems silly (multiplying and dividing by 100 resolves floating point arithmetic issues)
# >>> cost = 24.95
# >>> cost_of_books = cost *100 * 60 * .6 / 100
# >>> shipping_cost = 3 + 59 * .75
# >>> total_cost = cost_of_books + shipping_cost
# >>> total_cost
# 945.45
# 
# Just the Math:
# >>> (24.95*100*60*.6/100) + (3 + 59 * .75)
# 945.45
#
# 3.) Finish Time:
# >>> start_time_seconds = 6*60*60 + 52*60
# >>> secs_at_easy = (8*60 + 15) * 2                                        #num of seconds per mile * num miles at pace
# >>> secs_at_tempo = (7*60 + 12) * 3                                       #num of seconds per mile * num miles at pace
# >>> finish_time_secs = start_time_seconds + secs_at_easy + secs_at_tempo
# >>> finish_hour = finish_time_secs/60/60                                  #this gets the hours because of floor division -- takes off the remainder
# >>> finish_min = (finish_time_secs - (finish_hour*60*60))/60  
# >>> finish_hour
# 7
# >>> finish_min
# 30
# *** Answer: he gets home at 7:30am for breakfast