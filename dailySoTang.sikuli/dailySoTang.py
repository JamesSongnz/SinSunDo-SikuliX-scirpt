from sikuli.Sikuli import *
#  this is for daily sotang
Debug.user("Daily SoTang %s" % ("V01"))

def ExitScript(event):
    exit()

# When the user pressed Ctrl+Alt+F1, click the top-left apple icon.
Env.addHotkey(Key.ESC, KeyModifier.CTRL ,ExitScript)

l_WarpHole = Location(1100, 610)
def SoTang():
    click(l_WarpHole )
    wait(0.5)
    click(l_WarpHole)
    wait(0.3)
    click(l_WarpHole)

    Region(Region(281,358,238,47)).find("1466956409763.png").click()
    r_sotangDial = Region(Region(722,351,135,24))
    with r_sotangDial:
        wait("1466956487245.png",2)
        click("1466956566521.png")
    
    r_sotangStart = Region(Region(687,528,172,71))
    with r_sotangStart:
        click("1466956644242.png")
        click("1466956655804.png")


    wait(2)
    Debug.user("End of Daily SoTang")
    click(Location(583, 495))
    return

if __name__ == "__main__":
    Settings.UserLogs = True
    Settings.UserLogPrefix = "user"
    Settings.ActionLogs = True
    openApp("Google Chrome")

    SoTang() 
    exit()
