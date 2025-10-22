#handles the input and output to the CLI and file. Keep track of time
#Kenny/michael
#inputs: file with N locations, Enter key interpution(char or askii value)
#Outputs: Sum of distance(int), paths of points(array), if solution is greater than 6000...(string), any error messaging(string)
import math
from randomS import randomSearch
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

filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)

sumOfDistance = math.inf

print(f"There are {(len(listOfPoints))}, computing route...")
print("\t Shortest Route Discovered So Far")

while True:
    stopPoint = input()
    if stopPoint == "":
        break
    sumOfDistance, path = randomSearch(listOfPoints, sumOfDistance)
    print(sumOfDistance)










