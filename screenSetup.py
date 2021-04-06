import pyautogui as gui
import os
import time
print('\n\n\n')

#enough time to change windows, to be improved
time.sleep(3)

#Initialize gorups
groupsToCheck = ['air','earth','fire','water']

def imPath(filename):
    #Returns the filename with 'images/' prepended.
    return os.path.join("C:\\Users\giron\Desktop\Doodle God AI\images", filename)

#GameRegion[0,1,2,3] corresponds to [left,top,height,width]
pixelSize = 0.179 #mm (My PC has a pixel size of 0.179mm)
global GameRegionLeft
GameRegionLeft = (45/pixelSize, 25/pixelSize, 185/pixelSize, 165/pixelSize)
GameRegionRight = (0,0,0,0)

def groupSetup(groupsToCheck, groupsList):
    numGroups = 4
    for group in groupsToCheck:
        groupImPath = imPath(group+'.PNG')
        groupPos, groupExists = groupCheck(group, groupImPath)
        if groupExists:
            groupsList.append(group)
        else:
            groupsList.append('Empty')
        print(groupsList)

def groupCheck(group, groupImPath):
    groupPos = gui.locateCenterOnScreen(groupImPath, condifence = 0.5)
    if groupPos is not None:
        groupExists = True       
        print(group + ' found')
        return groupPos, groupExists
    else:
        groupPos = 0
        groupExists = False
        print(group + ' does not exist')
        return groupPos, groupExists

groupsList = []
groupSetup(groupsToCheck,groupsList)
