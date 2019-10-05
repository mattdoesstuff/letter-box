class Dictionary():
    def __init__(this, dictionary):
        """ Builds a dictionary object containing a list of words as well as groups them into a Dictionary
        separated by word length
        """
        wordList = []
        this.wordGroups = {}
        # Converts text file to list
        for line in dictionary:
            wordList.append(line.strip())
        # Populates a dictionary with word groups based on length
        for word in wordList:
            if len(word) in this.wordGroups.keys():
                this.wordGroups[len(word)].append(word)
            else:
                this.wordGroups[len(word)] = [word]
    def getKeys(this):
        """ Returns a list of valid keys corresponding to groups by word length """
        return sorted(list(this.wordGroups.keys()), reverse = True)
    def getWords(this, key):
        """ Gets words from dictionary with a given length """
        return this.wordGroups[key]
    
