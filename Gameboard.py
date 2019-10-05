

class Gameboard():
    def __init__(self, board):
        self.gameboard = board
        self.unused = list(board)
        self.used = []
        self.words = []


    def getGameboardLength():
        return len(this.gameboard)


#   Adds a word to gameboard and fixes corresponding arrays
    def addWord(word):
        self.words.append(word)
        remove = []
        tempUnused = []
        for c in word:
            if c in this.unused:
                this.used.append(c)
                remove.append(c)
        for c in this.unused:
            if c not in remove:
                tempUnused.append(c)
        this.unused = tempUnused

    def checkAgainstDict(dict):




    def fixUsed(self):
        """ Removes used characters from gameboard sections """
        tempUnused = []
        # for c in self.used:
        #     tempUnused.append(c)
        # for c in self.unused:
        #     if c not in tempUnused:
        #         tempUnused.append(c)
        # self.unused = tempUnused

# TODO Add Different Goals
    def checkWord(self, word):
        """ Checks if a given word is valid and returns efficiency, also updates respective gameboard properties.
        Will return -1 if a word is not valid.
        """
        # Edge Cases
        if len(word) <= 1:
            return -1

        efficiency = 0
        prevLetter = word[0].upper()

        used = self.used
        unused = self.unused

        if prevLetter not in used:
            used.append(prevLetter)
            efficiency += 1
        for i in range(1, len(word)):
            currLetter = word[i].upper()
            try:
                if (self.gameboard.index(prevLetter)) // 3 != (self.gameboard.index(currLetter)) // 3:
                    if currLetter not in used:
                        used.append(currLetter)
                        efficiency += 1
                    prevLetter = currLetter
                else:
                    print(currLetter + prevLetter)
                    print(self.gameboard.index(currLetter))
                    return -1
            except(ValueError):
                return -1
        return efficiency
