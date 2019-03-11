# How do you find the missing number in a given integer array of 1 to 100?
def missingnumber(n, m, duplList):
    for num in range(n,m):
        currentnum = num
        count = 0
        for x in duplList:
            if currentnum == x:
                count += 1
        if count == 0:
            return currentnum

dupList =  list(range(100))
dupList[23] = 22
dupnumber = missingnumber(1,100, dupList)
print("The missing number is " + str(dupnumber))