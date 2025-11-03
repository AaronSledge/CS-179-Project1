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
from ClassicNN import ClassicNN
from ModifiedNN import ModifiedNN
import EarlyAbandoning
from randomS import randomSearch
import threading
import time
import os

# Object called location to store the coordinates of a location read in from the file
class Location:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

# This function reads in the input file which has coordinates for each location
def FileRead(filename):
    # Opens the file
    file = open(filename)
    # Create a list to store the location objects in
    listOfPoints = []
    # Keeps track of what location we are at 
    number = 0

    # This while loop runs while the file is not empty 
    while True:
        # This reads in a line from the file, it ends when it sees a newline
        line = file.readline()
        # If the line read is not an empty string we can proceed and try to create object called location
        if (line != ""):
            # Splits the line so we can get the x and y coordinates separately
            splitLine = line.split()
            # Checks if the split line has only one x and one y coordinate
            if (len(splitLine) == 2):
                # We try to type convert the input, if it can not be converted then it is invalid
                try:
                    # We create the object called node which is a location object
                    x = float(splitLine[0])
                    y = float(splitLine[1])
                    number = number + 1
                    node = Location(number, x, y)
                    # Add the node into our list of points which stores our object location
                    listOfPoints.append(node)
                except:
                    # If the exception triggers the file is in the wrong format
                    print("File in wrong format")
                    exit()
            # If the splitline has more than just one x and one y then the file is in the incorrect format
            else:
                print("File in wrong format")
                exit()
        # Here we break the loop if we reach an empty string
        else: 
            break

    # Once we are done with the file we need to close it    
    file.close()

    # If list of points remains empty, then we know the input file is empty
    if (listOfPoints == []):
        print("File is empty")
        exit()

    # The drone is allowed a maximum of 256 points that it can reach
    if (len(listOfPoints) > 256):
        print("N is greater than 256")
        exit()
    
    # This function returns the list of points array which contains object location
    return listOfPoints

# Random Search Functions

isDone = False
collectionOfDistance = []
finalPath = []
prev = 0

# The print sum function prints the total distance of a path found using random search until the user hits the enter key
def printSum(sumOfDistance, listOfPoints):
    # We initialize gloabl variables so that the variables are mutable within thread and function
    global collectionOfDistance, finalPath, prev 
    # This gets the start time when it runs
    start_time = time.time()

    # This loop 
    while not isDone:
        time.sleep(0.25) #code pauses a quarter of a second. Can change if needed to
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

# This writes the solution for which nodes to visit e.g. "1 2 10 3 1"
def finalPathToFile(filename, finalPath, collectionOfDistance):
    with open(f"{filename}_SOLUTION_{int(round(collectionOfDistance[-1][0]))}.txt", "w") as outFile:
        for i in finalPath:
            outFile.write(f"{i.number} \n")
    return outFile.name

filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)

# Changing the last nodes number to match the start node since the start and stop position are the same
listOfPoints[-1].number = 1

#print(f"There are {(len(listOfPoints))} nodes, computing route...")
#print("\t Shortest Route Discovered So Far")

#source threading https://www.youtube.com/watch?v=A_Z1lgZLSNc
#threading.Thread(target=printSum, args=(math.inf, listOfPoints)).start() #used threading so function can continously run without having to wait for input

#input()
#isDone = True

#if (collectionOfDistance[-1][0] > 6000):
   #print(f"Warning: Solution is {collectionOfDistance[-1][0]}, greater than the 6000-meter constraint.")
    #filename = os.path.splitext(os.path.basename(filename))[0]

#outFile = finalPathToFile(filename, finalPath, collectionOfDistance)

#writeToDistanceFile(collectionOfDistance)
#writeToDistanceFile(collectionOfDistance)

#nameFileOne = "distanceFileRandomS.txt"
#nameFileOne = "distanceFileRandomS.txt"

#analyzeDistance(nameFileOne)
#analyzeDistance(nameFileOne)





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





# Random NN Functions

NNisDone = False
collectionOfDistanceNN = []
finalPathNN = []
first_iter = True
prev = 0

def printSumNN(sumOfDistance, listOfPoints):
    global collectionOfDistanceNN, finalPathNN, prev, first_iter #so variables are mutable within thread and function
    start_time = time.time()
    if first_iter == True:
        time.sleep(0.25)
        sumOfDistance, path, _, _ = ClassicNN(listOfPoints, dist_mat)
        if prev != sumOfDistance:
            time_So_Far = time.time() - start_time
            collectionOfDistanceNN.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
            finalPathNN = path #for jason when making route graph
            print(f"          {sumOfDistance}")
        prev = sumOfDistance
        first_iter = False
    while not NNisDone:
        time.sleep(0.25) #code pauses a quarter of a second. Can change if needed to
        sumOfDistance, path, _, _ = ModifiedNN(listOfPoints, dist_mat, finalPathNN, dist_to_beat=sumOfDistance)

        if prev != sumOfDistance:
            time_So_Far = time.time() - start_time
            collectionOfDistanceNN.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
            finalPathNN = path #for jason when making route graph
            print(f"          {sumOfDistance}")
        prev = sumOfDistance  
       
    saveRouteImg(listOfPoints, finalPathNN, prev, filename)


def writeToDistanceFileNN(collectionOfDistanceNN):
    with open("distanceFileRandomNN.txt", "a") as file:
        file.write(str(collectionOfDistanceNN) + "\n")
print("--List of Points--")
for i in range(0, len(listOfPoints)):
    print(listOfPoints[i].number)


print(f"There are {(len(listOfPoints))} nodes, computing route..")
print("     Shortest Route Discovered So Far")

threading.Thread(target=printSumNN, args=(math.inf, listOfPoints)).start() # used threading so function can continously run without having to wait for input

input()
NNisDone = True

if (collectionOfDistanceNN[-1][0] > 6000):
        print(f"Warning: Solution is {collectionOfDistanceNN[-1][0]}, greater than the 6000-meter constraint.")

filename = os.path.splitext(os.path.basename(filename))[0]
# this writes the solution for which nodes to visit e.g. "1 2 10 3 1"

outFile = finalPathToFile(filename, finalPathNN, collectionOfDistanceNN)

print(f"Route written to disk as {outFile}")

writeToDistanceFileNN(collectionOfDistanceNN)

#nameFileOne = "distanceFileRandomNN.txt"

#analyzeDistance(nameFileOne)