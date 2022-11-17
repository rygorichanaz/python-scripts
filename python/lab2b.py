moneyAmount = float(input("Please enter you money amount: "))
moneyAmount = int(moneyAmount*100)

twentyDollarBills = moneyAmount//2000
moneyAmount %= 2000
tenDollarBills = moneyAmount//1000
moneyAmount %= 1000
fiveDollarBills = moneyAmount//500
moneyAmount %= 500
oneDollarBills = moneyAmount//100
moneyAmount %= 100
quarterCoins = moneyAmount//25
moneyAmount %= 25
dimeCoins = moneyAmount//10
moneyAmount %= 10
nickelCoins = moneyAmount//5
moneyAmount %= 5
pennyCoins = moneyAmount//1

if (twentyDollarBills > 0):
    print(str(twentyDollarBills) + " 20 dollar bills.")
if (tenDollarBills > 0):
    print(str(tenDollarBills) + " 10 dollar bills.")
if (fiveDollarBills > 0):
    print(str(fiveDollarBills) + " 5 dollar bills.")
if (oneDollarBills > 0):
    print(str(oneDollarBills) + " 1 dollar bills.")
if (quarterCoins > 0):
    print(str(quarterCoins) + " quaters.")
if (dimeCoins > 0):
    print(str(dimeCoins) + " dimes.")
if (nickelCoins > 0):
    print(str(nickelCoins) + " nickels.")
if (pennyCoins > 0):
    print(str(pennyCoins) + " pennies.")