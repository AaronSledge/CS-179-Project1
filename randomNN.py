#Choose points that follows nearest neighbor rules while also implementing probability(10% chance of going to a randomly selected point)
#kenny/micahel
#inputs: Memo table(euclidean distance), List of points(array), Sum of distance(float)
#Returns: Sum of distance, path shown

import ClassicNN
import ModifiedNN
import EarlyAbandoning
from euclideanDistance import Euclidean

def randomNN(dist_matrix, starting_alg, second_alg, calculate_dist, optimizer=0):
    # somehow check that locations was created correctly, locations is an array that assigns a number to each
    # location and sets the x and y coordinates as attributes of the object
    # assuming this was done correctly do the following:

    # ClassicNN performs the first iteration to create the BSF solution as a baseline, i.e. the strawman.
    # this is the normal NearestNeighbors alg.
    bsf = starting_alg(dist_matrix)
    
    return 2