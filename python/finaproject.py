# take file input || code from ppt || and set file output
fname = "expinput.txt"
fOutName = "expoutput.csv"
out_file = open(fOutName, "w")

try:
    in_file= open(fname,"r")
except FileNotFoundError:
    print("File not found - "+ fname)
    raise
except IOerror:
    print("Could not open the file "+ fname)
    raise
else:
    contribList = [0,"",0.0,0]
    contribID = 0
    for line in in_file.readlines():
        # parse line into list of comma sep values
        lineList = line.split(',')
        if contribList[0] != lineList[0] and contribList[0] != 0:
            # output to .csv file
            out_file.write("{},{},{:.2f},{}\n".format(contribList[0],contribList[1],contribList[2],contribList[3]))
        # check if contrib number is in list
        if contribID == int(lineList[0]):            
            # add values to contribList
            if ".00" in lineList[3]:# check if line contains donation
                contribList[2] += float(lineList[3])
            if lineList[2].isdigit():# check if line contains volunteer hours
                contribList[3] += int(lineList[2])
        else:
            # check if value is a not a name -- looks like dates fill this space in the input
            if "/" in lineList[1]:
                contribName = ""
                # create new contribList || [contrib number, name, donation amount, hours]
                contribList = [lineList[0],contribName,0.0,0]
                # add values to new contribList
                if ".00" in lineList[3]:# check if line contains donation
                    contribList[2] += float(lineList[3])
                if lineList[2].isdigit():# check if line contains volunteer hours
                    contribList[3] += int(lineList[2])
            else:
                # concatenate first and last name
                contribName = lineList[2] + lineList[1]
                # create new contribList || contrib number, first and last name, donation amount, hours
                contribList = [lineList[0],contribName,0.0,0]
        # set contribID for following pass of loop
        contribID = int(contribList[0])
    in_file.close()
    out_file.close()