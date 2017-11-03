def compress(mystr):
    counter = 1
    current_ch = mystr[0]
    return_string = ""
    for e, ch in enumerate(mystr[1:]):
         if ch == current_ch:
            counter += 1
         else:
             return_string += current_ch + str(counter)
             current_ch = ch
             counter = 1
         print(e)
         if e == len(mystr) - 2:
             return_string += current_ch + str(counter)

    return (return_string)




if __name__ == "__main__":
    myString = "abbbbbbccccccc"
    print(compress(myString))