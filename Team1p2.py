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
        cafe1 = random.normalvariate(H1, D1)
        cafe2 = random.normalvariate(H2, D2)
        cafe3 = random.normalvariate(H3, D3)
        happiness = happiness + cafe1 + cafe2 + cafe3
    return int(happiness) # return the whole integer value w/out decimals
# range of happiness value should be (1800, 5600)



# take input value of e (percent value)
def eGreedy(e=10): # Noah Cirks 
        # stores the overall happiness value
    H1 = 0
    H2 = 0
    H3 = 0
    # stores the average happiness value
    AH1 = []
    AH2 = []
    AH3 = []
    # stores how many times you have visited each cafeteria
    count1 = 0
    count2 = 0
    count3 = 0
    if e > 100 or e < 0:
        e = 10
    if e == int():
        e = 10
    # percentage of e
    percE = e
    # one run through for the first day

    while H1 == H2 or H1 == H3:  # -> change to if (maybe)
        H1 = random.randint(2, 18)
        H2 = random.randint(9, 21)
        H3 = random.randint(7, 19)
        AH1.append(H1)
        AH2.append(H2)
        AH3.append(H3)
        count1 += 1
        count2 += 1
        count3 += 1
        # print(H1, H2, H3)
    while H2 == H1 or H2 == H3:
        H1 = random.randint(2, 18)
        H2 = random.randint(9, 21)
        H3 = random.randint(7, 19)
        AH1.append(H1)
        AH2.append(H2)
        AH3.append(H3)
        count1 += 1
        count2 += 1
        count3 += 1
    while H3 == H2 or H3 == H1:
        H1 = random.randint(2, 18)
        H2 = random.randint(9, 21)
        H3 = random.randint(7, 19)
        AH1.append(H1)
        AH2.append(H2)
        AH3.append(H3)
        count1 += 1
        count2 += 1
        count3 += 1

    AH1.append(H1)
    AH2.append(H2)
    AH3.append(H3)

    # 297 because you went to a different cafeteria for the first three days
    for x in range(297):
        # chance they could come back as equal, not exactly sure how to get it to choose which one to go to.
        # without it directly changing the variable

        # if they are even this will run
        if H1 == H2 or H1 == H3:
            while H1 == H2 or H1 == H3:
                EQ1 = random.randint(1, 10)
                if EQ1 > 1:
                    count1 += 1
                    H1 += random.randint(2, 18)
                if EQ1 == 1:
                    EQ2 = random.randint(1, 2)
                    if EQ2 == 1:
                        H2 += random.randint(9, 21)
                        count2 += 1
                    if EQ2 == 2:
                        count3 += 1
                        H3 += random.randint(7, 19)
                # print(H1, H2, H3)
                # ^ for testing, no need to uncomment
        if H2 == H1 or H2 == H3:
            while H1 == H2 or H1 == H3:
                EQ1 = random.randint(1, 10)
                if EQ1 > 1:
                    count2 += 1
                    H2 += random.randint(9, 21)
                if EQ1 == 1:
                    EQ2 = random.randint(1, 2)
                    if EQ2 == 1:
                        count1 += 1
                        H1 += random.randint(2, 18)
                    if EQ2 == 2:
                        count3 += 1
                        H3 += random.randint(7, 19)

        if H3 == H2 or H3 == H1:
            while H1 == H2 or H1 == H3:
                EQ1 = random.randint(1, 10)
                if EQ1 > 1:
                    count3 += 1
                    H3 += random.randint(2, 18)
                if EQ1 == 1:
                    EQ2 = random.randint(1, 2)
                    if EQ2 == 1:
                        H2 += random.randint(9, 21)
                        count2 += 1
                    if EQ2 == 2:
                        count1 += 1
                        H1 += random.randint(2, 18)

        # running for each cafeteria
        if H1 > H2 and H1 > H3:
            x = 0
            if x == 0:
                dec = random.randint(1, 100)
                if dec > percE:
                    count1 += count1
                    H1 += random.randint(2, 18)
                    AH1.append(H1)
                if dec <= percE:
                    dec2 = random.randint(1, percE)
                    if dec2 < percE // 2:
                        count2 += count2
                        H2 += random.randint(9, 21)
                        AH2.append(H2)
                    if dec2 > percE // 2:
                        count3 += count3
                        H3 += random.randint(7, 19)
                        AH3.append(H3)
        if H2 > H1 and H2 > H3:
            x = 0
            if x == 0:
                dec = random.randint(1, 100)  # -> z = random.normalvariate(.01,1) change to
                if dec > percE:
                    count2 += count2
                    H2 += random.randint(9, 21)
                    AH2.append(H2)
                if dec <= percE:
                    dec2 = random.randint(1, percE)
                    if dec2 < percE // 2:
                        count1 += count1
                        H1 += random.randint(2, 18)
                        AH1.append(H1)
                    if dec2 > percE // 2:
                        count3 += count3
                        H3 += random.randint(7, 19)
                        AH3.append(H3)
        if H3 > H1 and H3 > H2:
            x = 0
            if x == 0:
                dec = random.randint(1, 100)
                if dec > percE:
                    count1 += count1
                    H3 += random.randint(7, 19)
                    AH3.append(H3)
                if dec <= percE:
                    dec2 = random.randint(1, percE)
                    if dec2 < percE // 2:
                        count2 += count2
                        H2 += random.randint(9, 21)
                        AH2.append(H2)
                    if dec2 > percE // 2:
                        count1 += count1
                        H1 += random.randint(2, 18)
                        AH1.append(H1)
    # calculating average happiness for each time going to a certain cafeteria
    AVG1 = 0
    AVG2 = 0
    AVG3 = 0
    print("This is Happiness for cafeteria 1 ->", H1)
    print("This is Happiness for cafeteria 2 ->", H2)
    print("This is Happiness for cafeteria 3 ->", H3)
    # OHAP - stands for optimal happiness

    for x in AH1:
        AVG1 = x + AVG1
    AVG1 = AVG1 // count1
    print(" Average Happiness for cafeteria 1 ->", AVG1)
    for x in AH2:
        AVG2 = x + AVG2
    AVG2 = AVG2 // count2
    print("Average Happiness for cafeteria 2 ->", AVG2)

    for x in AH3:
        AVG3 = x + AVG3
    AVG3 = AVG3 // count3
    print("Average Happiness for cafeteria 3 ->", AVG3)


# optimum happiness
# expected happiness
# expected regret
# run simulation, for t trials
# compare them to the expected values
# Monet :)
    def simulation (t,e):
    avgExplore = 0
    avgExploit = 0
    avgGreed = 0
    count = t
    # average
    while (count > 0):
       avgExplore = avgExplore + exploreOnly()
       avgExploit = avgExploit + exploitOnly()
       avgGreed = avgGreed + eGreedy(e)
       count = count - 1

    avgExplore = avgExplore/t
    avgExploit = avgExploit/t
    avgGreed = avgGreed/t

    # optimum 
    if (avgExplore > avgExploit and avgGreed):
        opt = avgExplore*t
    elif (avgExploit > avgExplore and avgGreed):
        opt = avgExploit*t
    else:
        opt = avgGreed*t

    # expected & regret explore
    exExplore = 100*cafe1 + 100*cafe2 + 100*cafe3 
    regExplore = opt - exExplore

    # expected & regret exploit
    exExploit = Happiness1 + Happiness2 + Happiness3 + 297*10
    regExploit = opt - exExploit

    # expected & regret greed
    rest = 100 - e
    hiday = (rest/100)*300
    lowday = ((e/3)/100)*300
    exGreed = H1*hiday + H1*lowday + H2+lowday + H3*lowday
    regGreed = opt - exGreed

    print ("Explore:\n")
    print ("Optimum: " + opt)
    print ("Expected: " + exExplore)
    print ("Regret: " + regExplore)
    print ("Average: " + avgExplore)

    print ("Exploit:\n")
    print ("Optimum: " + opt)
    print ("Expected: " + exExploit)
    print ("Regret: " + regExploit)
    print ("Average: " + avgExploit)

    print ("eGreedy:\n")
    print ("Optimum: " + opt)
    print ("Expected: " + exGreed)
    print ("Regret: " + regGreed)
    print ("Average: " + avgGreed)
