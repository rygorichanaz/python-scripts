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
            character = characterList[0]
        else:
            characterList = line.split(" ")
            character = characterList[2] + " " + characterList[3][:-1]
        print(character)
    in_file.close()