fname= "characters.txt"
total,count=0,0

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
        if "|" in line:
            characterList = line.split("|")
            character = characterList[2]
        else:
            character = line[0]
        total += int(character)
        count += 1
    average = total/count
    print("The total years in the cast are {0}, average {1:.2f}".format(total,average))
    in_file.close()