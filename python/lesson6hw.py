participants=["Bob","Sue","Craig","Eric","Lisa","Jennifer"]
guessWho=input("Please enter a name: ")
isAPart=False

for i in participants:
    if guessWho == i:
        print("{} is a participant".format(guessWho))
        isAPart=True
        break

if isAPart == False:
    print("{} is not a participant".format(guessWho))