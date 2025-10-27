#handles the input and output to the CLI and file. Keep track of time
#Kenny/michael
#inputs: file with N locations, Enter key interpution(char or askii value)
#Outputs: Sum of distance(int), paths of points(array), if solution is greater than 6000...(string), any error messaging(string)
import math
import numpy as np
import DistanceMatrix
from euclideanDistance import Euclidean
import randomNN
import ClassicNN
import ModifiedNN
import EarlyAbandoning
from randomS import randomSearch
import threading
import time

class Location:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

def FileRead(filename):
    file = open(filename)

    listOfPoints = []
    number = 0

    while True:
        line = file.readline()
        if(line == ""):
            break
        else:
            x, y = line.split()
            x = float(x)
            y = float(y)
            number = number + 1
            node = Location(number, x, y)
            listOfPoints.append(node)
        
    file.close()
    return listOfPoints

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


filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)



# print(f"There are {(len(listOfPoints))}, computing route...")
# print("\t Shortest Route Discovered So Far")

# threading.Thread(target=printSum, args=(math.inf, listOfPoints)).start() #used threading so function can continously run without having to wait for input


# input()
# isDone = True

#print(collectionOfDistance) uncomment this to see array of distance and time(in seconds)assoicated with





for i in range(len(listOfPoints)):
    node = listOfPoints[i]
    print(f'{node.number}, ({node.x}, {node.y})')
length = len(listOfPoints)



# calculate distance matrix here, but how do we do make this matrix?
dist_mat = DistanceMatrix.dist_matrix(listOfPoints)
print(dist_mat)

print(f'Dimensions of dist_mat: {len(dist_mat)} x {len(dist_mat[0])}')

# pass dist matrix as a parameter to the RandomNN function?
# solution = randomNN(array, dist_mat, starting_alg=ClassicNN, second_alg=ModifiedNN, calculate_dist=Euclidean, optimizer=EarlyAbandoning)
print()
print()
print()
# solution_path, bsf, visited_nodes = ClassicNN.ClassicNN(listOfPoints, dist_mat)
# print(solution_path)
# print(f'Initial BSF: {bsf}')
# print(f'Visited Nodes: {visited_nodes}')

print(f"Distance from launch pad to first location: {dist_mat[0][1]}")
print(f"Distance from launch pad to 2nd index location (Euclidean function): {Euclidean(listOfPoints[0].x, listOfPoints[0].y, listOfPoints[2].x, listOfPoints[2].y)}")
print(f"Distance from launch pad to 125th index location (Euclidean function): {Euclidean(listOfPoints[0].x, listOfPoints[0].y, listOfPoints[125].x, listOfPoints[125].y)}")