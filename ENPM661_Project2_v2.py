import numpy as np
import matplotlib.pyplot as plot
import copy
import math
import time
#Blank Map Ma
# trix
# BlankMap = np.zeros((200,300))
#
# theta = math.radians(30)
# #Fucntion to find equation of line between two points:
# def FindLineEqn(x1,y1,x2,y2):
#     slope = (y2-y1)/(x2-x1)
#     c = y1-slope*x1
#     return slope,c
# print(FindLineEqn(75,85,50,150))
#
# # Rotz = np.asarray([math.cos(theta), -math.sin(theta) , 0] ,[ math.sin(theta), math.cos(theta), 0 ], [ 0 , 0 , 1])
# # xyz = np.asarray([a],[b],[c])
# #Fucntion to select and store map
#
# def GenerateMap(name):
#     Map = copy.deepcopy(BlankMap)
#     if(name == "Trial"):
#         for x in range(200):
#             for y in range(100):
#                 if((x>=90 and x<=110) and (y>=40 and y<=60)):
#                     Map[100-y][x] = 1
#                 if((((x-160)**2 + (y-50)**2) < 15**2)):
#                     Map[100-y][x] = 1
#         return Map
#
#     if(name == 'Map'):
#         for x in range(300):
#             for y in range(200):
#                 if((x-225)**2 + (y-150)**2 <= 25**2):
#                     Map[200-y][x] = 1
#                 if(((x-150)**2/40**2 + (y-100)**2/20**2) <= 1):
#                     Map[200-y][x] = 1
#                 if ((y-(0.6*x))>=(-125) and (y-(-0.6*x))<=(175) and (y-(0.6*x))<=(-95) and (y-(-0.6*x))>=(145)):
#                     Map[200-y][x] = 1
#                 if((y-(13*x))<=(-140) and (y-(1*x))>=(100) and y <= 185 and (y-(1.4*x)>=80) ):
#                     Map[200-y][x] = 1
#                 if ((y-(-1.2*x))>=(210) and (y-(1.2*x))>=(30) and (y-(-1.4*x))<=(290) and (y-(-2.6*x))>=280 and y<=185):
#                   Map[200-y][x] = 1
#                 # Map[200-10][225] = 3
#                 # if ((y-(-1.2*x))>=(210)):
#                 #     Map[199-y][x] = 1
#                 # if (y-(0.6*x))>=(-125):
#                 #     Map[199-y][x] = 1
#                 # if (y-(-0.6*x))>=(175):
#                 #     Map[199-y][x] = 1
#         return Map
#                 # if((((x-160)**2 + (y-50)**2) < 15**2)):
#                 #     BlankMap[100-y][x] = 1
#
# plot.matshow(GenerateMap("Map"))
# plot.show()

Workspace = [300,200]
GoalNode = [190,50]
StartNode = [50,50]
ExploredNodes = []
UnexploredNodes = []
CurrentNode = [0,0]
ParentNodeIndex = []
CurrentNodeIndex = 0
Path = []
NodePath = []
Cost = []
UnexploredNodesString =[]
def ActionMoveLeft(CurrentNode):
    # print("CURRLEFT",CurrentNode)
    if CurrentNode[0] > 0:
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0] = CurrentNode[0] - 1
        return NewNode
# print("Move Left",ActionMoveLeft(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveRight(CurrentNode):
    if CurrentNode[0] < Workspace[0] :
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0]  = CurrentNode[0] + 1
        return NewNode
# print("Move Right",ActionMoveRight(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveUp(CurrentNode):
    if CurrentNode[1] < Workspace[1] :
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[1]  = CurrentNode[1] + 1
        return NewNode
# print("Move Up",ActionMoveUp(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveDown(CurrentNode):
    if CurrentNode[1] > 0 :
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[1]  = CurrentNode[1] - 1
        return NewNode
# print("Move Down",ActionMoveDown(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveUpLeft(CurrentNode):
    if (CurrentNode[0] > 0) and (CurrentNode[1] < Workspace[1]):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1]  = CurrentNode[0] - 1 , CurrentNode[1]+1
        return NewNode
# print("Move UpLeft",ActionMoveUpLeft(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveUpRight(CurrentNode):
    if (CurrentNode[0] < Workspace[0]) and (CurrentNode[1] < Workspace[1]):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1]= CurrentNode[0] + 1 , CurrentNode[1]+1
        return NewNode
# print("Move UpRight",ActionMoveUpRight(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveDownLeft(CurrentNode):
    if (CurrentNode[0] > 0) and (CurrentNode[1] > 0):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1] = CurrentNode[0] - 1 , CurrentNode[1]-1
        return NewNode
# print("Move DownLeft",ActionMoveDownLeft(CurrentNode))
# print("CurrentNode",CurrentNode)

def ActionMoveDownRight(CurrentNode):
    if (CurrentNode[0] < Workspace[0]) and (CurrentNode[1] > 0):
        NewNode = copy.deepcopy(CurrentNode)
        NewNode[0],NewNode[1] = CurrentNode[0] + 1 , CurrentNode[1]-1
        return NewNode
# print("Move DownRight",ActionMoveDownRight(CurrentNode))
# print("CurrentNode",CurrentNode)
#Function to check if a node is new and add it to the list
def AddNode(NewNode):
    global CurrentNodeIndex
    global CurrentNode
    Node = ','.join(str(e) for e in NewNode)
    # print("Node",Node)
    # if not (NewNode in UnexploredNodes):
    if not (Node in UnexploredNodesString):
        UnexploredNodes.append(NewNode)
        UnexploredNodesString.append(Node)
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
        # global CurrentNodeIndex
        # global CurrentNode

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
StartTime = time.time()
CurrentNode = Dijkstra(StartNode)
GeneratePath(CurrentNode)
EndTime = time.time()
print(Path)
print(NodePath)
print("Solved" , EndTime - StartTime)





