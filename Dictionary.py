class Dictionary():
    def __init__(self, dictionary):
        """ Builds a dictionary object containing a list of words as well as groups them into a Dictionary
        separated by starting letter
        """
        wordList = []
        self.wordGroups = {}
        # Converts text file to list
        # Populates a dictionary with word groups based on length
        # dictionary = ["alcove", "equalizing", "equivocal", "clove", "anglicize", "convene", "cozenage", "lazing", "laicizing", "legalizing", "novocaine"]
        for line in dictionary:
            word = line.strip().upper()
            if word[0] in self.wordGroups.keys():
                self.wordGroups[word[0]].append(word)
            else:
                self.wordGroups[word[0]] = [word]

    def __init__(self, dictionary, gameboard):
        """ Builds a dictionary object containing a list of words as well as groups them into a Dictionary
        separated by starting letter, where starting letters are in gameboard if provided
        """
        wordList = []
        self.wordGroups = {}
        # Converts text file to list
        # Populates a dictionary with word groups based on length
        # dictionary = ["alcove", "equalizing", "equivocal", "clove", "anglicize", "convene", "cozenage", "lazing", "laicizing", "legalizing", "novocaine"]
        for line in dictionary:
            word = line.strip().upper()
            if word[0] in gameboard.getGameboard():
                if word[0] in self.wordGroups.keys():
                    self.wordGroups[word[0]].append(word)
                else:
                    self.wordGroups[word[0]] = [word]

    def getKeys(self):
        """ Returns a list of valid keys corresponding to groups by starting letter """
        return sorted(list(self.wordGroups.keys()), reverse = True)
    def getWords(self, key):
        """ Gets words from dictionary starting with a given letter """
        return self.wordGroups[key]
