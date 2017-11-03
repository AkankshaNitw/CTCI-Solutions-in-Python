def permPal(str):
    str.lower()
    check = [False]*26
    for ch in str:
        if check[ord(ch)-ord('a')] == False:
            check[ord(ch)-ord('a')] = True
        else:
            check[ord(ch) - ord('a')] = False
    if check.count(True) <= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    myString = "tactcammmml"
    if permPal(myString):
        print("It is a permutation of Palindrome!")
    else:
        print("It is not a permutation of Palindrome!")