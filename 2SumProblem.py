def my2Sum(myL, myN):
    myL.sort()
    i = 0
    j = len(myL)-1
    #print (i)
    while i<=j:
        if myL[i] + myL[j] == myN:
            #print (i, j)
            return(i, j)
        elif myL[i] + myL[j] < myN:
            i += 1
        else:
            j -= 1





if __name__ == "__main__":
    myList = [2, 4, 6, 8, 10]
    #print(myList)
    myNum = 8
    #print("Here!")
    print(my2Sum(myList, myNum))