from Node import Node
import math
from enum import Enum

class NodesEnum(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6

def createTree():
    nodes = []
    nodeA = Node("A", {'C': 1, 'D': 2})
    nodes.append(nodeA)
    nodeB = Node("B", {'C': 2, 'F': 3})
    nodes.append(nodeB)
    nodeC = Node("C", {'A': 1, 'B': 2, 'D': 1, 'E': 3})
    nodes.append(nodeC)
    nodeD = Node("D", {'A': 2, 'C': 1, 'G': 1})
    nodes.append(nodeD)
    nodeE = Node("E", {'C': 3, 'F': 2})
    nodes.append(nodeE)
    nodeF = Node("F", {'B': 3, 'E': 2, 'G': 1})
    nodes.append(nodeF)
    nodeG = Node("G", {'F': 1, 'D': 1})
    nodes.append(nodeG)

    return nodes

def createDArray(startNode):
    deltaArray = []
    for i in range(7):
        deltaArray.append(math.inf)
    deltaArray[startNode] = 0
    return deltaArray

def ifContinue(Q):
    haveToContinue = False
    for node in Q:
        if node.getVisited() == False:
            haveToContinue = True
    return haveToContinue

def findLowestDistanceNodeIndex(distanceArray, listOfNodeObjects):
    lowestValueIndex = 0
    lowestValue = 10
    for index, distance in enumerate(distanceArray):
        if distance <= lowestValue and listOfNodeObjects[index].getVisited() == False:
            lowestValueIndex = index
            lowestValue = distance
    return lowestValueIndex

def dijkstra(listOfNodeObjects, distanceArray, previousNode, endPoint):
    print("START OF DIJKSTRA")
    while(ifContinue(listOfNodeObjects)):
        lowestDistanceIdxNumber = findLowestDistanceNodeIndex(distanceArray, listOfNodeObjects)
        analyzingNode = listOfNodeObjects[lowestDistanceIdxNumber]
        analyzingNode.setVisited()
        for key in analyzingNode.getNeighbors():
            idxOfNode = NodesEnum[key].value
            if(listOfNodeObjects[idxOfNode].getVisited() == False):
                actualDistToNode = distanceArray[lowestDistanceIdxNumber] + getLenghtBetweenNodes(analyzingNode, key)
                if actualDistToNode < distanceArray[idxOfNode]:
                    distanceArray[idxOfNode] = actualDistToNode
                    previousNode[idxOfNode] = analyzingNode.getName()
        print(distanceArray)
        print (previousNode)
    print("END OF DIJKSTRA")
    print("PRINTING ROUTE TO NODE")
    print(getRouteToEndNode(distanceArray, previousNode, endPoint)[::-1])
    print("END OF THE PROGRAM")

def getRouteToEndNode(distanceArray, previousNode, endPoint):
    route = []
    route.append(NodesEnum(endPoint).name)
    while(previousNode[NodesEnum[route[-1]].value] != None):
        actualNode = NodesEnum[route[-1]].value
        route.append(previousNode[actualNode])
    return route



def getLenghtBetweenNodes(firstNode, secondNodeLenght):
    return firstNode.getNeighbors().get(secondNodeLenght)

if __name__ == '__main__':
    nodesList = createTree()
    startNode = 'F'
    finishNode = 'A'
    distanceArray = createDArray(NodesEnum[startNode].value)
    previousArray = [None] * 7
    dijkstra(nodesList, distanceArray, previousArray,NodesEnum[finishNode].value)


