ipAddress = ['11.16.211.2','133.1.1.111','201.22.3.41','17.55.23.123','144.211.32.45']

for i in ipAddress:
    address=i.split(".")
    if int(address[0]) < 128:
        print("Class A")
    elif int(address[0]) < 192:
        print("Class B")
    elif int(address[0]) < 224:
        print("Class C")