#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = [] # the_middle is a maxtrix not slicing opperation
for row in matrix: # moving through thw rows in the maxtrix
    the_middle.append(row[2:4]) # as its moving through it takes the middle rows and uses the .append method to add to the The_middle maxtrix
print("The middle columns of the matrix are: {}".format(the_middle))
