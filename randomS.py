#Randomly pick points in array to get distance. Update each call if there is a shorter path
#Inputs: Memo table(euclidean distance), List of points(array), Sum of distance(float)
#Returns: Sum of distance, path shown
#Aaron
import random
from euclideanDistance import Euclidean

def randomSearch(listOfPoints, sumOfDistance):
    middle = listOfPoints[1:len(listOfPoints)-2] #split the array, randomize, then combine at end
    randomList = random.sample(middle, len(middle))

    path = [listOfPoints[0]] + randomList + [listOfPoints[-1]]
    distance = 0
    for i in range(len(path) - 1):
        distance += Euclidean(path[i].x, path[i].y, path[i + 1].x, path[i + 1].y)
        #print(path[i].x, path[i].y, path[i + 1].x, path[i + 1].y)
    
    if(distance < sumOfDistance):
        return (distance, path)
    
    if (sumOfDistance > 6000):
        print(f"Warning: Solution is {sumOfDistance}, greater than the 6000-meter constraint.")
    
    return (sumOfDistance, path)
