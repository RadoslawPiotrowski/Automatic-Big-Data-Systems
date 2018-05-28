
class Node():
    def __init__(self, nodeName, neighborList):

        self.name = nodeName
        self.neighbors = neighborList
        self.visited = False

    def getName(self):
        return self.name

    def getNeighbors(self):
        return self.neighbors

    def getVisited(self):
        return self.visited

    def setVisited(self):
        self.visited = True
