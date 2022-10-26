import random

#first 3 days, visit each cafeteria
def exploitOnly():
    pass

# random libray -> random.normalvariate(mean, deviation)
# happiness  = random.normalvariate(H1, D1)
# visit each cafeteria 100 times
# C1; 100
# C2: 100
# C3: 100
# Each day calculate happiness based on normal distribution w/certain mean and standard deviation
# return the total sum of happiness value

# one for loop
# for i in range(100) gen c1 . c2, c3
def exploreOnly2(): # Akosua
    happiness = 0 #(for all 300 days)
    for days in range(100):
        cafe1 = random.normalvariate(10, 8)
        cafe2 = random.normalvariate(15, 6)
        cafe3 = random.normalvariate(12, 5)
        happiness = happiness + int(cafe1) + int(cafe2) + int(cafe3)
    return happiness
# range of happiness value should be (1800, 5600)



# take input value of e (percent value)
def eGreedy(e=10): # Noah Cirks 
    pass

# optimum happiness
# expected happiness
# expected regret
# run simulation, for t trials
# compare them to the expected values
def simu(): #Monet :)
    pass
