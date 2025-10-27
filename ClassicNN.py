from euclideanDistance import Euclidean
import numpy as np
import heapq as hq

class Location:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

def ClassicNN(pts_array, dist_matrix, calculate_dist = Euclidean):
    # source from YouTube: https://www.youtube.com/watch?v=RQpFffcI-ZI
    # need the pts_array to know what points pertain to what node number, need the calculate_dist
    # variable so we can change the distance function if we ever want to

    # so how do we do this? Start at Node 1 (launch pad and mark it as visited so that we don't visit it
    # again before visiting all other nodes)
    num_interm_nodes = len(pts_array) - 1 # for the 128Circle201.txt file, this should be 127, so now the last node(the launching pad is no longer included in the array)
    
    # isolate the intermediate nodes so that we don't visit the launching pad again before visiting all other nodes first
    dist_matrix_interm = np.delete(dist_matrix, num_interm_nodes, 1)
    dist_matrix_interm = np.delete(dist_matrix_interm, num_interm_nodes, 0)

    print(f'Number of Rows: {len(dist_matrix_interm)}')
    print(f'Number of Columns: {len(dist_matrix_interm[0])}')

    #sumOfDistance = 7000
    curr_dist = 0
    path = []

    visited = set()
    
    curr_node = pts_array[0]
    exceptions = set()

    while (len(visited) != num_interm_nodes) and (curr_node.number not in visited):
        # how do we make sure that we are getting a distance from the upper right triangle?
        # we could look at the indexes, of the neigboring nodes, that are greater than the current nodes index
        visited.add(curr_node.number)
        path.append(curr_node.number)

        zero_exceptions = list(range(0, curr_node.number))
        zero_exceptions = set(zero_exceptions)

        exception = curr_node.number - 1
        print(exception)

        neighbor_nodes = dist_matrix_interm[exception]
        
        print(f"For loop stuff")
        closest_node_idx = -1
        closest_node_dist = 7000
        for i in range(exception, len(neighbor_nodes) - 1):
            if (i != exception) and (i+1 not in visited) and (neighbor_nodes[i] < closest_node_dist):
                closest_node_dist = neighbor_nodes[i]
        print(closest_node_idx)
        print(closest_node_dist)
        closest_node = pts_array[closest_node_idx]

        curr_dist += closest_node_dist
        curr_node = closest_node
        # print(f'Closest node index (should not be 0, should be 16): {closest_node_idx}')
        # print(f'Closest node distance (should not be 0, should be 13.2569): {closest_node_dist}')
        # print(f'Closest Node info: Number = {closest_node.number}, ({closest_node.x}, {closest_node.y})')
        # break
        print(curr_dist)
        
        # delete the first column so that the while loop is not evaluated as false
        # if (dist_matrix_interm[0][0] == 0.0):
        #     dist_matrix_interm = np.delete(dist_matrix_interm, 0, 0)
        #     dist_matrix_interm = np.delete(dist_matrix_interm, 0, 1)
    # now visit last node (return to landing pad)
    neighbor_nodes = dist_matrix[curr_node.number - 1]
    return_dist = neighbor_nodes[num_interm_nodes]
    return_node = pts_array[num_interm_nodes]
    curr_dist += return_dist
    visited.add(return_node.number)
    path.append(return_node.number)

    return path, curr_dist, visited