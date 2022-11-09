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
    H1List = []
    H2List = []
    H3List = []
    Happiness1 = random.normalvariate(H1, D1)
    Happiness2 = random.normalvariate(H2, D2)
    Happiness3 = random.normalvariate(H3, D3)
    Happiness = [Happiness1, Happiness2, Happiness3]
    maxIndex = Happiness.index(max(Happiness))
    sumHappiness = Happiness1 + Happiness2 + Happiness3
    H1List.append(Happiness1)
    H2List.append(Happiness2)
    H3List.append(Happiness3)
    for i in range(297):
        r = random.random()
        if r < e / 100:
            selectCafeterias = random.randint(0, 2)
            if selectCafeterias == 0:
                timeHappiness = random.normalvariate(H1, D1)
                H1List.append(timeHappiness)
            elif selectCafeterias == 1:
                timeHappiness = random.normalvariate(H2, D2)
                H2List.append(timeHappiness)
            else:
                timeHappiness = random.normalvariate(H3, D3)
                H3List.append(timeHappiness)
        else:
            h = H[maxIndex]
            d = D[maxIndex]
            timeHappiness = random.normalvariate(h, d)
            if maxIndex == 0:
                H1List.append(timeHappiness)
            elif maxIndex == 1:
                H2List.append(timeHappiness)
            else:
                H3List.append(timeHappiness)
        average1 = sum(H1List) / len(H1List)
        average2 = sum(H2List) / len(H2List)
        average3 = sum(H3List) / len(H3List)
        averageList = [average1, average2, average3]
        maxIndex = averageList.index(max(averageList))
        sumHappiness += timeHappiness
    return sumHappiness
