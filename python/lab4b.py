squares = int(input("Please enter the number of Squares: "))
wheatGrains = 1

for i in range(squares):
    print("Square {}: {} grains.".format(i+1,wheatGrains))
    wheatGrains *= 2