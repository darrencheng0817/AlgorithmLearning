file=open("tempData.txt")
data=file.readlines()
for line in data:
    line = line.strip("\n")
    print("'"+line+"' +")