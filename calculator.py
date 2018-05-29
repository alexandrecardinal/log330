import argparse
import csv
import math

def initArguments():
  parser = argparse.ArgumentParser(description='Compute the average, variance and standard deviation')
  parser.add_argument('FILE', type=str, help='The path to the csv file')

  return parser.parse_args()

def readCSV(csvPath):
  dataset = []
  with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
      dataset.append(float(''.join(row)))
  return dataset

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

if __name__ == "__main__":
  args = initArguments()
  dataset = readCSV(args.FILE)
  print(dataset)

  avg = average(dataset)
  variance = variance(dataset)
  standardDeviation = standardDeviation(dataset)

  print("Average: " + str(avg))
  print("Variance: " + str(variance))
  print("Standard deviation: " + str(standardDeviation))

