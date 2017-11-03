def checkString(str1, str2):
    if abs(len(str1)-len(str2)) > 1:
        return(False)

    if len(str1) == len(str2):
        i=0
        flag = False
        while (i<len(str1)):
            if str1[i] != str2[i]:
                if flag == False:
                    flag = True
                    i += 1
                else:
                    return False
            else:
                i += 1




if __name__ == "__main__":
    myString1 = "pale"
    myString2 = "plale"
    if checkString(myString1, myString2):
        print("Strings are one edit away!")
    else:
        print("Strings are not one edit away!")