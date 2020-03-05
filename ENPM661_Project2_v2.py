import numpy as np
import matplotlib.pyplot as plot
import copy
import math
import time

StartTime = time.time()

Workspace = [300,200]
GoalNode = [150,130]
StartNode = [5,5]
Obstaclesx = []
Obstaclesy = []
ExploredNodes = []
UnexploredNodes = []
CurrentNode = []
ParentNodeIndex = []
CurrentNodeIndex = 0
Path = []
NodePath = []
Cost = []
UnexploredNodesString =[]
plot.plot(Workspace[0],Workspace[1])
plot.plot(StartNode[0], StartNode[1], "Dg")
plot.plot(GoalNode[0], GoalNode[1], "Dg")
for x in range(300):
    for y in range(200):
        if((x-225)**2 + (y-150)**2 <= 25**2):
            Obstaclesx.append(x)
            Obstaclesy.append(y)
        if(((x-150)**2/40**2 + (y-100)**2/20**2) <= 1):
            Obstaclesx.append(x)
            Obstaclesy.append(y)
        if ((y-(0.6*x))>=(-125) and (y-(-0.6*x))<=(175) and (y-(0.6*x))<=(-95) and (y-(-0.6*x))>=(145)):
            Obstaclesx.append(x)
            Obstaclesy.append(y)
        if((y-(13*x))<=(-140) and (y-(1*x))>=(100) and y <= 185 and (y-(1.4*x)>=80) ):
            Obstaclesx.append(x)
            Obstaclesy.append(y)
        if ((y-(-1.2*x))>=(210) and (y-(1.2*x))>=(30) and (y-(-1.4*x))<=(290) and (y-(-2.6*x))>=280 and y<=185):
            Obstaclesx.append(x)
            Obstaclesy.append(y)
        if ((y - (1.73)*x + 135 >= 0) and (y + (0.58)*x - 96.35  <= 0) and (y - (1.73)*x - 15.54 <= 0) and (y + (0.58)*x - 84.81 >= 0)):
            Obstaclesx.append(x)
            Obstaclesy.append(y)

plot.scatter(Obstaclesx,Obstaclesy,color = 'r')

def InObstacleSpace(Node):
    x = Node[0]
    y = Node[1]
    if((x-225)**2 + (y-150)**2 <= 25**2):
        return False
    elif(((x-150)**2/40**2 + (y-100)**2/20**2) <= 1):
        return False
    elif ((y-(0.6*x))>=(-125) and (y-(-0.6*x))<=(175) and (y-(0.6*x))<=(-95) and (y-(-0.6*x))>=(145)):
        return False
    elif((y-(13*x))<=(-140) and (y-(1*x))>=(100) and y <= 185 and (y-(1.4*x)>=80) ):
        return False
    elif ((y-(-1.2*x))>=(210) and (y-(1.2*x))>=(30) and (y-(-1.4*x))<=(290) and (y-(-2.6*x))>=280 and y<=185):
        return False
    elif ((y - (1.73)*x + 135 >= 0) and (y + (0.58)*x - 96.35  <= 0) and (y - (1.73)*x - 15.54 <= 0) and (y + (0.58)*x - 84.81 >= 0)):
        return False
    else:
        return True

print(InObstacleSpace([22,120]))
def ActionMoveLeft(CurrentNode):
    if CurrentNode[0] > 0 and (InObstacleSpace(CurrentNode)):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0] = CurrentNode[0] - 1
        return NewNode
# print("Move Left",ActionMoveLeft(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveRight(CurrentNode):
    if CurrentNode[0] < Workspace[0] and (InObstacleSpace(CurrentNode)) :
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0]  = CurrentNode[0] + 1
        return NewNode
# print("Move Right",ActionMoveRight(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveUp(CurrentNode):
    if CurrentNode[1] < Workspace[1] and (InObstacleSpace(CurrentNode)) :
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[1]  = CurrentNode[1] + 1
        return NewNode
# print("Move Up",ActionMoveUp(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveDown(CurrentNode):
    if CurrentNode[1] > 0 and (InObstacleSpace(CurrentNode)) :
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[1]  = CurrentNode[1] - 1
        return NewNode
# print("Move Down",ActionMoveDown(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveUpLeft(CurrentNode):
    if (CurrentNode[0] > 0) and (CurrentNode[1] < Workspace[1]) and (InObstacleSpace(CurrentNode)):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1]  = CurrentNode[0] - 1 , CurrentNode[1]+1
        return NewNode
# print("Move UpLeft",ActionMoveUpLeft(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveUpRight(CurrentNode):
    if (CurrentNode[0] < Workspace[0]) and (CurrentNode[1] < Workspace[1]) and (InObstacleSpace(CurrentNode)):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1]= CurrentNode[0] + 1 , CurrentNode[1]+1
        return NewNode
# print("Move UpRight",ActionMoveUpRight(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveDownLeft(CurrentNode):
    if (CurrentNode[0] > 0) and (CurrentNode[1] > 0) and (InObstacleSpace(CurrentNode)):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1] = CurrentNode[0] - 1 , CurrentNode[1]-1
        return NewNode
# print("Move DownLeft",ActionMoveDownLeft(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveDownRight(CurrentNode):
    if (CurrentNode[0] < Workspace[0]) and (CurrentNode[1] > 0) and (InObstacleSpace(CurrentNode)):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1] = CurrentNode[0] + 1 , CurrentNode[1]-1
        return NewNode
# print("Move DownRight",ActionMoveDownRight(CurrentNode))
# print("CurrentNode",CurrentNode)
#Function to check if a node is new and add it to the list
def AddNode(NewNode):
    global CurrentNodeIndex
    global CurrentNode
    # Node = ','.join(str(e) for e in NewNode)
    # print("Node",Node)
    if not (NewNode in UnexploredNodes):
    # if not (Node in UnexploredNodesString):
        UnexploredNodes.append(NewNode)
        # UnexploredNodesString.append(Node)
        ParentNodeIndex.append(CurrentNodeIndex)

def GeneratePath(CurrentNode):
    global CurrentNodeIndex
    Path.append(CurrentNodeIndex)
    while(Path[0] != 0):
        Path.insert(0,ParentNodeIndex[UnexploredNodes.index(CurrentNode)])
        CurrentNode = UnexploredNodes[Path[0]]

    for i in range(len(Path)):
        NodePath.append(UnexploredNodes[Path[i]])
def Dijkstra(InitialNode):
    global StartNode
    global GoalNode
    global CurrentNode
    global CurrentNodeIndex
    CurrentNode = copy.deepcopy(InitialNode)
    Node = ','.join(str(e) for e in CurrentNode)
    # print("CUUUU",CurrentNode)
    UnexploredNodes.append(CurrentNode)
    UnexploredNodesString.append(Node)
    ParentNodeIndex.append(CurrentNodeIndex)
    Cost.append(0)
    while((CurrentNode[0] != GoalNode[0]) or (CurrentNode[1] != GoalNode[1])):
        if(ActionMoveLeft(CurrentNode) is not None):
            AddNode(ActionMoveLeft(CurrentNode))
            # UnexploredNodes.append(ActionMoveLeft(CurrentNode))
        if(ActionMoveRight(CurrentNode) is not None):
            AddNode(ActionMoveRight(CurrentNode))
            # UnexploredNodes.append(ActionMoveRight(CurrentNode))
        if(ActionMoveUp(CurrentNode) is not None):
            AddNode(ActionMoveUp(CurrentNode))
            # UnexploredNodes.append(ActionMoveUp(CurrentNode))
        if(ActionMoveDown(CurrentNode) is not None):
            AddNode(ActionMoveDown(CurrentNode))
            # UnexploredNodes.append(ActionMoveDown(CurrentNode))
        if(ActionMoveUpLeft(CurrentNode) is not None):
            AddNode(ActionMoveUpLeft(CurrentNode))
            # UnexploredNodes.append(ActionMoveUpLeft(CurrentNode))
        if(ActionMoveUpRight(CurrentNode) is not None):
            AddNode(ActionMoveUpRight(CurrentNode))
            # UnexploredNodes.append(ActionMoveUpRight(CurrentNode))
        if(ActionMoveDownLeft(CurrentNode) is not None):
            AddNode(ActionMoveDownLeft(CurrentNode))
            # UnexploredNodes.append(ActionMoveDownLeft(CurrentNode))
        if(ActionMoveDownRight(CurrentNode) is not None):
            AddNode(ActionMoveDownRight(CurrentNode))
            # UnexploredNodes.append(ActionMoveDownRight(CurrentNode))
        # ExploredNodes.append(CurrentNode)
        # print(CurrentNode)
        CurrentNodeIndex += 1
        CurrentNode = UnexploredNodes[CurrentNodeIndex]

    return CurrentNode

print("Solving")
CurrentNode = Dijkstra(StartNode)
GeneratePath(CurrentNode)
EndTime = time.time()
print(Path)
print(NodePath)
print("Solved" , EndTime - StartTime)
NodePathX = [x[0] for x in NodePath]
NodePathY = [x[1] for x in NodePath]
print("X",NodePathX)
print("Y",NodePathY)
plot.plot(NodePathX,NodePathY)
plot.show()
