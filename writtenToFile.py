filename = open("writeToThisFile.csv","r")
data = filename.read()

##b00l = True
##while b00l == True:
##    count = 0
##    while count < 5:
##
##    b00l = False

list = data.split(",")
betterlist = []
count = 0
while count < len(list)-3:
    a = [list[count],list[count+1],list[count+2]]
    betterlist.append(a)
    count+=3

secondfile = open("writingToTheSecondFile.csv","w")
secondfile.write(str(betterlist))
secondfile.close()
