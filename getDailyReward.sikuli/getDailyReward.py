from sikuli import *

import utils
reload(utils)
from utils import *

def getDailyRewards():
    type(Key.ESC)

    Region(Region(411,147,610,238)).find("1467558441370.png").click()
    Region(Region(575,645,87,41)).find("1466952677862.png").click()
    #click(Location(659, -633))
    #wait(0.3)
    #click(Location(659, -633))
    wait(0.3)

#    Debug.user("End of Daily rewards")
    type(Key.ESC)
    return

if __name__ == "__main__":
    Settings.UserLogs = True
    Settings.UserLogPrefix = "user"
    Settings.ActionLogs = True
    openApp("Google Chrome")

    type(Key.ESC)
#    MakeFullScreen()
    getDailyRewards();
