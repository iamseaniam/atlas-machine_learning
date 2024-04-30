def matrix_shape(matrix):
    def ishape(matrix):
        shapes = [ishape(x) if isinstance(x, list) else [] for x in matrix]
        shape = shapes[0]
        shape.append(len(matrix))
        return shape
    return list(reversed(ishape(matrix)))
