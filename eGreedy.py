import random
H1 = 10
D1 = 8
H2 = 15
D2 = 6
H3 = 12
D3 = 5
def eGreedy(e=10):
    if e < 0 or e > 100:
        print("e should be between 0 and 100")
        exit(1)
    H = [H1, H2, H3]
    D = [D1, D2, D3]
    Happiness1 = random.normalvariate(H1, D1)
    Happiness2 = random.normalvariate(H2, D2)
    Happiness3 = random.normalvariate(H3, D3)
    Happiness = [Happiness1, Happiness2, Happiness3]
    maxIndex = Happiness.index(max(Happiness))
    maxHappiness = Happiness[maxIndex]
    sumHappiness = Happiness1 + Happiness2 + Happiness3
    for i in range(297):
        r = random.random()
        if r < e / 100:
            selectCafeterias = random.randint(0, 2)
            if selectCafeterias == 0:
                timeHappiness = random.normalvariate(H1, D1)
            elif selectCafeterias == 1:
                timeHappiness = random.normalvariate(H2, D2)
            else:
                timeHappiness = random.normalvariate(H3, D3)
            if timeHappiness > maxHappiness:
                maxHappiness = timeHappiness
                maxIndex = selectCafeterias
        else:
            h = H[maxIndex]
            d = D[maxIndex]
            timeHappiness = random.normalvariate(h, d)
            maxHappiness = max(timeHappiness, maxHappiness)
        sumHappiness += timeHappiness
    return sumHappiness
print(eGreedy(10))
