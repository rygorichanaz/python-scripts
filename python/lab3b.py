print("--------Gaming Tool--------")
systemCost = int(input("How much is the system? "))
numberA = int(input("How many A's did you earn last Semester? "))
numberB = int(input("How many B's did you earn last Semester? "))
numberDF = int(input("How many grades below a C did you earn last Semester? "))
hoursHomework = int(input("How many hours of homework? "))
hoursHousework = int(input("How many hours of house work? "))
hoursSports = int(input("How many hours of sports? "))

def canYouBuy():
    currentMoney = (numberA * 150) + (numberB * 75) + (numberDF * -150)
    if (currentMoney >= systemCost):
        return "You may buy a gaming system."
    else:
        return "You may not buy a gaming system."

def timeToPlay():
    currentTime = (hoursHomework//2) + (hoursHousework//3) + (hoursSports//4)
    return("You have earned {} hours of play time.".format(currentTime))

print ("--------------------")
print (canYouBuy())
print (timeToPlay())