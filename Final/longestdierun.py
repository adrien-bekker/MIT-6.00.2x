import random, pylab as plt

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """

    plt.hist(values, bins=numBins)

    if title != None:
        plt.title(title)
    
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    longest_list = []
    for i in range(numTrials):
        current = 1
        longest = 0
        prevRoll = 0
        for k in range(numRolls):
            roll = die.roll()
            if roll == prevRoll:
                current += 1
            else:
                if current > longest:
                    longest = current
                current = 1
            prevRoll = roll
        if current > longest:
          longest_list.append(current)
        else:
          longest_list.append(longest)
    
    makeHistogram(longest_list, 10, "Streak #", "# of Trials")

    return round(sum(longest_list) / len (longest_list), 3)

die = Die([1])
getAverage(die, 10, 100)