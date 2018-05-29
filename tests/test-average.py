import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest

MAX_VALUE = 2147483647
MIN_VALUE = -2147483648

class TestAverage(unittest.TestCase):

  def testLowerBoundAverage(self):
    dataset = [MIN_VALUE, MIN_VALUE, MIN_VALUE]
    average = calculator.average(dataset)
    self.assertEqual(average, MIN_VALUE)

  def testInvalidAverage(self):
    dataset = [23, 45, "ok"]
    with self.assertRaises(Exception):
      average = calculator.average(dataset)

  def testUpperBoundAverage(self):
    dataset = [MAX_VALUE, MAX_VALUE, MAX_VALUE]
    average = calculator.average(dataset)
    self.assertEqual(average, MAX_VALUE)

  def testNormalAverage(self):
    dataset = [1, 3, 5]
    average = calculator.average(dataset)
    self.assertEqual(average, 3)



if __name__ == '__main__':
    unittest.main()