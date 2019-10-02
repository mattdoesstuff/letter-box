from rootNode import RootNode
from Node import Node
gameboard = ['']

# wordList = ['andrew', 'and', 'band', 'ben', 'curse', 'clash']
wordList = []
wordGroups = {}
unusedLetters = ['e','g','w','o','k','i','p','l','s','a','d','c']
usedLetters = []
gameboard = ['e','g','w','o','k','i','p','l','s','a','d','c']
unusedLetters = gameboard
rootNode = RootNode()
f = open('unsortedDict.txt', 'r')
for line in f:
    wordList.append(line.strip())
nodes = []
maxEfficiency = 0
wordsUsed = []
def populateGroups():
    for word in wordList:
        if len(word) in wordGroups.keys():
            wordGroups[len(word)].append(word)
        else:
            wordGroups[len(word)] = [word]

# def canConnect(c1, c2):


# Takes in a word, unused letters, used letters
def checkWord(w, unused, used):
    prevLetter = w[0]
    efficiency = 0

    for i in range(1, len(w)):
        # print (unused)
        currLetter = w[i]
        if currLetter in gameboard and prevLetter in gameboard:
            if gameboard.index(currLetter)//3 == gameboard.index(prevLetter) // 3:
                print('e' in gameboard)
                return -1
            if currLetter in unused:
                unused.remove(currLetter)
                used.append(currLetter)
                efficiency += 1
        else:
            return -1

    return efficiency

# The char '#' means no bound
def populateTree(firstChar = "#"):

    rootNode = RootNode()
    keys = list(wordGroups.keys())
    keys.sort(reverse = True)

    unused = unusedLetters
    usable = usedLetters
    maxEfficiency = 0
    mostEfficient = []
    for key in keys:
        if key < maxEfficiency:
            continue
        group = wordGroups[key]
        maxEfficiency, mostEfficient = makeNodes(firstChar, group, maxEfficiency, unused[:], usable[:])


    # print(maxEfficiency)

    return mostEfficient



def makeNodes(firstChar, group, maxEfficiency, unused, used):
    mostEfficient = []
    for word in group:

        if firstChar != '#':
            if word[0] != firstChar:
                continue
        efficiency = 0
        currUnused = unused
        currUsed = used
        # print(word)
        efficiency = checkWord(word, currUnused[:], currUsed[:])
        # print(efficiency)
        if efficiency < maxEfficiency:
            continue
        else:
            # print("called")
            # Move these two lines to allow multiple solutions
            currNode = createNodes(rootNode, word)
            currNode.setEfficiency(efficiency)
        if efficiency == maxEfficiency:
            mostEfficient.append(currNode)
            # print(getWord(currNode))
        else:
            mostEfficient = [currNode]
    return (maxEfficiency, mostEfficient)

def createNodes(currNode, word):
    for c in range(len(word)):
        nextNode = None
        for node in currNode.getChildren():
            if node.getLetter == word[c]:
                nextNode = node
                break
        if nextNode == None:
            nextNode = Node(word[c], currNode)
        currNode.addChild(nextNode)
        currNode = nextNode
        currNode.makeTerminal()
        # print(word)
        return currNode

def getWord(lastNode):
    word = ''
    curr = lastNode
    while(True):
        if curr.isRoot():
            break
        word += curr.getLetter()
        curr = curr.getParent()
    return word
populateGroups()
mostEfficientWords = populateTree()
for word in mostEfficientWords:
    print(getWord(word)[::-1])
# print(getWord(mostEfficient[0]))
