def acronymGenerator(name):
    nameList = name.split(" ")
    acronymName=""
    for i in nameList:
        acronymName += i[0]
    return acronymName

tempInput = input("Enter the name to cover to an Acronym: ")
print(acronymGenerator(tempInput))