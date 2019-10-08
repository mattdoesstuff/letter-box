

class Gameboard():
    def __init__(self, board):
        self.gameboard = board
        self.unused = list(board)
        self.used = []
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
        remove = []
        tempUnused = []
        for c in word:
            if c in self.unused:
                self.used.append(c)
                remove.append(c)
        for c in self.unused:
            if c not in remove:
                tempUnused.append(c)
        self.unused = tempUnused


    def wordCount(self):
        return len(self.words)



    def fixUsed(self):
        """ Removes used characters from gameboard sections """
        tempUsed = []
        for word in self.words:
            for c in word:
                if c not in tempUsed:
                    tempUsed.append(c)
        self.unused = list(set(self.gameboard) - set(tempUsed))
        self.used = tempUsed

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
            used.append(prevLetter.upper())
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
                    return -1
            except(ValueError):
                return -1
        return efficiency
