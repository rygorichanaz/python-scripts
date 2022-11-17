clothing = input("Describe an item of clothing that is a knitted top that is half way between black and white: ")
bankNote = input("How would you Describe paying for it using a bank note? ")
britPoint=0
americaPoint=0

if ("grey" in clothing):
    britPoint+=1
elif ("gray" in clothing):
    americaPoint+=1

if ("pullover" in clothing):
    britPoint+=1
elif ("sweater" in clothing):
    americaPoint+=1

if ("cheque" in bankNote):
    britPoint+=1
elif("check" in bankNote):
    americaPoint+=1

if (britPoint > americaPoint):
    print("You are a Brit.")
elif (americaPoint > britPoint):
    print("You are American.")
else:
    print("You are awful at answering questions.")