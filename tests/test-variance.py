import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest

MAX_VALUE = 2147483647
MIN_VALUE = -2147483648

class TestVariance(unittest.TestCase):

  def testLowerBoundVariance(self):
    dataset = [MIN_VALUE, MIN_VALUE, 0, 0, 10]
    variance = calculator.variance(dataset)
    self.assertEqual(variance, 1383505809823183688L)

  def testUpperBoundVariance(self):
    dataset = [MAX_VALUE, 0, 0]
    variance = calculator.variance(dataset)
    self.assertEqual(variance, 1537228671377473536L)

  def testInvalidVariance(self):
    dataset = ['ok', 2, 3, 4, 5, 6]
    with self.assertRaises(Exception):
      variance = calculator.variance(dataset)

  def testNormalVariance(self):
    dataset = [1, 10, 1, 10, 1 , 10]
    variance = calculator.variance(dataset)
    self.assertEqual(variance, 24)



if __name__ == '__main__':
    unittest.main()