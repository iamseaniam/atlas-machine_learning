#!/usr/bin/env python3
def matrix_shape(matrix):
    def ishape(matrix):
        shapes = [ishape(x) if isinstance (x, list) else [] for x in matrix]
        # iterates over each element x in the matrix. if x is a list, it recursivly calls (ishape(x)) to calculate its shape. if not, returns a empty list
        shape = shapes[0]
        # assigns the first shape in shapes list to the var shape.
        shape.append(len(matrix))
        # appends the length of current matrix to the shape list. it does it to complete shape info by adding dimension of matrix 
        return shape
        # returns shape of matrix
    return list(reversed(ishape(matrix)))
    # revereses it to be correct format as in row col and converts it to a list
