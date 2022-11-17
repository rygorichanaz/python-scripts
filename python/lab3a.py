def whatToOut(intrusionValue):
    if(intrusionValue < 20):
        return "Low"
    elif(intrusionValue < 100):
        return "Average"
    elif(intrusionValue < 200):
        return "High"
    else:
        return "Critical"

totalIntrusions = int(input("Please enter the number of intrusions: "))
daysTracked = int(input("Please enter the number of days tracked: "))
avgIntrusions = totalIntrusions/daysTracked
print(str(avgIntrusions) + " " + whatToOut(avgIntrusions))