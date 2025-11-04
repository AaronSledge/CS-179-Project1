import math
import numpy as np
from euclideanDistance import Euclidean

def dist_matrix(points_array):
    n = len(points_array)
    matrix = [[float(0) for i in range(n)] for j in range(n)]
    matrix = np.array(matrix)
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows): # row
        for j in range(num_cols): # col
            if j > i: # will calculate dists for the top right corner
                nodei = points_array[i]
                nodej = points_array[j]
                matrix[i][j] = float(Euclidean(nodei.x, nodei.y, nodej.x, nodej.y))
    return matrix