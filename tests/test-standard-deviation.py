import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest

MAX_VALUE = 2147483647
MIN_VALUE = -2147483648

class TestStandardDeviation(unittest.TestCase):

  def testLowerBoundStandardDeviation(self):
    dataset = [MIN_VALUE, MIN_VALUE, 0, 0, 10]
    standardDeviation = calculator.standardDeviation(dataset)
    self.assertEqual(standardDeviation, 1176225237.7088258)

  def testUpperBoundStandardDeviation(self):
    dataset = [MAX_VALUE, 0, 0]
    standardDeviation = calculator.standardDeviation(dataset)
    self.assertEqual(standardDeviation, 1239850261.6757693)

  def testInvalidStandardDeviation(self):
    dataset = ['ok', 2, 3, 4, 5, 6]
    with self.assertRaises(Exception):
      standardDeviation = calculator.standardDeviation(dataset)

  def testNormalStandardDeviation(self):
    dataset = [1, 10, 1, 10, 1 , 10]
    standardDeviation = calculator.standardDeviation(dataset)
    self.assertEqual(standardDeviation, 4.898979485566356)

if __name__ == '__main__':
    unittest.main()