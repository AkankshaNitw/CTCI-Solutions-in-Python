def findMinDiff(myA):
    myA.sort()
    minDiff = abs(myA[0]-myA[1])
    for i in range(1, len(myA)-1):
        if abs(myA[i]-myA[i+1]) < minDiff:
            minDiff = abs(myA[i]-myA[i+1])
    return(minDiff)

if __name__ == "__main__":
    myArr = [4, 9, 1, 31, 13, 32, 32]
    print(findMinDiff(myArr))