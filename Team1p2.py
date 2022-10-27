import random
H1 = 10
D1 = 8
H2 = 15
D2 = 6
H3 = 12
D3 = 5
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
    return sumHappiness

# random libray -> random.normalvariate(mean, deviation)
# happiness  = random.normalvariate(H1, D1)
# visit each cafeteria 100 times (C1, C2, C3)
# Each day calculate happiness based on normal distribution w/certain mean and standard deviation
# return the total sum of happiness value
def exploreOnly(): # Akosua
    happiness = 0 #(for all 300 days)
    for days in range(100):
        cafe1 = random.normalvariate(10, 8)
        cafe2 = random.normalvariate(15, 6)
        cafe3 = random.normalvariate(12, 5)
        happiness = happiness + cafe1 + cafe2 + cafe3
    return int(happiness) # return the whole integer value w/out decimals
# range of happiness value should be (1800, 5600)



# take input value of e (percent value)
def eGreedy(e=10): # Noah Cirks 
    pass

# optimum happiness
# expected happiness
# expected regret
# run simulation, for t trials
# compare them to the expected values
def simu(): # Monet :)
    pass
