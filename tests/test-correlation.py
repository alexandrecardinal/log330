import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest


class TestCorrelation(unittest.TestCase):

  # We expect a correlation of '-1.0' that has been made absolute (|correlation|)
  def testCorrelationInverse(self):
    dataset = [(-30, 30), (30, -30)]
    correlation = calculator.correlation(dataset)
    self.assertEqual(correlation, 1.0)

  def testDirectCorrelation(self):
    dataset = [(1, 2), (2, 4)]
    correlation = calculator.correlation(dataset)
    self.assertEqual(correlation, 1.0)

  def testNoCorrelationAtAll(self):
    dataset = [(-5, 10), (5, 10)]
    correlation = calculator.correlation(dataset)
    self.assertEqual(correlation, 0.0)


if __name__ == '__main__':
    unittest.main()