from sikuli.Sikuli import *

import Screens

l_MoneyTree = Location(688, 466)
l_ExpTree  = Location(571, 470) # exptree

r_TreeDiagTitle = Region(587,358,84,24)

r_HarvistDiagBtn = Region(582,570,94,36)


def showupFarm():
    r_leftmenu = Region(Region(14,306,83,116))
    r_farm = Region(Region(610,231,39,21))
    if not r_farm.exists("Md_Harvist_FarmTitleText.png",1):
        r_leftmenu.find(Pattern("M_LeftMenu_Harvist.png").similar(0.46)).click()


def harvist(fl, locTree):
    Debug.user("Harvist one")
    print fl
#    mouseMove(fl)
    click(fl)

    # wait select tree diag
    if not Screens.checkExists(r_TreeDiagTitle, "Md_Harvist_TreeDiagTitle.png",1):
        return False

    # moneytree or exptree
    click(locTree)
    sleep(0.2)

    if not Screens.findClick(r_HarvistDiagBtn, "Md_Harvist_DiagGet.png"):
        return False

#    sleep(1)
#    click(fl)
    return True

def MakeFarmArray():

    #    r_harvmenu = Region(-158,-653,101,251)
    avail_f = []
    field_array = [Location(623, 381), Location(536, 424), Location(453, 471),Location(709, 421)] #, Location(535, 510),Location(795, 461) ]
    for fl in field_array:
        r = Region(fl.x - 25, fl.y-20, 50, 40)
        if r.exists("Md_Harvist_soil.png",1):
            avail_f.append(fl)

    print ("Found ", avail_f)
    return avail_f


TreeTypePtr  = { 'money' : l_MoneyTree, 'exp' : l_ExpTree }

def HarvistMoney():
    mfs = MakeFarmArray()
    if not HarvistArray(mfs, 'money'):
        return

    # 1 more (8 times )
    HarvistArray(mfs, 'money')


def HarvistExp():
    # remove mouse cursor on the soil
    mouseMove(Location(752, 372))
    wait(1)     # wait until money harvist animation finished
    efs = MakeFarmArray()
    HarvistArray(efs, 'exp')


def HarvistArray(farms, type):
    Debug.user("==== ")
    grow_farm = []
    for f in farms:
        Debug.user("try Harvist ")
        print f

        if not harvist(f, TreeTypePtr[type]):
            # Screens. region .findclick X
            click(Location(752, 372))
            break  #
            #return False
        wait(0.5)
        grow_farm.append(f)

    for f in grow_farm:
        # click f
        click(f)
        wait(0.2)

    print grow_farm
    return True

