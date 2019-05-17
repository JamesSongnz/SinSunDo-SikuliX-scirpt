from sikuli.Sikuli import *



def getDailyHonor():
    Region(Region(403,133,637,242)).find("1467299772067.png").click()
    Region(Region(407,212,444,453)).find("1467299815068.png").click()
    Region(Region(505,382,230,114)).find("1467299871578.png").click()


def getDailyActivities():               
    Debug.user("Star of Daliy Activities")
    wait(0.5)

    click(Location(907, -751))
    wait(0.5)
    click(Location(679, -265))
    wait(1)
    click(Location(679, -265))
    wait(1)
    click(Location(679, -265))
    wait(1)
    
    click(Location(662, -400))
    wait(0.5)
    
    click(Location(512, -407))

    type(Key.ESC)
    #click(Location(727, -673))
    return;

def SinSunSeYe():
    r_menu=Region(Region(401,149,630,278))
    if not r_menu.exists(Pattern("1467385948969.png").similar(0.89),0.5):
        return
    """    
    try:    
        r_menu.find(Pattern("1467385948969.png").similar(0.89))
        pass
    except FindFailed:
        Debug.user("No SinsunSeYe.. Skip")
        return
    """
    
    # found 
    r_menu.getLastMatch().click()

    wait(2)
    
    # go n times 
    r_button = Region(Region(470,695,314,41))
    
    for i in range(0, 2):
        for j in range(0,40):
            click(Location(572, 717))
            wait(0.1)
            
#        if Region(Region(575,701,151,36)).exists("1467389244108.png"):
#            break

                    
    type(Key.ESC)
    return      
def JusulMerge():
    Region(Region(528,641,724,136)).find("1467386485959.png").click()
    Region(Region(344,587,119,50)).find("1467386514941.png").click()
    Region(Region(526,453,204,69)).find("1467386547264.png").click()
    type(Key.ESC)
    wait(0.5)

def Fishing():
    r_menu=Region(Region(19,265,76,173))
    # check cur state
    click(Location(31, 281))
    wait(0.3)
    if not Region(Region(587,256,92,27)).exists("1467389931121.png",1):
        Debug.user("No Fishing.. Skip")
        return
    
    
    r_inFishing=Region(Region(541,588,184,54))
    try: 
        r_inFishing.wait("1467386212104.png",1)
        r_inFishing.getLastMatch().click()
    except FindFailed:
        type(Key.ESC)
        return
    
    wait(7)
    if r_inFishing.exists("1467386212104.png"):
        JusulMerge()
        r_inFishing.getLastMatch().click()
        wait(5)
        
    type(Key.ESC)
    

def EventDayHeaven():
    Region(Region(401,149,630,278)).find("1467382850597.png").click()
    Region(Region(476,506,218,178)).find("1467382879502.png").click()
    Region(Region(1045,139,213,70)).find("1467382907611.png").click()
    Region(Region(790,173,313,176)).find("1467382945440.png").click()
    Region(Region(706,529,173,96)).find("1467382971051.png").click()
    Region(Region(1063,141,188,65)).find("1467383004792.png").click()

def getHonor():
    Region(Region(401,149,630,278)).find("1467383434959.png").click()
    
    wait(0.5)
    if not Region(Region(438,393,361,161)).exists("1467385626798.png"):
        return
    
    try:
        

        Region(Region(438,393,361,161)).find(Pattern("1467385626798.png").targetOffset(280,3)).click()
        wait(1.5)
        Region(Region(541,422,168,115)).find("1467384181447.png").click()
    except FindFailed:
        pass

    r_dailyReward = Region(Region(709,553,132,112))
#    r_dailyReward.find("1467383550190.png").click()
    for i in range(0,13):
        if r_dailyReward.exists(Pattern("1467384114680.png").similar(0.88),2):
            r_dailyReward.find(Pattern("1467384114680.png").similar(0.88)).click()
            wait(1)
        else:
            type(Key.ESC)
    
def Jumsul():
    r_menu = Region(Region(401,149,630,278))
    if not r_menu.exists("1467386698329.png"):
        return

    r_menu.getLastMatch().click()
    
    #Region(Region(401,149,630,278)).find("1467386698329.png").click()
    
    wait(0.1)
    Regino(Region(590,229,81,35)).wait("1467729951535.png",3)
    consumed = 0
    for i in range(0,10):
        click(Location(547, 511))

        if consumed == 0 and Region(Region(569,365,23,27)).exists("1467386842469.png",0.5):
            if not Region(Region(643,428,93,44)).exists("1467391247826.png"):
                

                for j in range(0,10):
                    if not Region(Region(546,483,78,28)).exists("1467391052997.png",0,3):
                    #if not Region(Region(342,399,10,13)).exists("1467386956004.png",0.5):
                        click(Location(684, 452)) # 1000 ki nu sul
                    else:
                        consumed = 1

        else:
            # retry 
            pass
        
        # get this one
        Region(Region(524,408,213,60)).find("1467386785694.png").click()
    Region(Region(948,212,73,55)).find("1467391353325.png").click()

    Region(Region(646,426,80,48)).find("1467730249151.png")
    
#    Region(Region(541,422,168,115)).find("1467384181447.png").click()
    

if __name__ == "__main__":
    #  this is for daily sotang
    Settings.UserLogs = True
    Settings.UserLogPrefix = "user"
    Settings.ActionLogs = True
    openApp("Google Chrome")
    Debug.user("Sub Char %s" % ("V01"))

    Jumsul()
    exit()
    #getDailyActivities() 
#    JusulMerge()
    Fishing()
    exit()
    SinSunSeYe()
    exit()
    getHonor()

    EventDayHeaven()

    Debug.user("End of Daily SoTang")
    exit()
