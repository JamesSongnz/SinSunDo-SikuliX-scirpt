from sikuli.Sikuli import *
#  this is for daily sotang
Debug.user("Sub char each join evt & go  %s" % ("V01"))

def ExitScript(event):
    exit()

# When the user pressed Ctrl+Alt+F1, click the top-left apple icon.
Env.addHotkey(Key.ESC, KeyModifier.CTRL ,ExitScript)
setThrowException(False)
def WaitReload():
  
    click(Location(74, 77))    
    wait(5)
#    Region(47,-129,121,37).wait("1446565520094.png", 9)
    wait(12) # to wait until reorganize menu icon
    Debug.user("Reload done !!" )
    
def InfiniteRetry_100year():
    # choice retry item
    # go. 
    # reload
    # wait 
    # re-
    wait(0.5)
    
    r_Menuicons = Region(Region(342,185,661,313))


    # six return 
    #r_Menuicons.find("../SixReturn.png").click()
    r_Menuicons.find("1467211405339.png").click() 
    startSix = False
    while not startSix:
        r_sixbutton = Region(Region(413,644,380,76))
        m_six = r_sixbutton.wait("1467211523552.png")
        m_six.click()
#        m_six.click()
        wait(2) 

        # check fight-remain time
        #try:
        ret = r_sixbutton.waitVanish("../SixButtonReset.png",8)
        if ret:
            startSix = True
        #except FindFailed:
        else:        
            wait(3)


    WaitReload()


def InfiniteRetry():
    # choice retry item
    # go. 
    # reload
    # wait 
    # re-
    wait(0.5)
    
    r_Menuicons = Region(Region(342,185,661,313))


    # six return 
    #r_Menuicons.find("../SixReturn.png").click()
    r_Menuicons.find("1467211405339.png").click() 
    startSix = False
    while not startSix:
        r_sixbutton = Region(599,-357,246,147)
        m_six = r_sixbutton.find("1446569622154.png")
        m_six.click()
        m_six.click()
        wait(2) 

        # check fight-remain time
        #try:
        ret = r_sixbutton.waitVanish("../SixButtonReset.png",8)
        if ret:
            startSix = True
        #except FindFailed:
        else:        
            wait(3)


    WaitReload()

"""
    # restrictedArea
    r_Menuicons.find("../RestrictArea.png").click()
    wait(1)
    m_resA=Region(407,-288,200,88).find("1446569783834.png")
    m_resA.click()
    m_resA.click()    
    wait(0.5)    
    WaitReload()   
"""


if __name__ == "__main__":
    Settings.UserLogs = True
    Settings.UserLogPrefix = "user"
    Settings.ActionLogs = True
    openApp("Google Chrome")
    setThrowException(False)
    
    for i in xrange(200):
        InfiniteRetry_100year()
        Debug.user("retury done %d " % i)
        
    exit()
