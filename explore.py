import random 
H1 = 10
D1 = 8
H2 = 15
D2 = 6
H3 = 12
D3 = 5
# random libray -> random.normalvariate(mean, deviation)
# happiness  = random.normalvariate(H1, D1)
# visit each cafeteria 100 times
# C1; 100
# C2: 100
# C3: 100
# Each day calculate happiness based on normal distribution w/certain mean and standard deviation
# return the total sum of happiness value
# average = 100*H1 + 100*H2+100*3
# regret = 3000-average

def exploreOnly():
    count = 0
    happiness = 0 # (for all 300 days)
    # cafe 1
    while count < 100:
        # generate a happiness value based on the cafeteria
        i = random.normalvariate(10, 8)
        happiness = happiness + i
        count += 1
    # cafe 2
    count = 0
    while count < 100:
        # generate a happiness value based on the cafeteria
        i = random.normalvariate(15, 6)
        happiness = happiness + i
        count += 1
    count = 0
    # cafe 3
    while count < 100:
        # generate a happiness value based on the cafeteria
        i = random.normalvariate(12, 5)
        happiness = happiness + i
        count += 1
    return int(happiness)
# range of happiness value should be (1800, 5600)


# one for loop
# for i in range(100) gen c1 . c2, c3
def exploreOnly2():
    happiness = 0 #(for all 300 days)
    for days in range(100):
        cafe1 = random.normalvariate(10, 8)
        cafe2 = random.normalvariate(15, 6)
        cafe3 = random.normalvariate(12, 5)
        happiness = happiness + int(cafe1) + int(cafe2) + int(cafe3)
    return happiness
# range of happiness value should be (1800, 5600)

def exploreOnly3():
    happiness = 0 #(for all 300 days)
    for days in range(100):
        cafe1 = random.normalvariate(H1, D1)
        cafe2 = random.normalvariate(H2, D2)
        cafe3 = random.normalvariate(H3, D3)
        happiness = happiness + int(cafe1) + int(cafe2) + int(cafe3)
    return happiness
# range of happiness value should be (1800, 5600)

#first 3 days, visit each cafeteria
def exploitOnly2():
    happinessvalue = 0
    for i in range(1):
        cafe1 = random.normalvariate(10, 8)
        cafe2 = random.normalvariate(15, 6)
        cafe3 = random.normalvariate(12, 5)
        happinessvalue = happinessvalue + cafe1 + cafe2 + cafe3

    if cafe1 > cafe2 and cafe1 > cafe3:
        for days in range(297): # rest of the 297 days
            cafe1 = random.normalvariate(10, 8)
            happinessvalue = happinessvalue + cafe1
    elif cafe2 > cafe1 and cafe2 > cafe3:
        for days in range(297): # rest of the 297 days
            cafe2 = random.normalvariate(15, 6)
            happinessvalue = happinessvalue + cafe2
    elif cafe3 > cafe1 and cafe3 > cafe2:
        for days in range(297): # rest of the 297 days
            cafe3 = random.normalvariate(12, 5)
            happinessvalue = happinessvalue + cafe3
    return int(happinessvalue)
# range of happiness value should be (1800, 5600)



#first 3 days, visit each cafeteria
def exploitOnly(): # Yuchao
    H = [H1, H2, H3]
    D = [D1, D2, D3]
    Happiness1 = random.normalvariate(H1, D1)
    Happiness2 = random.normalvariate(H2, D2)
    Happiness3 = random.normalvariate(H3, D3)
    Happiness = [Happiness1, Happiness2, Happiness3]
    maxIndex = Happiness.index(max(Happiness))
    sumHappiness = Happiness1 + Happiness2 + Happiness3
    for i in range(297):
        tempHappiness = random.normalvariate(H[maxIndex], D[maxIndex])
        sumHappiness += tempHappiness
    return int(sumHappiness)