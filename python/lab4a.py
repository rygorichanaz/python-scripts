inputSteps = int(input("Enter the number of steps (-1 to quit) "))
totalSteps=0
countDays=0
mostSteps=inputSteps
leastSteps=inputSteps

while (inputSteps != -1): 
    if (inputSteps > mostSteps):
        mostSteps = inputSteps
    elif(inputSteps < leastSteps):
        leastSteps = inputSteps

    totalSteps += inputSteps
    countDays += 1
    inputSteps = int(input("Enter the number of steps (-1 to quit) "))

if(countDays!=0):
    avgSteps = totalSteps/countDays
else: avgSteps = 0

print("------------------------------")
print("Total steps {} over {} day(s) with an average of {} steps.".format(totalSteps,countDays,avgSteps))
print("The most steps in one day was {} and the lowest was {}.".format(mostSteps,leastSteps))
print("------------------------------")