from Gameboard import Gameboard
from Dictionary import Dictionary
from Node import RootNode, Node
import copy

dict = Dictionary(open("words.txt", "r"))

def getValidWords(group, mostEfficient):
    for word in dict.getWords(group):
        efficiency = currGameboard.checkWord(word)

        if len(word) <= 3:
            continue

        if efficiency == -1:
            continue
        if word[-1] in mostEfficient.keys():
            if mostEfficient[word[-1]][0] < efficiency:
                mostEfficient[word[-1]] = [efficiency, word]
        else:
            mostEfficient[word[-1]] = [efficiency, word]


def findGameboards(currGameboard):
    gameboards = []
    # if len(currGameboard.getWords()) == 1:
        # print("CALLED")
    vals = []
    mostEfficient = {}


    if currGameboard.isSolved():
        return [currGameboard]
    if len(currGameboard.getWords()) > 2:
        return [-1]

    if len(currGameboard.getWords() == 0):
        for group in dict.getKeys():
            updateValidWords(group, mostEfficient)
    else:
        updateValidWords(currGameboard.getWords()[-1][-1], gameboard)


    for key in mostEfficient:
        gboard = copy.deepcopy(currGameboard)
        gboard.addWord(mostEfficient[key][1])
        nextBoards = findGameboards(gboard)
        for board in nextBoards:
            if isinstance(board, Gameboard):
                if board.isSolved():
                    gameboards.append(board)
    return gameboards


print("LETTER BOXED SOLVER")
mainBoard = Gameboard(input("ENTER THE CHARACTERS IN THE GAMEBOARD: "))


# mainBoard = Gameboard("GIOZLNUCEAVQ")
solutions = findGameboards(mainBoard)
for sol in solutions:
    print(sol.getWords())
