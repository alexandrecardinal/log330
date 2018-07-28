import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator
import unittest


class TestCorrelation(unittest.TestCase):
  confidence = 0.9
  estimation = 1119

  def testAllZeroes(self):
    dataset = [
      (0, 0), 
      (0, 0), 
      (0, 0), 
      (0, 0),
      (0, 0),
      (0, 0),
      (0, 0),
      (0, 0),
      (0, 0),
      (0, 0)
    ]
    linReg = calculator.linearRegression(dataset)
    standardDeviation = calculator.standardDeviation(dataset, linReg)
    (lowerInterval, higherInterval) = calculator.confidenceInterval(dataset, linReg, standardDeviation, self.confidence, self.estimation)

    self.assertEqual((lowerInterval, higherInterval), (0, 0))

  def testEmptyDataset(self):
    dataset = []
    linReg = calculator.linearRegression(dataset)
    standardDeviation = calculator.standardDeviation(dataset, linReg)

    with self.assertRaises(Exception):
      (lowerInterval, higherInterval) = calculator.confidenceInterval(dataset, linReg, standardDeviation, self.confidence, self.estimation)

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
    linReg = calculator.linearRegression(dataset)
    standardDeviation = calculator.standardDeviation(dataset, linReg)

    (lowerInterval, higherInterval) = calculator.confidenceInterval(dataset, linReg, standardDeviation, self.confidence, self.estimation)
    self.assertEqual((lowerInterval, higherInterval), (1471.4585277625715, 2350.5491765845945))

if __name__ == '__main__':
    unittest.main()