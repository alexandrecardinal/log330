import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest


class TestCorrelation(unittest.TestCase):

  def testAllZeroes(self):
    dataset = [
      (0, 0), 
      (0, 0), 
      (0, 0), 
      (0, 0),
      (0, 0)
    ]
    linearRegression = calculator.linearRegression(dataset)
    self.assertEqual(linearRegression, (0, 0))

  def testEmptyDataset(self):
    dataset = []
    linearRegression = calculator.linearRegression(dataset)
    self.assertEqual(linearRegression, (0, 0))

  def testNormalCondition(self):
    dataset = [
      (130, 186),
      (650, 699),
      (99, 132),
      (150, 272),
      (128, 291),
      (302, 331),
      (95, 199),
      (945, 1890),
      (368, 788),
      (961, 1601)
    ]
    linearRegression = calculator.linearRegression(dataset)
    self.assertEqual(linearRegression, (-22.552532752034267, 1.727932426206986))

if __name__ == '__main__':
    unittest.main()