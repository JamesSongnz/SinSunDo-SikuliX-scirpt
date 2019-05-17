from sikuli.Sikuli import *


# define : screen constants
#class Screen:

R_MainMenu = Region(401,149,630,278)
#Region(411,147,610,238)

R_BottomMenu = Region(528,641,724,136) #Region(530,716,717,48)

__verbose = True


# select ,
# if not exist return false
def selectA(self,menuItem):
    if not self.R_MainMenu.exists(menuItem,0.5):
        return False

    self.R_MainMenu.getLastMatch().click()
    return True


def selectBase(menuRegion, menuItem):
    if not menuRegion.exists(menuItem,1):
        return False

    menuRegion.getLastMatch().click()
    return True

def select(menuItem):
    return selectBase(R_MainMenu,menuItem)

def selectBottom(menuItem):
    return selectBase(R_BottomMenu,menuItem)

def findClick(r,icon):
    try:
        r.find(icon).click()
    except FindFailed:
        print ("Find Failed : Region: ", r, " icon : ", icon)
        return False
    return True

def checkExists(r, icon, timeout = 1):
    if r.exists(icon,timeout):
        return True

    if __verbose:
        print ("Not Exists : region ",r, " icon ", icon )
    return False

#class CharScreen:
#    R_CharList = Region(10,315,350,364)
