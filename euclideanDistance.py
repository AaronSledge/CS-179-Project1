#Calculate distance
#input: List of points(array)
#Output: distance(float)
#Kenny
import math

def Euclidean(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return distance

