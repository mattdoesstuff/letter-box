"""
Matt Prodani
10/7/2018
A recursive solver for the New York Times 'Letter Boxed' Game
Returns most 2 or 3 word solutions
"""


from Gameboard import Gameboard
from Dictionary import Dictionary
import copy

def updateValidWords(group, mostEfficient, currGameboard):
    """ Takes a list of words starting with a certain letter,
    the list to update, and a gameboard.
    Updates mostEfficient with the 'best' word to use for each ending letter on them
    next gameboard
    Only updates, does not return
    """
    for word in dict.getWords(group):

        efficiency = currGameboard.checkWord(word)
        if len(word) <= 3:
            continue

        if efficiency == -1: # Means word is not usable
            continue

        if word[-1] in mostEfficient.keys():
            if mostEfficient[word[-1]][0] < efficiency:
                mostEfficient[word[-1]] = [efficiency, word]
        else:
            mostEfficient[word[-1]] = [efficiency, word]


def findGameboards(currGameboard):
    # Stores the recursive returned valid gameboards
    gameboards = []
    # This list stores valid next words for each gameboard as {"last letter": "word"}
    # Only stores the most "efficient" word for each last letter
    mostEfficient = {}

    # Base Cases
    if currGameboard.isSolved():
        return [currGameboard]
    if len(currGameboard.getWords()) > 2:
        return [-1]


    # Goes through each word that starts with a valid letter if gameboard has no words,
    # otherwise only checks words starting with the correct letter
    if len(currGameboard.getWords()) == 0:
        for group in dict.getKeys():
            updateValidWords(group, mostEfficient, currGameboard)
    else:
        updateValidWords(currGameboard.getWords()[-1][-1], mostEfficient, currGameboard)


    # Creates new gameboard with each valid word and recursively calls itself
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

# Gets gameboard from user input and checks validity
while(True):
    board = input("ENTER THE CHARACTERS IN THE GAMEBOARD: ")
    if len(board) != 12:
        print("Gameboard needs to be 12 letters long")
        continue
    for c in board:
        if not c.isalpha():
            print("Gameboard has to consist of letters")
            continue
    break
mainBoard = Gameboard(board)
if input("Type 1 for the smaller dictionary, 2 for the bigger one: ") == 1:
    words = open("words.txt", "r")
else:
    words = open("words_alpha.txt", "r")


# Builds dictionary object and calls recursive algorithm
dict = Dictionary(words, mainBoard)
results = findGameboards(mainBoard)


# Prints solutions which are stored as a dictionary of solutions
# with solution word count as keys
# {"1": [["word1"], ["word2"]], }
solutions = {}
for res in results:
    solWords = res.getWords()
    if len(solWords) in solutions.keys():
        solutions[len(solWords)].append(solWords)
    else:
        solutions[len(solWords)] = [solWords]

for key in sorted(solutions.keys()):
    print(str(key) + " Word Solutions: ")
    for sol in solutions[key]:
        print(sol)
