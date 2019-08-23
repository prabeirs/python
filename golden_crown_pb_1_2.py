#!/usr/bin/python

vKingdom = {
           'Land'  : {'p' : 1, 'a' : 2, 'n' : 1, 'd' : 1},
           'Water' : {'o' : 2, 'c' : 1, 't' : 1, 'p' : 1, 'u' : 1, 's' : 1},
           'Ice'   : {'m': 3, 'a' : 1, 'o' : 1, 't' : 1, 'h' : 1},
           'Air'   : {'o' : 1, 'w' : 1, 'l' : 1},
           'Fire'  : {'d' : 1, 'r' : 1, 'a' : 1, 'g' : 1, 'o' : 1, 'n' : 1},
          }

vInput = []

def main():
    prevAllies = ""
    while True:
        text = raw_input("a) Who is the ruler of Southeros?, b) Allies of Ruler?, c) Allies of King Shan?, d)<Kingdom_name>,<\"some_message_to_kingdom\">, e) q to quit: ")

        if text == 'q':
            break
        elif text == "Who is the ruler of Southeros?" or text == "a":
            showRuler()
        elif text == "Allies of Ruler?" or text == "b":
            if (prevAllies):
                print(prevAllies)
                prevAllies = ""
            else:
                showAlliesOfRuler()
        elif text == "Allies of King Shan?" or text == "c":
            if (prevAllies):
                print(prevAllies)
                prevAllies = ""
            else:
                showAlliesOfRuler()
        elif text == "d":
            continue
        else:
            if (checkInput(text)):
                populateInput(text)

def showRuler():
    if (numInput()):
        print("King Shan")
        prevAllies = getAllies()
        print(">>>> " + prevAllies)
    else:
        print("None")

def showAlliesOfRuler():
    if (numInput()):
        #print the allies
        #prevAllies = getAllies()
        #print(prevAllies)
        print(getAllies())
        flushInput()
    #elif (prevAllies != ""):
    #    print(prevAllies)
    #    prevAllies = ""
    else:
        print("None")

def checkInput(inputStr):
    if ',' in inputStr:
        vCharInMsgCnt = {}
        (kingdom, message) = inputStr.split(",", 1)
        print("Kingdom = {} and message = {}".format(kingdom, message))
        if kingdom in vKingdom:
            print("Kingdom " + kingdom + " found in list of kingdoms. Message code of this kingdom is "),
            vMsgCode = vKingdom[kingdom]
            print(str(vMsgCode))
            print("Checking message string character by character...")
            for char in message:
                if char.isupper():
                    char = char.lower()
                if char in vMsgCode:
                    print("Character \"" + char + "\" found in message string "),
                    if char in vCharInMsgCnt:
                        vCharInMsgCnt[char] = vCharInMsgCnt[char] + 1
                    else:
                        vCharInMsgCnt[char] = 0 + 1

                    print("{} times.".format(vCharInMsgCnt[char]))

            print("Finding occurrences of required characters in message string...")
            for char in vMsgCode:
                if char in vCharInMsgCnt:
                    if vCharInMsgCnt[char] >= vMsgCode[char]:
                        print("{} occured {} times, it's least expected occurence is {}.".format(char, vCharInMsgCnt[char], vMsgCode[char]))
                    else:
                        return(0)
                else:
                    return(0)
    else:
        return(0)

    return(1)

def populateInput(message):
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
    del vInput[:]
    
if __name__ == "__main__":
    main()
