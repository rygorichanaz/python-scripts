totalIntrusions = int(input("Please enter the number of intrusions: "))
daysTracked = int(input("Please enter the number of days tracked: "))
avgIntrusions = totalIntrusions/daysTracked

if(avgIntrusions < 20):
    print(str(avgIntrusions) + " Low")
elif(avgIntrusions >= 20) and (avgIntrusions < 100):
    print(str(avgIntrusions) + " Average")
elif(avgIntrusions >= 100) and (avgIntrusions < 200):
    print(str(avgIntrusions) + " High")
elif(avgIntrusions >= 200):
    print(str(avgIntrusions) + " Critical")