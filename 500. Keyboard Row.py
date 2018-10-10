"""
Given a List of words, return the words that can be typed using letters
of alphabet on only one row's of American keyboard like the image below.
"""

#Keyboard:
    #Q W E R T Y U I O P
    #A S D F G H J K L
    #Z X C V B N M

def findWords(words: "list of str"):
    top = {"Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"}
    middle = {"A", "S", "D", "F", "G", "H", "J", "K", "L"}
    bottom = {"Z", "X", "C", "V", "B", "N", "M"}

    foundWords = []
    
    for word in words:
        inTop = 1
        inMid = 1
        inBot = 1
        for char in word.upper():
            if char not in top:
                inTop = 0
            if char not in middle:
                inMid = 0
            if char not in bottom:
                inBot = 0
        if inTop == 1 or inMid == 1 or inBot == 1:
            foundWords.append(word)
    return foundWords
