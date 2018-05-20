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


def variance(dataset, average):
  distanceSum = 0

  for value in dataset:
    distanceWithAverage = value - average
    squaredDistance = distanceWithAverage * distanceWithAverage
    distanceSum += squaredDistance

  variance = distanceSum / (len(dataset) - 1)
  return variance

def standardDeviation(variance):
  return math.sqrt(variance)

if __name__ == "__main__":
  args = initArguments()
  dataset = readCSV(args.FILE)
  print(dataset)

  average = average(dataset)
  variance = variance(dataset, average)
  standardDeviation = standardDeviation(variance)

  print ("Average: " + str(average))
  print("Variance: " + str(variance))
  print("Standard deviation: " + str(standardDeviation))

