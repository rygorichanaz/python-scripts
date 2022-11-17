fname= "characters.txt"
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
        print(line)
    in_file.close()