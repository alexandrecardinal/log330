import sys
import os.path
import unittest
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import calculator


MAX_VALUE = 2147483647
MIN_VALUE = -2147483648


class TestIndependant(unittest.TestCase):
    
    def testCorrelation(self):
        dataset = [(186, 15), (699, 69.9), (132, 6.5), (272, 22.4), (291, 28.4), (331, 65.9), (199, 19.4),
                   (1890, 189.7), (788, 38.8), (1601, 138.2)]
        correlation = calculator.correlation(dataset)
        self.assertAlmostEqual(correlation, 0.95592053, places=8)

    def testCorrelationUpper(self):
        dataset = [(MIN_VALUE, MIN_VALUE), (MAX_VALUE, MAX_VALUE)]
        correlation = calculator.correlation(dataset)
        self.assertEqual(correlation, 1)

    def testCorrelationLower(self):
        dataset = [(MIN_VALUE, MIN_VALUE), (MAX_VALUE, MIN_VALUE)]
        correlation = calculator.correlation(dataset)
        self.assertEqual(correlation, 0)

    def testCorrelationInvalid(self):
        dataset = [(0, "test")]
        with self.assertRaises(TypeError):
            calculator.correlation(dataset)


if __name__ == '__main__':
    unittest.main()
