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
