import screenFn as fn
import pyautogui as gui

global currentLayer, elementPosLeft, elementPosLeft
currentLayer = 1
elementPosLeft, elementPosRight = fn.getelEmentPosLeftList()

def checkElementCreation():
    fn.imPathLayer('earthBottomLeft.PNG')
    checkForEarth = gui.locateCenterOnScreen(fn.imPathLayer('earthBottomLeft.PNG'), region = (40,900,120,100))
    if checkForEarth is not None:
        elementCreation = True
    else:
        elementCreation = False
    return elementCreation

def createElement():
    elementCreation = True
    while elementCreation:
        for elementLeft in elementPosLeft:
            fn.clickElement(elementLeft, 0.0)
            for elementRight in elementPosRight:
                fn.clickElement(elementLeft, 0.0)
                fn.clickElement(elementRight, 0.0)
                elementCreation = checkElementCreation()

def increaseLayer():
    global currentLayer
    layerNum = fn.layerCheck(currentLayer)
    groupsPosListLeft, groupsPosListRight = fn.groupSetup(currentLayer)
    for groupPosLeft in groupsPosListLeft:
        if groupPosLeft != 0:
            fn.clickGroup(groupPosLeft)
            for groupPosRight in groupsPosListRight:
                if groupPosRight != 0:
                    fn.clickGroup(groupPosRight)
                    createElement()
                    fn.clickGroup((1500,287))

increaseLayer()
