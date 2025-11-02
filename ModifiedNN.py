from euclideanDistance import Euclidean
import numpy as np
import random

def ModifiedNN(pts_array, dist_matrix, path_to_beat, dist_to_beat):
    num_interm_nodes = len(pts_array) - 1 # for the 128Circle201.txt file, this should be 127, so now the last node(the launching pad is no longer included in the array)
    
    # isolate the intermediate nodes so that we don't visit the launching pad again before visiting all other nodes first
    dist_matrix_interm = np.delete(dist_matrix, num_interm_nodes, 1)
    dist_matrix_interm = np.delete(dist_matrix_interm, num_interm_nodes, 0)

    curr_dist = 0
    path = []

    idx_visited = set()

    # add all indexes to the not visited set
    idx_not_visited = set()
    for i in range(0, num_interm_nodes):
        idx_not_visited.add(i)
    # print(f"Not visited set:")
    # print(idx_not_visited)
    
    # at this point curr_node is node 1 with coordinates = (82.0, 50.0)
    curr_node = pts_array[0]

    while (len(idx_visited) != num_interm_nodes - 1) and ((curr_node.number - 1) not in idx_visited) and (bool(idx_not_visited) == True):
        # add current node to visited set and path, and remove the current node index from the not visited set (essentially swap the indices)
        curr_node_idx = curr_node.number - 1
        idx_visited.add(curr_node_idx)
        idx_not_visited.remove(curr_node_idx)
        path.append(curr_node)
        
        closest_node_idx = -1
        closest_node_dist = 7000
        # how do we get the closest node and 2nd closest node simultaneously?
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
        
        closest_node_idx2 = -1
        closest_node_dist2 = 7000
        for idx, j in enumerate(idx_not_visited):
            if (j != closest_node_idx):
                if (j > curr_node_idx):
                    if (dist_matrix_interm[curr_node_idx][j] < closest_node_dist2):
                        closest_node_dist2 = dist_matrix_interm[curr_node_idx][j]
                        closest_node_idx2 = j
                # if the ith index is less than the current index, then we can access using the current index as the column instead
                elif (j < curr_node_idx):
                    if (dist_matrix_interm[j][curr_node_idx] < closest_node_dist2):
                        closest_node_dist2 = dist_matrix_interm[j][curr_node_idx]
                        closest_node_idx2 = j
                else:
                    # else statement should never be reached, change to formal error-handling later on
                    print("Somehow we got to this part2")
        # if the two nodes are equidistant from the current node, choose the node based on number
        # this helps for the 128Circle201.txt file since all the nodes are equidistant from each other
        closest_node = -1
        if (closest_node_dist2 == closest_node_dist):
            if (closest_node_idx < closest_node_idx2):
                closest_node = pts_array[closest_node_idx]
                curr_dist += closest_node_dist
            else:
                closest_node = pts_array[closest_node_idx2]
                curr_dist += closest_node_dist2
        else:
            # now the randomness to choose between the two closest nodes
            # how do we choose a node? random number generator where numbers 0-8 correspond to closest node
            # and number 9 corresponds to 2nd closest node
            rand_num = random.randint(0, 9)
            # print(f"Random Number: {rand_num}")
            if (rand_num == 9):
                closest_node = pts_array[closest_node_idx2]
                curr_dist += closest_node_dist2
            else:
                closest_node = pts_array[closest_node_idx]
                curr_dist += closest_node_dist
        curr_node = closest_node
        #if (len(idx_visited) == num_interm_nodes-1): # prints current nodes index on the last iteration of this while loop
            #print(f"Last curr_node index: {curr_node.number - 1}")
        # print(f"Closest Node distance: {closest_node_dist}")
        # print(f"Closest Node index: {closest_node_idx}")
        # print(f"2nd Closest Node distance: {closest_node_dist2}")
        # print(f"2nd Closest Node index: {closest_node_idx2}")
    # now visit last node (return to landing pad)
    last_curr_node_idx = curr_node.number - 1
    idx_visited.add(last_curr_node_idx)
    # print(f"Not visited set after main part of algorithm:")
    # print(idx_not_visited)

    # Need to check if the last curr node index is in the index not visited set before we remove it so that indexing
    # is not messed up by trying to remove something that does not exist in the set
    if (last_curr_node_idx in idx_not_visited):
        idx_not_visited.remove(last_curr_node_idx)
        
    path.append(curr_node)

    neighbor_nodes = dist_matrix[last_curr_node_idx]
    return_dist = neighbor_nodes[num_interm_nodes]
    return_node = pts_array[num_interm_nodes]
    curr_dist += return_dist
    return_node_idx = return_node.number - 1
    idx_visited.add(return_node_idx)
    path.append(return_node)

    sorted_idx_visited = sorted(idx_visited)
    sorted_idx_not_visited = sorted(idx_not_visited)

    # idx_visted should have all the indices and idx_not_visited should be an empty set at this point

    # if dist to beat is greater than current distance then we should return current distance
    if (dist_to_beat > curr_dist):
        return int(curr_dist), path, sorted_idx_visited, sorted_idx_not_visited 
    # if it is not we should return the old path and distance and try again 
    else: 
        return int(dist_to_beat), path_to_beat, sorted_idx_visited, sorted_idx_not_visited 
    