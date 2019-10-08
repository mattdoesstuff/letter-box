class Gameboard():

    """
    This object contains a letter boxed gameboard.
    Attributes:
        Unused letters
        Used letters
        Words Used
        String literal for the gameboard itself


    """
    def __init__(self, board):
        """ Constructs a gameboard object given the characters as a string """
        self.gameboard = board
        self.unused = set(board)
        self.used = set()
        self.words = []


    def getGameboard(self):
        return self.gameboard

    def getWords(self):
        return self.words

    def isSolved(self):
        """ Returns True if Gameboard is complete, false otherwise """
        if len(self.unused) == 0:
            return True
        return False

    def addWord(self, word):
        """ Adds a word to gameboard """
        self.words.append(word)
        self.used.update(word)
        self.unused = set(self.gameboard) - self.used


    def checkWord(self, word):
        """ Checks if a given word is valid and returns the number of unused letters it fills up.
        Will return -1 if a word is not valid.
        """
        # Edge Cases
        if len(word) <= 1:
            return -1

        efficiency = 0
        prevLetter = word[0].upper()

        # Checks if last letter of last word matches next
        if len(self.words) > 0:
            if self.words[-1][-1] != prevLetter.upper():
                return -1

        used = set(self.used)
        unused = set(self.unused)

        if prevLetter not in used:
            used.update(prevLetter.upper())
            efficiency += 1

        # Loops through each letter in word and compares to previous letter
        # Starts from 2nd character to accomodate for checking word compatibility
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
                # Will be called if a letter is not in gameboard
                return -1
        return efficiency
