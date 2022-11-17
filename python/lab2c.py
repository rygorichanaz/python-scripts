numberSeconds = (int(input("Please enter the number of seconds: ")))

numberDays = numberSeconds//(60*60*24)
numberSeconds %= 60*60*24
numberHours = numberSeconds//(60*60)
numberSeconds %= 60*60
numberMinutes = numberSeconds//60
numberSeconds %= 60

print(str(numberDays) + " days " + str(numberHours) + " hours " + str(numberMinutes) + " minutes " + str(numberSeconds) + " seconds.")