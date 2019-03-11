# How do you find the duplicate number on a given integer array?

def duplicatenumber(n, m, duplList):
    for num in range(n,m):
        currentnum = num
        count = 0
        for x in duplList:
            if currentnum == x:
                count += 1
        if count == 2:
            return currentnum

dupList =  list(range(100))
dupList[23] = 22
dupnumber = duplicatenumber(1,100, dupList)
print("The duplicate number is " + str(dupnumber))