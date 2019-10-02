from rootNode import RootNode
from Node import Node
# Gameboard consists of 12 chars where each 3 chars make one edge
gameboard = ['e','g','w','o','k','i','p','l','s','a','d','c']

wordList = []
wordGroups = {}

# Loads dictionary
f = open('unsortedDict.txt', 'r')
for line in f:
    wordList.append(line.strip())

nodes = []

def populateGroups():
    for word in wordList:
        if len(word) in wordGroups.keys():
            wordGroups[len(word)].append(word)
        else:
            wordGroups[len(word)] = [word]

def checkWord(word, unusedLetters, usedLetters):
    prevChar = word[0]
    efficiency = 0
    if prevChar in unusedLetters:
        efficiency += 1
        unusedLetters.remove(prevChar)
        usedLetters.append(prevChar)
    elif word[0] not in usedLetters:
        return -1
    for i in range(1, len(word)):
        currChar = word[i]
        if gameboard.indexOf(prevChar) // 3 == gameboard.indexOf(currChar) // 3:
            return -1
        if currChar in unusedLetters:
            efficiency += 1
            unusedLetters.remove(currChar)
            usedLetters.append(currChar)
        elif currChar not in usedLetters:
            return -1
        prevChar = currChar
