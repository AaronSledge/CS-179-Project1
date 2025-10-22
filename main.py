#handles the input and output to the CLI and file. Keep track of time
#Kenny/michael
#inputs: file with N locations, Enter key interpution(char or askii value)
#Outputs: Sum of distance(int), paths of points(array), if solution is greater than 6000...(string), any error messaging(string)
import math

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

def Euclidean(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - x1), 2))
    return distance

filename = input("Enter the name of file: ")
listOfPoints = FileRead(filename)
distanceMatrix = []
for i in range(len(listOfPoints)):
    row = []
    for j in range(len(listOfPoints)):
        row.append((Euclidean(listOfPoints[i].x, listOfPoints[i].y, listOfPoints[j].x, listOfPoints[j].x), listOfPoints[i], listOfPoints[j]))
    distanceMatrix.append(row)

print(len(distanceMatrix))


