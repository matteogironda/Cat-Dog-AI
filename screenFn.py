import pyautogui as gui
import os
import time
from pathlib import Path

print('\n\n\n')
global GameRegionLeft, groupNumRegion, layerList, currentLayer, groupsToCheck
#enough time to change windows, to be improved
time.sleep(3)

#Initialize gorups
groupsToCheck = ['air','earth','fire','water', 'tao', 'bacteria']
layerList = []
totalLayerNum = 4
for layer in range(1,totalLayerNum):
    layerList.append(str(layer))
currentLayer = 1
groupResetLeft = (492,287)
groupResetRight = (1500,287)
#GameRegion[0,1,2,3] corresponds to [left,top,height,width]
pixelSize = 0.179 #mm (My PC has a pixel size of 0.179mm)
GameRegionLeft = (239, 103, 185/pixelSize, 165/pixelSize)
GameRegionRight = (1039,134, 800, 880)
groupNumRegion = (709,39,20,29)

def imPathGroup(filename, currentLayer):
    #Returns the filename with 'images/' prepended.
    return os.path.join("C://Users\giron\Desktop\Doodle God AI\images\Layer"+str(currentLayer), filename)

def imPathLayer(filename):
    #Returns the filename with 'images/' prepended.
    return os.path.join("C://Users\giron\Desktop\Doodle God AI\images/readLayer", filename)

def checkPath(group, currentLayer):
    fileToCheck = Path("C://Users\giron\Desktop\Doodle God AI\images\Layer"+str(currentLayer)+'/'+group+'.PNG')
    if fileToCheck.is_file():
        fileExists = True
        return fileExists
    else:
        fileExists = False
        return fileExists

def getelEmentPosLeftList():
    elementPosLeft = [0]*10
    elementPosLeft[0] = (770,280)
    elementPosLeft[1] = (770,400)
    elementPosLeft[2] = (770,530)
    elementPosLeft[3] = (770,680)
    elementPosLeft[4] = (770,280)
    elementPosLeft[5] = (900,815)
    elementPosLeft[6] = (900,280)
    elementPosLeft[7] = (900,400)
    elementPosLeft[8] = (900,530)
    elementPosLeft[9] = (900,680)

    elementPosRight = [0]*10
    elementPosRight[0] = (1300,280)
    elementPosRight[1] = (1300,400)
    elementPosRight[2] = (1300,530)
    elementPosRight[3] = (1300,680)
    elementPosRight[4] = (1300,280)
    elementPosRight[5] = (1200,815)
    elementPosRight[6] = (1200,280)
    elementPosRight[7] = (1200,400)
    elementPosRight[8] = (1200,530)
    elementPosRight[9] = (1200,680)

    return elementPosLeft, elementPosRight

def groupCheck(group, currentLayer):
    # When opencv is downloaded the region attribute does not work, 
    # Confidence will not be used as it is not as reliable as we need it to be
    fileExists = checkPath(group, currentLayer)
    if fileExists:
        groupPosLeft = gui.locateCenterOnScreen(imPathGroup(group+'.PNG', currentLayer), region = GameRegionLeft)
        if groupPosLeft is not None:
            groupPosRight = (groupPosLeft.x+800,groupPosLeft.y)
            groupExists = True       
            print(group + ' found')
            return groupPosLeft, groupPosRight, groupExists
        else:
            groupPosRight = 0
            groupPosLeft = 0
            groupExists = False
            print(group + ' does not exist')
            return groupPosLeft, groupPosRight, groupExists
    else:
        groupPosRight = 0
        groupPosLeft = 0
        groupExists = False
        print(group + ' does not exist')
    return groupPosLeft, groupPosRight, groupExists

def groupSetup(currentLayer):
    groupsList = []
    groupsPosListLeft = []
    groupsPosListRight = []
    numGroups = 6
    for group in groupsToCheck:
        groupPosLeft, groupPosRight, groupExists = groupCheck(group, currentLayer)
        if groupExists:
            groupsList.append(group)
            groupsPosListLeft.append(groupPosLeft)
            groupsPosListRight.append(groupPosRight)
        else:
            groupsList.append('Empty')
            groupsPosListLeft.append(groupPosLeft)
            groupsPosListRight.append(groupPosRight)
    print('\n',groupsList)
    print('\n',groupsPosListLeft)
    print('\n',groupsPosListRight)
    return groupsPosListLeft, groupsPosListRight

def clickGroup(groupPos):
    gui.click(groupPos)

def clickElement(elementPos, delay):
    gui.click(elementPos)
    time.sleep(delay)

def layerCheck(currentLayer):
    #Layer1 starts at 4 elemments, 2 at 5 and so on
    try:
        print('reading Layer\n')
        layerImage = currentLayer + 3
        readLayer = gui.locateOnScreen(imPathLayer(str(layerImage)+'.PNG'))
        if readLayer is not None:
            layerNum = currentLayer
            print('same Layer\n')
        else:
            layerNum = currentLayer + 1
            print('new Layer\n')
        return layerNum
    except Exception as e:
        print('[ERROR in layerCheck:] ',e)
