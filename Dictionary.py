class Dictionary():
    def __init__(self, dictionary):
        """ Builds a dictionary object containing a list of words as well as groups them into a Dictionary
        separated by word length
        """
        wordList = []
        self.wordGroups = {}
        # Converts text file to list
        # Populates a dictionary with word groups based on length
        # dictionary = ["alcove", "equalizing", "equivocal", "clove", "anglicize", "convene", "cozenage", "lazing", "laicizing", "legalizing", "novocaine"]
        for line in dictionary:
            word = line.strip().upper()
            if len(word) in self.wordGroups.keys():
                self.wordGroups[len(word)].append(word)
            else:
                self.wordGroups[len(word)] = [word]
    def getKeys(self):
        """ Returns a list of valid keys corresponding to groups by word length """
        return sorted(list(self.wordGroups.keys()), reverse = True)
    def getWords(self, key):
        """ Gets words from dictionary with a given length """
        return self.wordGroups[key]
