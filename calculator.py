import argparse
import csv
import math
import os.path


def initArguments():
    """ Reads the cmd arguments """
    parser = argparse.ArgumentParser(description='Compute the average, \
    variance and standard deviation OR the correlation')
    parser.add_argument('FILE', type=str, help='The path to the csv file')
    parser.add_argument('--correlation', action="store_true",
                        help='Calculate the correlation instead of the average, variance and \
    standard deviation.')
    parser.add_argument('--linear-regression', action="store_true",
                        help='Calculate the linear regression instead of the average, variance and \
    standard deviation.')
    parser.add_argument('--correlation-effort', action="store_true",
                        help='Calculate the correlation between effort spent on the 6 modules and the result \
    at the mid-term exam instead of the average, variance and standard deviation.')
    parser.add_argument('--confidence', action="store_true",
                        help='Calculate the confidence interval for 90% and 70% for \
                        a given csv file with estimated,real values.')

    return parser.parse_args()


def readCSV(csvPath):
    """ Reads simple values in a csv file """
    dataset = []
    with open(csvPath, 'r') as csvFile:
        csvReader = csv.reader(csvFile)
        for row in csvReader:
            dataset.append(float(''.join(row)))
    return dataset


def readTuplesCSV(csvPath):
    """ Reads the tuples in a csv """
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


def readEffortLinesCSV(csvPath):
    """ Reads the effortlines in a csv file """
    dataset = []
    if os.path.isfile(csvPath):
        with open(csvPath, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            for row in csvReader:
                effortRow = validateEffortRow(row)
                if effortRow:
                    dataset.append(effortRow)
        return dataset
    else:
        exit(1, "File not found " + csvPath)


def validateEffortRow(row):
    """ Validates effort rows and returns sum of Xs with Y as (sumX, Y)"""
    try:
        (name, c1, c2, c3, c4, c5, c6, y) = row
        c1 = float(c1.replace(',', '.'))
        c2 = float(c2.replace(',', '.'))
        c3 = float(c3.replace(',', '.'))
        c4 = float(c4.replace(',', '.'))
        c5 = float(c5.replace(',', '.'))
        c6 = float(c6.replace(',', '.'))
        y = float(y.replace(',', '.'))
        sumX = c1 + c2 + c3 + c4 + c5 + c6
        return (sumX, y)
    except Exception as e:
        print("Ignoring row {csvRow}".format(csvRow=row))
        return False


def validateTuple(row):
    """ Validates tuples """
    try:
        (x, y) = row
        x = float(x.replace(',', '.'))
        y = float(y.replace(',', '.'))
        return (x, y)
    except Exception as e:
        print("The row {csvRow} is invalid, skipping".format(csvRow=row))
        return False


def average(dataset):
    """ Computes average from dataset """
    avg = 0
    total = 0
    if len(dataset) == 0:
        return 0

    for value in dataset:
        total += value

    avg = total / len(dataset)
    return avg


def variance(dataset):
    """ Computes variance from dataset"""
    distanceSum = 0
    avg = average(dataset)

    for value in dataset:
        distanceWithAverage = value - avg
        squaredDistance = distanceWithAverage * distanceWithAverage
        distanceSum += squaredDistance

    var = distanceSum / (len(dataset) - 1)
    return var


def varianceFromLinearRegression(dataset, linearRegression):
    """ Computes variance from dataset and linearRegression """
    distanceSum = 0
    b0 = linearRegression[0]
    b1 = linearRegression[1]

    for pair in dataset:
        b1_x1 = b1 * pair[0]
        yi_b0_b1_xi = pair[1] - b0 - b1_x1
        squaredDistance = yi_b0_b1_xi * yi_b0_b1_xi
        distanceSum += squaredDistance

    var = distanceSum / (len(dataset) - 1)
    return var


def standardDeviation(dataset, linearRegression):
    """ Computes standard deviation from dataset and linearRegression if provided"""
    var = 0
    if linearRegression:
        var = varianceFromLinearRegression(dataset, linearRegression)
    else:
        var = variance(dataset, linearRegression)

    return math.sqrt(var)


def linearRegression(dataset):
    """ Computes linenar regression from dataset """
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
    """ Computes the linear regression from the length of a dataset,
    it's sum of X, sum of Y, sum of X * Y and sum of X * X 
    """
    if n == 0:
        return (0, 0)
    meanX = sumX / n
    meanY = sumY / n

    topB1 = sumXY - (n * meanX * meanY)
    bottomB1 = sumXX - (n * (meanX * meanX))

    if bottomB1 == 0:
        bottomB1 = 1

    b1 = topB1 / bottomB1
    b0 = meanY - (b1 * meanX)

    return (b0, b1)


def correlation(dataset):
    """ Computes the correlation in a (x, y) dataset """
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
    """ Computes the correlation for the length of the dataset and the sums """
    top = (n * sumXY - sumX * sumY)
    middle = (n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY)
    bottom = (math.sqrt(middle))

    if bottom == 0:
        return 0

    corr = top / bottom

    if corr < 0:
        corr = corr * -1
    return corr


def confidenceInterval(dataset, linearRegression, standardDeviation, confidence, estimation):
    """ Computes the confidence interval and returns the interval as a tuple"""
    totalDistance = 0
    listOfX = [row[0] for row in dataset]
    averageX = average(listOfX)
    length = len(dataset)
    tValue = 0
    
    if length != 10:
        raise Exception("Size of the dataset must be 10")

    if averageX == 0:
        return (0, 0)

    for pair in dataset:
        x = pair[0]
        distance = x - averageX
        squaredDistance = distance * distance
        totalDistance += squaredDistance

    squareRoot = math.sqrt(1 + (1 / length) +
                           ((estimation - averageX) * (estimation - averageX) / totalDistance))

    # using two-tails and 8 as liberty degree
    if confidence == 0.9:
        tValue = 1.86
    elif confidence == 0.7:
        tValue = 1.108
    else:
        raise Exception(
            "Can't use {invalidConfidence} as confidence, must be 0.9 or 0.7")

    predictedY = linearRegression[0] + (linearRegression[1] * estimation)
    interval = tValue * standardDeviation * squareRoot
    lowerInterval = predictedY - interval
    higherInterval = predictedY + interval

    return (lowerInterval, higherInterval)


if __name__ == '__main__':
    """ Main function """
    args = initArguments()
    isCorrelation = args.correlation
    isLinearRegression = args.linear_regression
    isCorrelationEffort = args.correlation_effort
    isConfidenceInterval = args.confidence

    if isConfidenceInterval:
        print("Is confidence")
        dataset = readTuplesCSV(args.FILE)
        linReg = linearRegression(dataset)
        standardDeviation = standardDeviation(dataset, linReg)
        (lower90, higher90) = confidenceInterval(
            dataset, linReg, standardDeviation, 0.9, 1119)
        (lower70, higher70) = confidenceInterval(
            dataset, linReg, standardDeviation, 0.7, 1119)

        print(("Avec un pourcentage de certitude de {percentage}%, mon intervalle " +
               "varie de {lowerInterval} à {higherInterval}. Ce qui fait que je suis certain " +
               "à {percentage}% que la taille de mon projet variera entre {lowerInterval} et " +
               "{higherInterval} LOC.").format(percentage=90, lowerInterval=lower90, higherInterval=higher90))

        print(("Avec un pourcentage de certitude de {percentage}%, mon intervalle " +
               "varie de {lowerInterval} à {higherInterval}. Ce qui fait que je suis certain " +
               "à {percentage}% que la taille de mon projet variera entre {lowerInterval} et " +
               "{higherInterval} LOC.").format(percentage=70, lowerInterval=lower70, higherInterval=higher70))

    elif isCorrelationEffort:
        dataset = readEffortLinesCSV(args.FILE)
        corr = correlation(dataset)
        print("Correlation: " + str(corr))
        if corr < 0.5:
            print("La corrélation entre les effort d'un étudiant et sa note est FAIBLE")
        else:
            print("La corrélation entre les effort d'un étudiant et sa note est FORTE")

    elif isCorrelation:
        dataset = readTuplesCSV(args.FILE)
        corr = correlation(dataset)
        print("Correlation: " + str(corr))

    elif isLinearRegression:
        dataset = readTuplesCSV(args.FILE)
        linReg = linearRegression(dataset)
        print("Linear regression: b0={b0} ; b1={b1}".format(
            b0=linReg[0], b1=linReg[1]))

    else:
        dataset = readCSV(args.FILE)
        print(dataset)

        avg = average(dataset)
        variance = variance(dataset)
        standardDeviation = standardDeviation(dataset)

        print('Average: ' + str(avg))
        print('Variance: ' + str(variance))
        print('Standard deviation: ' + str(standardDeviation))
