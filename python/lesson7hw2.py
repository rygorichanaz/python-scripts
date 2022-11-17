import os
fOutName = 'log.txt'
out_file = open(fOutName,"w")

def findText(fname):
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
            if ("GET" in line) and (".html" in line):
                htmlList = line.split(" ")
                data1 = htmlList[0]
                data2 = htmlList[3]
                data3 = htmlList[5]
                out_file.write("{}|{}|{}\n".format(data1,data3,data2))
        in_file.close()


for root,dirs,files in os.walk('D:\All logs'):
    for f in files:
        if os.path.splitext(f)[1] == '.log':
            fullPath = os.path.join(root,f)
            findText(fullPath)

out_file.close()
print("Job complete. File saved to {}.".format(fOutName))