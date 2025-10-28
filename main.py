#handles the input and output to the CLI and file. Keep track of time
#Kenny/michael
#inputs: file with N locations, Enter key interpution(char or askii value)
#Outputs: Sum of distance(int), paths of points(array), if solution is greater than 6000...(string), any error messaging(string)
import math
import DistanceMatrix
from euclideanDistance import Euclidean
#import randomNN
#import ClassicNN
#import ModifiedNN
#import EarlyAbandoning
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
    i = 1
    while not isDone:
        time.sleep(0.25) #code pauses half a second. Can change if needed to
        sumOfDistance, path = randomSearch(listOfPoints, sumOfDistance)
        time_So_Far = time.time() - start_time 
        collectionOfDistance.append((sumOfDistance, time_So_Far)) #for jason when making distance over time graph
        if i == 1:
            finalPath = path
            print(f"\t \t {sumOfDistance}")
        else:
            if sumOfDistance < collectionOfDistance[-2][0]:
                finalPath = path
                print(f"\t \t {sumOfDistance}")
        i += i 

filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)

print(f"There are {(len(listOfPoints))} nodes, computing route...")
print("\t Shortest Route Discovered So Far")

threading.Thread(target=printSum, args=(math.inf, listOfPoints)).start() #used threading so function can continously run without having to wait for input

input()
isDone = True

with open(f"{filename}_SOLUTION_{collectionOfDistance[-1][0]}", "w") as outFile:
    for i in finalPath:
        outFile.write(f"{i.number} \n")

#print(collectionOfDistance) uncomment this to see array of distance and time(in seconds)assoicated with







#length = len(array)
# for i in range(length):
#     if i == 0:
#         print(f'Length of array: {length}')
#     node = array[i]
#     print(f'Node {node.number}, ({node.x}, {node.y})')



# calculate distance matrix here, but how do we do make this matrix?
#dist_mat = DistanceMatrix.dist_matrix(array)
#print(dist_mat)

# pass dist matrix as a parameter to the RandomNN function?
#solution = randomNN(dist_mat, starting_alg=ClassicNN, second_alg=ModifiedNN, calculate_dist=Euclidean, optimizer=EarlyAbandoning)