from Gameboard import Gameboard
from Dictionary import Dictionary
gboard = Gameboard("NIUSRZMFXADE")
print(gboard.checkWord("NEUSFRUEN"))
thisDict = Dictionary(open("words.txt", "r"))
print(thisDict.getWords(7))
