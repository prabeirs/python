#!/usr/bin/python
import os

vKingdom = {
       'Land'  : {'p' : 1, 'a' : 2, 'n' : 1, 'd' : 1},
       'Water' : {'o' : 2, 'c' : 1, 't' : 1, 'p' : 1, 'u' : 1, 's' : 1},
       'Ice'   : {'m': 3, 'a' : 1, 'o' : 1, 't' : 1, 'h' : 1},
       'Air'   : {'o' : 1, 'w' : 1, 'l' : 1},
       'Fire'  : {'d' : 1, 'r' : 1, 'a' : 1, 'g' : 1, 'o' : 1, 'n' : 1},
      }

vInput = []
debug = 0

def main():
    global debug
    debug = os.getenv('DEBUG', 0)
    if (int(debug) == 1):
        debug = 1
    else:
        debug = 0
    print("************* The Golden Crown ***************")
    print("                   USAGE                      ")
    print("**********************************************")
    print("Type either a, b, c, d or q as input and press Enter. Alternatively you can also type in and provide the input as shown below.")
    print("Instead of a, b and c type in the sentences as seen in the bottom most menu corresponding to each one of them.")
    print("For d it has to be always provided in this format Kingdom_name,\"secret_message_to_kingdom\". Quotes are optional. Can send messages more than once too.")
    print("Once either b or c is opted or supplied as input the current ongoing game is over and continues with a new one from the start. Echoes an \"It's Over.\" message.")
    print("The kingdom names are :- Land, Water, Ice, Air and Fire. The kingdom name and the secret message has to be always separated by a comma.")
    print("                    MENU                      ")
    print("**********************************************")
    print("a) Who is the ruler of Southeros?, b) Allies of Ruler?, c) Allies of King Shan?, d)<Kingdom_name>,<\"secret_message_to_kingdom\">, e) q to quit\n")
    while True:
        try:
            text = raw_input("")
        except EOFError:
            print("ERROR: EOF or empty input!")
            text = ""

        if text == 'q':
            break
        elif text == "Who is the ruler of Southeros?" or text == "a":
            showRuler()
        elif text == "Allies of Ruler?" or text == "b":
            showAlliesOfRuler()
        elif text == "Allies of King Shan?" or text == "c":
            showAlliesOfRuler()
        elif text == "d":
            continue
        else:
            if (checkInput(text)):
                populateInput(text)

def showRuler():
    if (numInput()):
        print("King Shan")
    else:
        print("None")

def showAlliesOfRuler():
    if (numInput()):
        print(getAllies())
        flushInput()
    else:
        print("None")

def checkInput(inputStr):
    if ',' in inputStr:
        vCharInMsgCnt = {}
        (kingdom, message) = inputStr.split(",", 1)
        kingdom = kingdom.lstrip()
        kingdom = kingdom.rstrip()
        if debug:
            print("Kingdom = {} and message = {}".format(kingdom, message))
        if kingdom in vKingdom:
            if debug:
                print("Kingdom " + kingdom + " found in list of kingdoms. Message code of this kingdom is "),
            vMsgCode = vKingdom[kingdom]
            if debug:
                print(str(vMsgCode))
                print("Checking message letter by letter ...")
            for char in message:
                if char.isupper():
                    char = char.lower()
                if char in vMsgCode:
                    if debug:
                        print("Letter \"" + char + "\" found in message "),
                    if char in vCharInMsgCnt:
                        vCharInMsgCnt[char] = vCharInMsgCnt[char] + 1
                        if debug:
                            print("{} times.".format(vCharInMsgCnt[char]))
                    else:
                        vCharInMsgCnt[char] = 0 + 1
                        if debug:
                            print("{} times.".format(vCharInMsgCnt[char]))

        else:
            if debug:
                print("Kingdom not found or invalid!")
            return(0)

        for char in vMsgCode:
            if char in vCharInMsgCnt:
                if vCharInMsgCnt[char] >= vMsgCode[char]:
                   if debug:
                      print("{} occurred {} times, it's least expected occurrence is {}.".format(char, vCharInMsgCnt[char], vMsgCode[char]))
                else:
                    return(0)
            else:
               return(0)
    else:
        return(0)

    return(1)

def populateInput(message):
    ## Global
    global vInput
    vInput.append(message)

def numInput():
    if (len(vInput) >= 3):
        return(1)
    else:
        return(0)

def getAllies():
    str = ""
    for line in vInput:
        (kingdom, msg) = line.split(",", 1)
        str = str + kingdom + " ,"

    return(str.rstrip(','))

def flushInput():
    ## Global
    global vInput
    del vInput[:]
    print("It's Over.")
    
if __name__ == "__main__":
    main()
