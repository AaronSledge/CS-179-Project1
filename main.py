#handles the input and output to the CLI and file
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

class Location:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

def FileRead(filename):
    file = open(filename)

    array = []
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
            array.append(node)
        
    file.close()
    return array

filename = input("Enter the name of file: ")
array = FileRead(filename)

length = len(array)
# for i in range(length):
#     if i == 0:
#         print(f'Length of array: {length}')
#     node = array[i]
#     print(f'Node {node.number}, ({node.x}, {node.y})')

# calculate distance matrix here, but how do we do make this matrix?
dist_mat = DistanceMatrix.dist_matrix(array)
print(dist_mat)

# pass dist matrix as a parameter to the RandomNN function?
#solution = randomNN(dist_mat, starting_alg=ClassicNN, second_alg=ModifiedNN, calculate_dist=Euclidean, optimizer=EarlyAbandoning)