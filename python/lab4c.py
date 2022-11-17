amountToSave = float(input("Enter the amount you'd like to save: "))
monthlyDeposit = float(input("Enter your monthly deposit: "))
annualInterest = float(input("Enter the annual interest: "))

monthInterest = annualInterest/1200
savedAmount = 0
monthCounter = 0

while (savedAmount < amountToSave):
    savedAmount += (savedAmount*monthInterest) + monthlyDeposit
    monthCounter += 1
    print("Month {} has ${:,.2f} saved".format(monthCounter,savedAmount))

print("--------------------")
print("It will take {} month(s) to save ${:,.2f}".format(monthCounter,amountToSave))
print("--------------------")