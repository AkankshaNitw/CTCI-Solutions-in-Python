def checkDups(str):
    if len(str) > 128:
        return(True)
    else:
        check = [False]*128
        for ch in str:
            if check[ord(ch)]:
                return(True)
            else:
                check[ord(ch)] = True
    return (False)



if __name__ == "__main__":
    myString = "Test"
    if checkDups(myString):
        print("String has duplicates!")
    else:
        print("String has no duplicates!")