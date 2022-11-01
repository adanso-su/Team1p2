import random
from random import randint
H1 = 10
D1 = 8
H2 = 15
D2 = 6
H3 = 12
D3 = 5
def eGreedy(e = 10):
    # if e is not between 0-100, then stop running eGreedy part
    if e < 0 or e > 100:
        print("e should be between 0 and 100")
        exit(1)
    # create a list for happiness and standard deviation
    H = [H1, H2, H3]
    D = [D1, D2, D3]
    # initial value of sum, max happiness
    sumHappiness = 0
    maxHappiness = 0
    # initial max index is a random selection between 1 to 3 (1,2,3), because there will be no value for max happiness if first day randomly chose to go to the max happiness cafeteria
    maxIndex = random.randint(1,3)
    # initial accumulated number of day which chose to go random cafeteria, which means e% days of 300 days
    accumulatedRandomNum = 0
    # initial total number of day i
    i = 0
    while i < 300:
        # generate random selection between 0 to 1, 0 stand for go to random cafeteria, and 1 stand for go to the max happiness cafeteria
        randomSelect = random.randint(0,1)
        if randomSelect == 0:
            # this part gonna stop stop after e% of total 300 days
            if accumulatedRandomNum >= 300*e/100:
                continue
            accumulatedRandomNum += 1
            selectCafeterias = random.randint(0,2)
            if selectCafeterias == 0:
                Happiness = random.normalvariate(H1, D1)
            elif selectCafeterias == 1:
                Happiness = random.normalvariate(H2, D2)
            else:
                Happiness = random.normalvariate(H3, D3)
            if Happiness > maxHappiness:
                maxHappiness = Happiness
                maxIndex = selectCafeterias
        else:
            h = H[maxIndex]
            d = D[maxIndex]
            Happiness = random.normalvariate(h,d)
            maxHappiness = Happiness
        sumHappiness += Happiness
        i += 1
    return sumHappiness
