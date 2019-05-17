from sikuli import *
from sikuli import Region

# utils 


def MakeFullScreen_try():
#    setFindFailedResponse(SKIP)
    setThrowException(False)
    # Enlarge left bar
    try:

        Region(Region(1033,376,58,222)).find("1466943356273.png").click()
    except FindFailed:
        pass
    
    # remove up tool bar
    try:
        Region(Region(1085,131,84,28)).find("1466943375529.png").click() 
    except FindFailed:
        pass
#    setFindFailedResponse(ABORT)   
    setThrowException(True)
    Debug.user("Make Full Screen")
    return


def MakeFullScreen():
    # Enlarge left bar
    r = Region(Region(1042,426,35,114))
    with Region(r):
       if exists("1466943356273.png"):
           click(Location(1061, 458))
           

#        Region(Region(1033,376,58,222)).find("1466943356273.png").click()

    
    # remove up tool bar
    r_toptoolbar = Region(Region(1085,131,84,28))
    with Region(r_toptoolbar):
        if exists("1466943375529.png"):
            click()
#        Region(Region(1085,131,84,28)).find("1466943375529.png").click() 
    
    Debug.user("Make Full Screen")
    return


def ShowupCheck():
    r_mainmenu = Region(Region(429,149,596,231))
    with r_mainmenu:
        find("1466956847138.png").click()
        Region(Region(533,615,232,76)).find("1466956881720.png").click()
    wait(1)    
    type(Key.ESC)

    return


if __name__ == "__main__":
    openApp("Google Chrome")
    MakeFullScreen();
