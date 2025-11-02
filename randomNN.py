#Choose points that follows nearest neighbor rules while also implementing probability(10% chance of going to a randomly selected point)
#kenny/micahel
#inputs: Memo table(euclidean distance), List of points(array), Sum of distance(float)
#Returns: Sum of distance, path shown

import ClassicNN
import ModifiedNN
import EarlyAbandoning
from euclideanDistance import Euclidean

def RandomNN(pts_array, dist_matrix, starting_alg, second_alg, optimizer=0):
    # somehow check that locations was created correctly, locations is an array that assigns a number to each
    # location and sets the x and y coordinates as attributes of the object
    # assuming this was done correctly do the following:

    # ClassicNN performs the first iteration to create the BSF solution as a baseline, i.e. the strawman.
    # this is the normal NearestNeighbors alg.
    bsf_path, bsf_dist, _, _ = starting_alg(pts_array, dist_matrix)

    # need to do threading here. Want second_alg to keep running until user hits the ENTER key
    isDone = False
    collectionOfDistance = []
    finalPath = []

    def printSum(sumOfDistance, listOfPoints):
        global collectionOfDistance, finalPath #so variables are mutable within thread and function
        start_time = time.time()
        while not isDone:
            time.sleep(0.5) #code pauses half a second. Can change if needed to
            sumOfDistance, path = randomSearch(listOfPoints, sumOfDistance)
            time_So_Far = time.time() - start_time 
            collectionOfDistance.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
            finalPath = path
            print(f"\t \t {sumOfDistance}")
    bsf_path2, bsf_dist2, _, _ = second_alg(pts_array, dist_matrix, bsf_path, bsf_dist)
    if (bsf_dist2 < bsf_dist):
        bsf_dist = bsf_dist2
        bsf_path = bsf_path2

    if (bsf_dist > 6000):
        print(f"Warning: Solution is {bsf_dist}, greater than the 6000-meter constraint.")

    return bsf_path, bsf_dist