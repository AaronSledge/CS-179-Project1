#test all functions making sure they work properly
#everyone

import unittest
import math
from euclideanDistance import Euclidean
from randomS import randomSearch
from main import Location

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

class TestRandomS(unittest.TestCase):
    def test_randomFirstValue(self):
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

        sumOfdistance, path = randomSearch(testArray, math.inf)
        coordinates = (path[0].x, path[0].y)
        self.assertEqual(coordinates, (testArray[0].x, testArray[0].y), "Random search randomizes start point")




if __name__ == "__main__":
    unittest.main()

