def process(str):
    return (str.strip()).replace(" ", "%20")

if __name__ == "__main__":
    myString = "Mr John    Smith   "
    print(process(myString))