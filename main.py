#handles the input and output to the CLI and file. Keep track of time
#Kenny/michael
#inputs: file with N locations, Enter key interpution(char or askii value)
#Outputs: Sum of distance(int), paths of points(array), if solution is greater than 6000...(string), any error messaging(string)
import math
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
        


filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)



print(f"There are {(len(listOfPoints))}, computing route...")
print("\t Shortest Route Discovered So Far")

#source threading https://www.youtube.com/watch?v=A_Z1lgZLSNc
threading.Thread(target=printSum, args=(math.inf, listOfPoints)).start() #used threading so function can continously run without having to wait for input

input()
isDone = True

print()






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
#solution = randomNN(dist_mat, starting_alg=ClassicNN, second_alg=ModifiedNN, calculate_dist=Euclidean, optimizer=EarlyAbandoning)