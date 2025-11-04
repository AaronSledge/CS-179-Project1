from euclideanDistance import Euclidean
import numpy as np

class Location:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

def ClassicNN(pts_array, dist_matrix):
    # source from YouTube: https://www.youtube.com/watch?v=RQpFffcI-ZI
    # need the pts_array to know what points pertain to what node number
    num_interm_nodes = len(pts_array) - 1 # for the 128Circle201.txt file, this should be 127, so now the last node(the launching pad is no longer included in the array)
    
    # isolate the intermediate nodes so that we don't visit the launching pad again before visiting all other nodes first
    dist_matrix_interm = np.delete(dist_matrix, num_interm_nodes, 1)
    dist_matrix_interm = np.delete(dist_matrix_interm, num_interm_nodes, 0)

    #sumOfDistance = 7000
    curr_dist = 0
    path = []

    idx_visited = set()

    # add all indexes to the not visited set
    idx_not_visited = set()
    for i in range(0, num_interm_nodes):
        idx_not_visited.add(i)
    
    curr_node = pts_array[0]

    while (len(idx_visited) != num_interm_nodes-1) and ((curr_node.number - 1) not in idx_visited) and (bool(idx_not_visited) == True):
        # add current node to visited set and path, and remove the current node index from the not visited set (essentially swap the indices)
        curr_node_idx = curr_node.number - 1
        idx_visited.add(curr_node_idx)
        idx_not_visited.remove(curr_node_idx)
        path.append(curr_node)
        
        closest_node_idx = -1
        closest_node_dist = 7000
        for idx, i in enumerate(idx_not_visited):
            # if the ith index is greater than the current index then we can access using the current index as the row
            if (i > curr_node_idx):
                if (dist_matrix_interm[curr_node_idx][i] < closest_node_dist):
                    closest_node_dist = dist_matrix_interm[curr_node_idx][i]
                    closest_node_idx = i
            # if the ith index is less than the current index, then we can access using the current index as the column instead
            elif (i < curr_node_idx):
                if (dist_matrix_interm[i][curr_node_idx] < closest_node_dist):
                    closest_node_dist = dist_matrix_interm[i][curr_node_idx]
                    closest_node_idx = i
            else:
                # else statement should never be reached, change to formal error-handling later on
                print("Somehow we got to this part")
        closest_node = pts_array[closest_node_idx]

        curr_dist += closest_node_dist
        curr_node = closest_node

    # now visit last node (return to landing pad)
    last_curr_node_idx = curr_node.number - 1
    idx_visited.add(last_curr_node_idx)
    idx_not_visited.remove(last_curr_node_idx)
    path.append(curr_node)

    # accesses all neighbor nodes for the last node we have visited
    neighbor_nodes = dist_matrix[last_curr_node_idx]

    # we will return the start location by access the last index of this array of neighbor nodes
    # the last node and first node are both the same location; which is the launch pad

    # this gets the actual distance to return from the last visited node to the launch pad
    return_dist = neighbor_nodes[num_interm_nodes]

    # this gets the actual node (the launch pad)
    return_node = pts_array[num_interm_nodes]

    # this adds the return distance to the total distance for the current path
    curr_dist += return_dist

    # adds the last nodes index to the visited set
    return_node_idx = return_node.number - 1
    idx_visited.add(return_node_idx)

    # appends the last node to the path so that we have a path in the form: 1 5 4 1
    path.append(return_node)

    # sorts the two visited sets which helped during the development process to make sure that
    # all nodes were visited and no nodes were left unvisited
    sorted_idx_visited = sorted(idx_visited)
    sorted_idx_not_visited = sorted(idx_not_visited)

    # idx_visted should have all the indices and idx_not_visited should be an empty set at this point
    return int(curr_dist), path, sorted_idx_visited, sorted_idx_not_visited