from Gameboard import gameboard
from Dictionary import dictionary
from Node import RootNode, Node


dict = Dictionary(open("words.txt"), "r")


populateTree(boardvals):
    rootNode = rootNode()
    gameboard = Gameboard(boardvals)


    for word in currWords:
        currGameboard = gameboard.deepCopy()

findGameboard(currGameboard):
    for group in dict.getKeys():
        maxEfficiency = 0

        
        for word in dict.getWords(group):
            efficiency = gameboard.checkWord(word)
            if efficiency == -1:
                continue
            elif efficiency > maxEfficiency:
                currWords = [word]
            elif efficiency == maxEfficiency:
                currWords.append(word)
