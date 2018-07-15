import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest


class TestCorrelationEffort(unittest.TestCase):

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

  def testValidateEffortRowInvalid(self):
    row = [("georges", "ok", "n", "importe", "quoi")]  
    validatedRow = calculator.validateEffortRow(row)
    self.assertEqual(validatedRow, False)

  def testValidateEffortRowValid(self):
    row = ["georges", "1", "10", "9,5", "3,0", "0", "1", "64"]
    validatedRow = calculator.validateEffortRow(row)
    self.assertEqual(validatedRow, (24.5, 64))

if __name__ == '__main__':
    unittest.main()