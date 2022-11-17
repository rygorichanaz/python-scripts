message = ""

def emailDomain(emailAddress):
    findDomain = emailAddress[emailAddress.find("@")+1:]
    return findDomain

for i in range(5):
    stringInput = input("Please enter an email address: ")
    if ("@" in stringInput):
        domain=(emailDomain(stringInput))
        print(domain)
        message += domain + " "
    else:
        print("Not a valid email address.")

print(message)