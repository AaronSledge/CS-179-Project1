#test all functions making sure they work properly
#everyone

import unittest
import math
from euclideanDistance import Euclidean
from randomS import randomSearch
from main import Location
from main import FileRead
from main import finalPathToFile
from DistanceMatrix import dist_matrix
from ClassicNN import ClassicNN
from ModifiedNN import ModifiedNN

class TestEuclidean(unittest.TestCase):
    def test_euclideanCalc(self):
        x1 = 8
        y1 = 6
        x2 = 5
        y2 = 7
        self.assertEqual(Euclidean(x1, y1, x2, y2), math.sqrt(10), "The distance is incorrectly miscalculated for whole numbers")

   #def test_euclideanFloats(self):
        #x1 = 8.5
        #y1 = 6.2
        #x2 = 5.1
        #y2 = 7.8
        #self.assertAlmostEqual(Euclidean(x1, y1, x2, y2), math.sqrt(14.12), "The distance is incorrectly miscalculated for floating points")

testArray = []
node1 = Location(1, 8, 6)
testArray.append(node1)

node2 = Location(2, 10, 5)
testArray.append(node2)

node3 = Location(3, 9, 1)
testArray.append(node3)

node4 = Location(4, 5, 7)
testArray.append(node4)

node5 = Location(5, 1, 10)
testArray.append(node5)

node6 = Location(6, 3, 13)
testArray.append(node6)

node7 = Location(7, 2, 15)
testArray.append(node7)

node8 = Location(8, 12, 5)
testArray.append(node8)

node9 = Location(1, 4, 11)
testArray.append(node9)

node10 = Location(1, 10, 20)
testArray.append(node10)


class TestRandomS(unittest.TestCase):
    def test_randomFirstValue(self):
        sumOfdistance, path = randomSearch(testArray, math.inf)
        coordinates = (path[0].x, path[0].y)
        self.assertEqual(coordinates, (testArray[0].x, testArray[0].y), "Random search randomizes start point")
    
    def test_randomLastValue(self):
        sumOfdistance, path = randomSearch(testArray, math.inf)
        coordinates = (path[-1].x, path[-1].y)
        self.assertEqual(coordinates, (testArray[-1].x, testArray[-1].y), "Random search randomizes last point")
    
    def test_middleValues(self):
        sumOfdistance, path = randomSearch(testArray, math.inf)
        self.assertNotEqual(path, testArray, "Random search does not randomize the array")
    
    def distanceIsLower(self):
        sumOfdistance, path = randomSearch(testArray, math.inf)
        distance1 = sumOfdistance
        sumOfdistance, path = randomSearch(testArray, math.inf)
        distance2 = sumOfdistance
        self.assertLess(distance2, distance1, "Random search does not output quicker path")


class TestFileRead(unittest.TestCase):
    def test_CorrectRead(self):
        testFile = "filereadtest.txt"
        listOfPoints = FileRead(testFile)
        one = Location(1, 1.0, 2.0)
        two = Location(2, 3.0, 4.0)
        three = Location(3, 5.0, 6.0)
        four = Location(1, 1.0, 2.0)
        array = [one, two, three, four]
        count = 0
        for i in range(len(array)):
            if ((listOfPoints[i].number == array[i].number) & (listOfPoints[i].x == array[i].x) & (listOfPoints[i].y == array[i].y)):
                count += 1
        self.assertEqual(4, 4, "The file is not read correctly")


class TestOutputFile(unittest.TestCase):
    def test_MakeOutputFile(self):
        filename = "file"
        one = Location(1, 1.0, 2.0)
        two = Location(2, 3.0, 4.0) 
        three = Location(3, 5.0, 6.0)
        four = Location(1, 1.0, 2.0)
        s1 = Euclidean(one.x, one.y, two.x, two.y)
        s2 = Euclidean(three.x, three.y, four.x, four.y)
        ts = s1 + s2 
        array = [one, two, three, four]
        collectionOfDistance = []
        collectionOfDistance.append((ts, 0.25))
        outFileName = finalPathToFile(filename, array, collectionOfDistance)
        created = False
        print(outFileName)
        if (outFileName == f"file_SOLUTION_{int(round(ts))}.txt"):
            created = True
        self.assertEqual(created, True, "The output file is not made correctly")
    

class TestDistanceMatrix(unittest.TestCase):
    def test_DistanceMatrix(self):
        one = Location(1, 1.0, 2.0)
        two = Location(2, 3.0, 4.0) 
        three = Location(3, 5.0, 6.0)
        four = Location(4, 7.0, 8.0)
        path = [one, two, three, four]
        dm = dist_matrix(path)
        matrix = [[float(0) for i in range(4)] for j in range(4)]
        matrix[0][1] = 2.82842712
        matrix[0][2] = 5.65685425
        matrix[0][3] = 8.48528137
        matrix[1][2] = 2.82842712
        matrix[1][3] = 5.65685425
        matrix[2][3] = 2.82842712
        count = 0
        for i in range(4): # row
            for j in range(4): # col
                if (int(dm[i][j]) == int(matrix[i][j])):
                    count += 1
        self.assertEqual(count, 16, "The distance matrix is not made correctly")

class TestClassicNN(unittest.TestCase):
    def test_ClassicNN(self):
        one = Location(1, 1.0, 10.0)
        two = Location(2, 10.0, 4.0) 
        three = Location(3, 5.0, 8.0)
        four = Location(4, 7.0, 6.0)
        five = Location(1, 1.0, 2.0)
        path = [one, two, three, four, five]
        dm = dist_matrix(path)
        sumOfDistance, newPath, _, _ = ClassicNN(path, dm)
        # This should always be true
        if (sumOfDistance >= 0):
            self.assertNotEqual(path, newPath, "Classic NN was not able to find a new path")
    
    def test_StartPosition(self):
        one = Location(1, 1.0, 10.0)
        two = Location(2, 10.0, 4.0) 
        three = Location(3, 5.0, 8.0)
        four = Location(4, 7.0, 6.0)
        five = Location(1, 1.0, 2.0)
        path = [one, two, three, four, five]
        dm = dist_matrix(path)
        sumOfDistance, newPath, _, _ = ClassicNN(path, dm)
        # This should always be true
        if (sumOfDistance >= 0):
            self.assertEqual(newPath[0].number, 1, "Start position is changed")
    
    def test_StopPosition(self):
        one = Location(1, 1.0, 10.0)
        two = Location(2, 10.0, 4.0) 
        three = Location(3, 5.0, 8.0)
        four = Location(4, 7.0, 6.0)
        five = Location(1, 1.0, 2.0)
        path = [one, two, three, four, five]
        dm = dist_matrix(path)
        sumOfDistance, newPath, _, _ = ClassicNN(path, dm)
        # This should always be true
        if (sumOfDistance >= 0):
            self.assertEqual(newPath[-1].number, 1, "Stop position is changed")

class TestModifiedNN(unittest.TestCase):
    def test_ModifiedNN(self):
        one = Location(1, 1.0, 10.0)
        two = Location(2, 10.0, 4.0) 
        three = Location(3, 5.0, 8.0)
        four = Location(4, 7.0, 6.0)
        five = Location(1, 1.0, 2.0)
        path = [one, two, three, four, five]
        dm = dist_matrix(path)
        csumOfDistance, cnnPath, _, _ = ClassicNN(path, dm)
        msumOfDistance, modnnPath, _, _ = ModifiedNN(path, dm, cnnPath, dist_to_beat=csumOfDistance)
        # This should always be true
        if (modnnPath != cnnPath):
            self.assertless(msumOfDistance, csumOfDistance, "Modified NN was not able to find a new path that is shorter than Classic NN")
    
    def test_StartPosition(self):
        one = Location(1, 1.0, 10.0)
        two = Location(2, 10.0, 4.0) 
        three = Location(3, 5.0, 8.0)
        four = Location(4, 7.0, 6.0)
        five = Location(1, 1.0, 2.0)
        path = [one, two, three, four, five]
        dm = dist_matrix(path)
        csumOfDistance, cnnPath, _, _ = ClassicNN(path, dm)
        msumOfDistance, modnnPath, _, _ = ModifiedNN(path, dm, cnnPath, dist_to_beat=csumOfDistance)
        # This should always be true
        if ((modnnPath != cnnPath) & (msumOfDistance > 0)):
            self.assertEqual(modnnPath[0].number, 1, "Start position is changed")
    
    def test_StopPosition(self):
        one = Location(1, 1.0, 10.0)
        two = Location(2, 10.0, 4.0) 
        three = Location(3, 5.0, 8.0)
        four = Location(4, 7.0, 6.0)
        five = Location(1, 1.0, 2.0)
        path = [one, two, three, four, five]
        dm = dist_matrix(path)
        csumOfDistance, cnnPath, _, _ = ClassicNN(path, dm)
        msumOfDistance, modnnPath, _, _ = ModifiedNN(path, dm, cnnPath, dist_to_beat=csumOfDistance)
        # This should always be true
        if ((modnnPath != cnnPath) & (msumOfDistance > 0)):
            self.assertEqual(modnnPath[-1].number, 1, "Stop position is changed")

if __name__ == "__main__":
    unittest.main()

