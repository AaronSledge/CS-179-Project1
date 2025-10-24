import math
import numpy as np
from euclideanDistance import Euclidean

def dist_matrix(points_array):
    n = len(points_array)
    matrix = [[float(0) for i in range(n)] for j in range(n)]
    matrix = np.array(matrix)
    print(f"Start of Distance Matrix (dim = {n}x{n}):")
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # print(f"Number of rows: {num_rows}")
    # print(f"Number of cols: {num_cols}")
    for i in range(num_rows): # row
        for j in range(num_cols): # col
            if j > i: # will calculate dists for the top right corner
                nodei = points_array[i]
                nodej = points_array[j]
                # print(f"Node i = {nodei.number}, coords: ({nodei.x}, {nodei.y})")
                # print(f"Node j = {nodej.number}, coords: ({nodej.x}, {nodej.y})")
                matrix[i][j] = float(Euclidean(nodei.x, nodei.y, nodej.x, nodej.y))
    print(f'Number of points in file: {n}')
    return matrix