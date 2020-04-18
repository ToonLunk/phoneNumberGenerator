def getNumber(): # this function accepts the number, and returns its numeric equivalent

    realNum = "" # initialize the variable

    number = str(input("Please enter the phone number in this format: 'XXX-XXX-XXXX' using alphanumeric characters:"))

    trueNumber = ""

    for letter in number: # this loop removes dashes from number and adds them to a new variable
        if letter == "-": # remove dashes
            letter = "" # turn them into nothing (delete them)
            trueNumber += letter # add that number/letter to trueNumber variable
        else: # if it wasn't a dash (-), add it to the trueNumber variable
            trueNumber += letter

    for char in number: # for every character in the number, do this:
        char = char.lower().rstrip() # strip the character of whitespace and make it lowercase (for ease)

        if char == "-":
            char = ""
        if char == "a" or char == "b" or char == "c": # if it is a, b, or c, make it a number
            char = "2"
            realNum += char
        elif char == "d" or char == "e" or char == "f":
            char = "3"
            realNum += char
        elif char == "g" or char == "h" or char == "i":
            char = "4"
            realNum += char
        elif char == "j" or char == "k" or char == "l":
            char = "5"
            realNum += char
        elif char == "m" or char == "n" or char == "o":
            char = "6"
            realNum += char
        elif char == "p" or char == "q" or char == "r" or char =="s":
            char = "7"
            realNum += char
        elif char == "t" or char == "u" or char == "v":
            char = "8"
            realNum += char
        elif char == "w" or char == "x" or char == "y" or char =="z":
            char = "9"
            realNum += char
        else:
            realNum += char

    trueNumber = trueNumber.upper() # make sure all the letters in phone number are uppercase
    
    return(realNum,trueNumber)# return the number and its numeric equivalent


def showNumber(): # this displays the results
    realNum, trueNumber = getNumber() # get the number and convert it by calling the getNumber function
    print("Your alphanumeric number: " + trueNumber[0:3] + "-" + trueNumber[3:6] + "-" + trueNumber[6:10])

    print("Your numeric number: " + realNum[0:3] + "-" + realNum[3:6] + "-" + realNum[6:10])
    
        
showNumber() # run the program by calling the showNumber function
