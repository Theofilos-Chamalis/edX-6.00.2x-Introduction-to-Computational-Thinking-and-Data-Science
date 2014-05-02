def sampleQuizzes():
    n = 0
    for i in range(10000):
        m1 = random.randrange(50,81)
        m2 = random.randrange(60,91)
        finl = random.randrange(55,96)
 
        total = 0.25*m1 + 0.25*m2 + finl*0.5
        if total >= 70 and total <= 75 :
            n = n+1
 
    p = n/ float (10000)
    return p