#Calculate distance
#input: List of points(array)
#Output: distance(float)
#Kenny
import math

# This function calculates the euclidean distance using the formula d = sqrt((x2-x1)^2-((y2-y1)
def Euclidean(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return distance

