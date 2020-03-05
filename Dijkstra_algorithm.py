import numpy as np
import matplotlib.pyplot as plot
import copy
import math
#Blank Map Matrix
BlankMap = np.zeros((200,300))

theta = math.radians(30)
#Fucntion to find equation of line between two points:
def FindLineEqn(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    c = y1-slope*x1
    return slope,c
print(FindLineEqn(75,85,50,150))

# Rotz = np.asarray([math.cos(theta), -math.sin(theta) , 0] ,[ math.sin(theta), math.cos(theta), 0 ], [ 0 , 0 , 1])
# xyz = np.asarray([a],[b],[c])
#Fucntion to select and store map

def GenerateMap(name):
    Map = copy.deepcopy(BlankMap)
    if(name == "Trial"):
        for x in range(200):
            for y in range(100):
                if((x>=90 and x<=110) and (y>=40 and y<=60)):
                    Map[100-y][x] = 1
                if((((x-160)**2 + (y-50)**2) < 15**2)):
                    Map[100-y][x] = 1
        return Map

    if(name == 'Map'):
        for x in range(300):
            for y in range(200):
                if((x-225)**2 + (y-150)**2 <= 25**2):
                    Map[200-y][x] = 1
                if(((x-150)**2/40**2 + (y-100)**2/20**2) <= 1):
                    Map[200-y][x] = 1
                if ((y-(0.6*x))>=(-125) and (y-(-0.6*x))<=(175) and (y-(0.6*x))<=(-95) and (y-(-0.6*x))>=(145)):
                    Map[200-y][x] = 1
                if((y-(13*x))<=(-140) and (y-(1*x))>=(100) and y <= 185 and (y-(1.4*x)>=80) and y<= 185):
                    Map[200-y][x] = 1
                if ((y-(-1.2*x))>=(210) and (y-(1.2*x))>=(30) and (y-(-1.4*x))<=(290) and (y-(-2.6*x))>=280 and y<=185):
                    Map[200-y][x] = 1
                if ((y - (1.73)*x + 135 >= 0) and (y + (0.58)*x - 96.35  <= 0) and (y - (1.73)*x - 15.54 <= 0) and (y + (0.58)*x - 84.81 >= 0)):
                    Map[200 - y][x] = 1
                # Map[200-10][225] = 3
                # if ((y-(-1.2*x))>=(210)):
                #     Map[199-y][x] = 1
                # if (y-(0.6*x))>=(-125):
                #     Map[199-y][x] = 1
                # if (y-(-0.6*x))>=(175):
                #     Map[199-y][x] = 1
        return Map
                # if((((x-160)**2 + (y-50)**2) < 15**2)):
                #     BlankMap[100-y][x] = 1

plot.matshow(GenerateMap("Map"))
plot.show()
