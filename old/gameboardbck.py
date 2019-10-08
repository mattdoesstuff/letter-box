

class Gameboard():
    def __init__(self, board):
        self.gameboard = board
        self.unused = set(board)
        self.used = set()
        self.words = []

        # FOR # DEBUG:
    def getUsed(self):
        return self.used
    def getUnused(self):
        return self.unused
        # END FOR DEBUG




    def getWords(self):
        return self.words

    def getGameboardLength(self):
        return len(self.gameboard)


    def isSolved(self):
        if len(self.unused) == 0:
            return True
        return False

    def addWord(self, word):
        ''' Adds a word to gameboard and fixes corresponding arrays '''
        self.words.append(word)
        self.used.update(word)
        self.unused = set(self.gameboard) - self.used





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

        if len(self.words) > 0:
            if self.words[-1][-1] != prevLetter.upper():
                return -1

        used = self.used
        unused = self.unused

        if prevLetter not in used:
            used.update(prevLetter.upper())
            efficiency += 1
        for i in range(1, len(word)):
            currLetter = word[i].upper()
            try:
                if (self.gameboard.index(prevLetter)) // 3 != (self.gameboard.index(currLetter)) // 3:
                    if currLetter not in used:
                        used.update(currLetter)
                        efficiency += 1
                    prevLetter = currLetter
                else:
                    return -1
            except(ValueError):
                return -1
        return efficiency
