fname = "D:\pride and prejudice.txt"

try:
    in_file= open(fname,"r")
except FileNotFoundError:
    print("File not found - "+ fname)
    raise
except IOerror:
    print("Could not open the file "+ fname)
    raise
else:
    useLine=False
    allWords={}
    for line in in_file.readlines():
        if "End of the Project Gutenberg EBook" in line:
            useLine=False
        if useLine == True:
            text=line.replace(".",' ').replace(',',' ').replace('"',' ').replace(";",' ').replace("!",' ').replace("?",' ').lower()
            words=text.split()
            for word in words:
                if word not in allWords:
                    allWords[word]=1
                else:
                    allWords[word]+=1
        if "Produced by Anonymous Volunteers" in line:
            useLine=True
    max_key = max(allWords, key=allWords.get)
    print(max_key + " " + str(allWords[max_key]))
    in_file.close()