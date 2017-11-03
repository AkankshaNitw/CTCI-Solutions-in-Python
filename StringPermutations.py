def checkPerm1(str1, str2):
    if "".join(sorted(str1.lower())).strip() == "".join(sorted(str2.lower())).strip():
        return True
    else:
        return False

def checkPerm2(str1, str2):
    if len(str1)!=len(str2):
        return False
    else:
        check = [0]*256
        for c in str1:
            check[ord(c)] += 1
        for c in str2:
            check[ord(c)] -= 1
            if check[ord(c)] == -1:
                return False
        return True



if __name__ == "__main__":
    myStr1 = "Hello"
    myStr2 = "oHel"
    if checkPerm2(myStr1, myStr2):
        print("Strings are permutations")
    else:
        print("Strings are not permutations")