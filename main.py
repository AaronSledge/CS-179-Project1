#handles the input and output to the CLI and file. Keep track of time
#Kenny/michael
#inputs: file with N locations, Enter key interpution(char or askii value)
#Outputs: Sum of distance(int), paths of points(array), if solution is greater than 6000...(string), any error messaging(string)
import math
import numpy as np
import DistanceMatrix
from euclideanDistance import Euclidean
from route import saveRouteImg
from distancePlot import analyzeDistance
import randomNN
from ClassicNN import ClassicNN
from ModifiedNN import ModifiedNN
import EarlyAbandoning
from randomS import randomSearch
import threading
import time
import os

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
prev = 0
def printSum(sumOfDistance, listOfPoints):
    global collectionOfDistance, finalPath, prev #so variables are mutable within thread and function
    start_time = time.time()
    while not isDone:
        time.sleep(0.25) #code pauses half a second. Can change if needed to
        sumOfDistance, path = randomSearch(listOfPoints, sumOfDistance)
        if prev != sumOfDistance:
            time_So_Far = time.time() - start_time 
            collectionOfDistance.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
            finalPath = path #for jason when making route graph
            print(f"\t \t {sumOfDistance}")
        prev = sumOfDistance  
        
    saveRouteImg(listOfPoints, finalPath, prev, filename)
        

def writeToDistanceFile(collectionOfDistance):
    with open("distanceFileRandomS.txt", "a") as file:
        file.write(str(collectionOfDistance) + "\n")

filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)
listOfPoints[-1].number = 1;

print(f"There are {(len(listOfPoints))} nodes, computing route...")
print("\t Shortest Route Discovered So Far")

#source threading https://www.youtube.com/watch?v=A_Z1lgZLSNc
threading.Thread(target=printSum, args=(math.inf, listOfPoints)).start() #used threading so function can continously run without having to wait for input

input()
isDone = True

filename = os.path.splitext(os.path.basename(filename))[0]
# this writes the solution for which nodes to visit e.g. "1 2 10 3 1"
with open(f"{filename}_SOLUTION_{int(round(collectionOfDistance[-1][0]))}", "w") as outFile:
    for i in finalPath:
        outFile.write(f"{i.number} \n")

writeToDistanceFile(collectionOfDistance)

nameFileOne = "distanceFileRandomS.txt"

analyzeDistance(nameFileOne)





length = len(listOfPoints)
# for i in range(length):
#     if i == 0:
#         print(f'Length of array: {length}')
#     node = array[i]
#     print(f'Node {node.number}, ({node.x}, {node.y})')



# calculate distance matrix here, but how do we do make this matrix?
dist_mat = DistanceMatrix.dist_matrix(listOfPoints)
#print(dist_mat)



# pass dist matrix as a parameter to the RandomNN function?
# solution_path, solution_dist = RandomNN(listOfPoints, dist_mat, starting_alg=ClassicNN, second_alg=ModifiedNN)

# print("     ClassicNN Stuff:")
# path, curr_dist, visited, not_visited = ClassicNN(listOfPoints, dist_mat)
# print(f"Current Distance (bsf): {curr_dist}")
# print("     DONE")
# # print(f"Path: {path}")
# # print(f"Distance: {curr_dist}")
# # print(f"Indices Visted Nodes: {visited}")
# # print(f"Indices Not Visited: {not_visited}")

# print("     ModifiedNN Stuff:")
# path, curr_dist, visited, not_visited = ModifiedNN(listOfPoints, dist_mat, path, curr_dist)

# print(f"Path: {path}")
# print(f"Distance: {curr_dist}")
# print(f"Indices Visted Nodes: {visited}")
# print(f"Indices Not Visited: {not_visited}")





# stuff for randomNN
NNisDone = False
collectionOfDistanceNN = []
finalPathNN = []
first_iter = True
prev = 0
def printSumNN(sumOfDistance, listOfPoints):
    global collectionOfDistanceNN, finalPathNN, prev, first_iter #so variables are mutable within thread and function
    start_time = time.time()
    i = 1
    if first_iter == True:
        time.sleep(0.25)
        sumOfDistance, path, _, _ = ClassicNN(listOfPoints, dist_mat)
        if prev != sumOfDistance:
            time_So_Far = time.time() - start_time 
            collectionOfDistanceNN.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
            finalPathNN = path #for jason when making route graph
            print(f"\t \t {sumOfDistance}")
        prev = sumOfDistance
        first_iter = False
    while not NNisDone:
        time.sleep(0.25) #code pauses half a second. Can change if needed to
        sumOfDistance, path, _, _ = ModifiedNN(listOfPoints, dist_mat, dist_to_beat=sumOfDistance)
        if prev != sumOfDistance:
            time_So_Far = time.time() - start_time 
            collectionOfDistanceNN.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
            finalPathNN = path #for jason when making route graph
            print(f"\t \t {sumOfDistance}")
        prev = sumOfDistance  
        
    saveRouteImg(listOfPoints, finalPathNN, prev, filename)

def writeToDistanceFileNN(collectionOfDistanceNN):
    with open("distanceFileRandomNN.txt", "a") as file:
        file.write(str(collectionOfDistanceNN) + "\n")
print("--List of Points--")
for i in range(0, len(listOfPoints)):
    print(listOfPoints[i].number)

print("--Solution from RandomNN Algorithm--")
print(f"There are {(len(listOfPoints))} nodes, computing route...")
print("\t Shortest Route Discovered So Far")

threading.Thread(target=printSumNN, args=(math.inf, listOfPoints)).start() #used threading so function can continously run without having to wait for input

input()
isDone = True

filename = os.path.splitext(os.path.basename(filename))[0]
# this writes the solution for which nodes to visit e.g. "1 2 10 3 1"
with open(f"{filename}_SOLUTION_{int(round(collectionOfDistanceNN[-1][0]))}", "w") as outFile:
    for i in finalPathNN:
        outFile.write(f"{i} \n")

writeToDistanceFileNN(collectionOfDistanceNN)