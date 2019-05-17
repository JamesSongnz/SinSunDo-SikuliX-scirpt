from sikuli.Sikuli import *
import utils
reload(utils)
from utils import *

import dailyAct
reload(dailyAct)
from dailyAct import *

#  this is for daily sotang
Debug.user("Sub char each join evt & go  %s" % ("V01"))

def ExitScript(event):
    exit()

# When the user pressed Ctrl+Alt+F1, click the top-left apple icon.
Env.addHotkey(Key.ESC, KeyModifier.CTRL ,ExitScript)

def eachSubCharStart():
    # find empty event icon
    # click found 
    # comeback ori tab
    # join, get Daliy
    # turn ssd tab
    # click go 
    # turn ssd go tab 
    r_IDicons = Region(Region(10,315,350,364))

#    r_IDicons.find("../IdIconEmpty.png").click()
    r_IDicons.find("IdIconEmpty.png").click()
    wait(0.5)
    type(Key.TAB , KeyModifier.CTRL + KeyModifier.SHIFT )
#    Region(92,-893,377,55).find ("JoinEvent.png").click()
    wait(0.5)
    
    Region(Region(382,168,687,60)).find ("GetDaliyReward.png").click()
    wait(0.5)
    type(Key.TAB , KeyModifier.CTRL )

def checkLoginPeriod():
    # check event join result 
    if not Region(Region(425,284,441,111)).exists("1467297251249.png",0.5):
        return
    
    click(Location(117, 215)) 
    type(Key.SPACE)
    Region(Region(236,129,757,238)).find("1467297304824.png").click()
    

def CheckEventResult():
    # check event join result 
    #openApp("your-browser") # should open a new Browser window
    wait(0.5) # make sure window is ready
    type("l", KeyModifier.CMD)
    #wait(1)
    paste("http://ssd.ilovegame.co.kr/event/read/1872")
    type(Key.ENTER)
    wait(0.5)
    #openApp("Google Chrome", "http://ssd.ilovegame.co.kr/event/read/1793")
    type(Key.SPACE);
    wait(1)
    type(Key.SPACE, KeyModifier.SHIFT)
    
    # check daily join result 
#    Region(838,-954,95,46).find("1446477118087.png").click()   
#    wait(0.7)
#    Region(-54,-600,847,612).find("DialogDailyClose.png").click()
#    wait(0.3)
    

def GoFlashSSD():
    Region(Region(125,337,279,364)).find("1466955773193.png").click()
    wait(1)
    
    Debug.user("End of each sub char start")

if __name__ == "__main__":
    Settings.UserLogs = True
    Settings.UserLogPrefix = "user"
    Settings.ActionLogs = True
    openApp("Google Chrome")

    if not Region(Region(149,722,260,79)).exists("1466955899374.png",0.5):
        eachSubCharStart() 
    #    CheckEventResult()
        checkLoginPeriod()
        GoFlashSSD()
        
        
        wait(4)
        MakeFullScreen()
    
        Region(Region(149,722,260,79)).wait("1466955899374.png", 20)
        wait(3) # to wait until reorganize menu icon
        Debug.user("Reload done !!" )
    
    ShowupCheck()    

    
    runScript("/Users/JamesSong/getDailyReward")
    getHonor()  
    SinSunSeYe()
    Fishing()
    Jumsul()
    #EventDayHeaven()
    wait(1)

    runScript("/Users/JamesSong/dailySoTang")
    exit()
