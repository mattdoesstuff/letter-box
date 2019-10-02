class RootNode:
    children = []
    def __init__(self):
        print("created")
    def getChildren(self):
        return self.children
    def addChild(self, node):
        self.children.append(node)
    def isRoot(self):
        return True
