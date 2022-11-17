fname= "log.txt"

try:
    in_file= open(fname,"r")
except FileNotFoundError:
    print("File not found "+ fname)
    raise
except IOerror:
    print("could not open the file "+ fname)
    raise
else:
    for line in in_file.readlines():
        if ("GET" in line) and ("html" in line):
            htmlList = line.split(" ")
            data1 = htmlList[0]
            data2 = htmlList[3]
            data3 = htmlList[5]
            print("{}|{}|{}".format(data1,data3,data2))
    in_file.close()