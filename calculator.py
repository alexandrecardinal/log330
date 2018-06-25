import argparse
import csv
import math
import os.path

def initArguments():
  parser = argparse.ArgumentParser(description='Compute the average, \
    variance and standard deviation OR the correlation')
  parser.add_argument('FILE', type=str, help='The path to the csv file')
  parser.add_argument('--correlation', action="store_true",\
    help='Calculate the correlation instead of the average, variance and \
    standard deviation.')
  parser.add_argument('--linear-regression', action="store_true",\
    help='Calculate the linear regression instead of the average, variance and \
    standard deviation.')

  return parser.parse_args()

def readCSV(csvPath):
  dataset = []
  with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
      dataset.append(float(''.join(row)))
  return dataset

def readTuplesCSV(csvPath):
  dataset = []
  if os.path.isfile(csvPath):
    with open(csvPath, 'r') as csvFile:
      csvReader = csv.reader(csvFile, delimiter=';')
      for row in csvReader:
        cleanedRow = validateTuple(row)
        if cleanedRow:
          dataset.append(cleanedRow)
    return dataset
  else:
    exit(1, "File not found")

def validateTuple(row):
  try:
    (x, y) = row
    x = float(x.replace(',', '.'))
    y = float(y.replace(',', '.'))
    return (x, y)
  except Exception as e:
    print("The row {csvRow} is invalid, skipping".format(csvRow=row))
    return False

def average(dataset):
  avg = 0
  total = 0

  for value in dataset:
    total += value

  avg = total / len(dataset)
  return avg


def variance(dataset):
  distanceSum = 0
  avg = average(dataset)

  for value in dataset:
    distanceWithAverage = value - avg
    squaredDistance = distanceWithAverage * distanceWithAverage
    distanceSum += squaredDistance

  var = distanceSum / (len(dataset) - 1)
  return var

def standardDeviation(dataset):
  var = variance(dataset)
  return math.sqrt(var)

def linearRegression(dataset):
  sumX = 0
  sumY = 0
  sumXY = 0
  sumXX = 0
  sumYY = 0
  for i in dataset:
    sumX += i[0]
    sumY += i[1]

    sumXX += i[0] * i[0]
    sumXY += i[0] * i[1]

  return computeLinearRegressionFormula(len(dataset), sumX, sumY, sumXY, sumXX)

def computeLinearRegressionFormula(n, sumX, sumY, sumXY, sumXX):
  if n == 0:
    return (0, 0)
  meanX = sumX / n
  meanY = sumY / n

  topB1 = sumXY - ( n * meanX * meanY)
  bottomB1 = sumXX - ( n * (meanX * meanX))
  
  if bottomB1 == 0:
    bottomB1 = 1

  b1 = topB1 / bottomB1
  b0 = meanY - (b1 * meanX)

  return (b0, b1)

def correlation(dataset):
  sumX = 0
  sumY = 0
  sumXY = 0
  sumXX = 0
  sumYY = 0
  for i in dataset:
    sumX += i[0]
    sumY += i[1]

    sumXY += i[0] * i[1]
    sumXX += i[0] * i[0]
    sumYY += i[1] * i[1]

  return computeCorrelationFormula(len(dataset), sumX, sumY, sumXY, sumXX, sumYY)

def computeCorrelationFormula(n, sumX, sumY, sumXY, sumXX, sumYY):
  top = (n * sumXY - sumX * sumY)
  middle = (n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY)
  bottom = (math.sqrt(middle))

  if bottom == 0:
    return 0

  corr = top / bottom

  if corr < 0:
    corr = corr * -1
  return corr

if __name__ == '__main__':
  args = initArguments()
  isCorrelation = args.correlation
  isLinearRegression = args.linear_regression

  if isCorrelation:
    dataset = readTuplesCSV(args.FILE)
    corr = correlation(dataset)
    print("Correlation: " + str(corr))

  elif isLinearRegression:
    dataset = readTuplesCSV(args.FILE)
    linReg = linearRegression(dataset)
    print("Linear regression: b0={b0} ; b1={b1}".format(b0=linReg[0], b1=linReg[1]))

  else:
    dataset = readCSV(args.FILE)
    print(dataset)

    avg = average(dataset)
    variance = variance(dataset)
    standardDeviation = standardDeviation(dataset)

    print('Average: ' + str(avg))
    print('Variance: ' + str(variance))
    print('Standard deviation: ' + str(standardDeviation))