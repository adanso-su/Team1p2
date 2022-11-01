import random
from random import randint
H1 = 10
D1 = 8
H2 = 15
D2 = 6
H3 = 12
D3 = 5
def eGreedy(e = 10):
    if e < 0 or e > 100:
        print("e should be between 0 and 100")
        exit(1)
    H = [H1, H2, H3]
    D = [D1, D2, D3]
    sumHappiness = 0
    maxHappiness = 0
    maxIndex = random.randint(0,2)
    accumulatedRandomNum = 0
    i = 0
    while i < 300:
        randomSelect = random.randint(0,1)
        if randomSelect == 0:
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
