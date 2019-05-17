# -*- coding: utf-8 -*-

from sikuli.Sikuli import *
#from Screens import *
import Screens



# define : screen constants
class Action:
    def __init__(self):
        pass

    def Do(self,menu):
        if not Screens.select(menu):
            print ("Can not find ", menu)
            return False
        return True

    def post(self):
        pass


# 한글 주석 test
# 출석 이벤트 참여
class AttendAction(Action):

    I_MenuAttend = "MainMenuAttend.png"

    r_attendBtn = Region(533,615,232,76)
    i_Attend_btn = "A_Attend_attendbtn.png"

    def __init__(self):
        Action.__init__(self)

    def Do(self):
        if not Action.Do(self, self.I_MenuAttend):
            return False

        Screens.findClick(self.r_attendBtn, self.i_Attend_btn)
#        self.r_attendBtn.find(self.i_Attend_btn).click()

        self.post()

    def post(self):
        wait(1)
        type(Key.ESC)



class RewardAction(Action):

    I_MenuReward = Pattern("M_Menu_Reward.png").similar(0.5)

    r_AllGet = Region(575,645,87,41)
    i_AllGet_btn = "A_Reward_Allget.png"

    def __init__(self):
        Action.__init__(self)

    def Do(self):
        if not Action.Do(self,self.I_MenuReward):
            return False

        Screens.findClick(self.r_AllGet, self.i_AllGet_btn)
        #self.r_AllGet.find(self.i_AllGet_btn).click()
        self.post()

    def post(self):
        wait(1)
        type(Key.ESC)


class HonorAction(Action):

    I_MenuHonor = "M_Menu_Honor.png"

    r_HonorItem_InList = Region(438,393,361,161)
    i_GetHonorReward  = "A_Honor_getHonorReward.png"

    r_HonorConfirm_Dig = Region(541,422,168,115)
    i_HonorConfirm_btn = "A_Honor_HornorConfirm.png"

    r_dailyReward = Region(709,553,132,112)
    i_dailyReward = "A_Honor_getDailyReward.png"

    def Do(self):
        if not Action.Do(self,self.I_MenuHonor):
            return False

        # get honor
        if Screens.checkExists(self.r_HonorItem_InList, self.i_GetHonorReward):
            #Region(Region(438,393,361,161)).find(Pattern("1467385626798.png").targetOffset(280,3)).click()
            #self.r_HonorItem_InList.getLastMatch().targetOffset(280,3).click()
            Screens.findClick(self.r_HonorItem_InList, Pattern(self.i_GetHonorReward).targetOffset(280,3))
            wait(1.5)
            Screens.findClick(self.r_HonorConfirm_Dig, self.i_HonorConfirm_btn)

        # get daily yellow tickets

        for i in range(0,5):
            if Screens.checkExists(self.r_dailyReward, Pattern(self.i_dailyReward).similar(0.88)):
                self.r_dailyReward.getLastMatch().click()
                wait(1.5)


        self.post()

    def post(self):
        #wait(1)
        type(Key.ESC)

class SuyehAction(Action):
    I_MenuSuyeh  = Pattern("M_Menu_Suyeh.png").similar(0.89)

    r_SuyehBtn = Region(470,695,314,41)
    l_getBtn = Location(572, 717)

    def Do(self):
        if not Action.Do(self,self.I_MenuSuyeh):
            return False
        # wait until load suyeh screen
        wait(2)

        # click get btn until no more remains
        for i in range(0,12):
            click(self.l_getBtn)
            #wait(0.2)
            click(self.l_getBtn)
            #wait(0.2)

        #Screens.findClick(self.r_SuyehBtn, self.i_AllGet_btn)

        self.post()

    def post(self):
        #wait(1)
        type(Key.ESC)


class FishingAction(Action):

    r_LeftTextMenu = Region(19,265,76,173)
    l_TopTextMenu = Location(31, 281)

    r_FishDiag = Region(587,256,92,27)
    i_FishDiagText = "A_Fish_Diag_FishText.png"
    r_FishDiagBottom = Region(541,588,184,54)
    i_FishDiagBottom_getall = "A_FishDiag_Bottom_Getall.png"

    # check cur state
    def Do(self):
        click(self.l_TopTextMenu)
        wait(0.5)
        if Screens.checkExists(self.r_FishDiag, self.i_FishDiagText,2):
            pass
        else:
            Debug.user("No Fishing.. Skip")
            return

        Screens.findClick(self.r_FishDiagBottom,self.i_FishDiagBottom_getall)

        wait(5)

        self.post()

    def post(self):
        #wait(1)
        type(Key.ESC)

class JusulMergeAction(Action):
    IB_MenuJusul = "MB_Menu_Jusul.png"

    r_JusulDiagBtnArea = Region(344,587,119,50)
    i_JusulMergeBtn = "A_Jusul_Diag_MergeAll.png"

    r_JusulConfirmDiag = Region(526,453,204,69)
    i_ConfirmBtn = "A_Jusul_ConfirmDiag_ok.png"

    def Do(self):            print ("Can not find ", self.IB_MenuJusul)
    return False

Screens.findClick(self.r_JusulDiagBtnArea,self.i_JusulMergeBtn)
Screens.findClick(self.r_JusulConfirmDiag,self.i_ConfirmBtn)

self.post()

def post(self):
    wait(1)
    type(Key.ESC)


class JumsulAction(Action):
    I_MenuJumsul = "M_Menu_Jumsul.png"

    def Do(self):
        if not Action.Do(self, self.I_MenuJumsul):
            return False

        if not Screens.selectBottom(self.IB_MenuJusul):

        r_JumsulDiag  = Region(590,229,81,35)
        i_JumsulText = "A_Jumsul_TextTop.png"

        if not Screens.checkExists(r_JumsulDiag, i_JumsulText, 3):
            return

        l_rollDices = Location(620, 492)
        click(l_rollDices)

        r_1000kinusul =Region(646,426,80,48)
        i_1000kinusul  = "A_Jumsul_Diag_1000ki.png"

        # click 9 times
        Screens.findClick(r_1000kinusul, i_1000kinusul)
        for i in range(0,8):
            r_1000kinusul.getLastMatch().click() # click again 8 more

        l_ConfirmDices = Location(630, 453)
        click(l_ConfirmDices)

        # click ok 9 more
        for i in range(0,10):
            click(l_ConfirmDices)
            wait(0.5)
            click(l_ConfirmDices)

        self.post()

    def post(self):
        wait(1)
        click (Location(994, 239))


import Farm

class HarvistAction(Action):

    def Do(self):
        Farm.showupFarm()
        wait (1.5)

        Farm.HarvistMoney()

        # wait till finish animation
        wait (2)
        Farm.HarvistExp()

    def post(self):
        type(Key.ESC)


class InfinteAction(Action):

    def Do(self):
        if not Action.Do(self, "M_Main_100yeargungon.png"):
            return False

        r_100yearTry = Region(413,644,380,76)
        Screens.findClick(r_100yearTry, "A_100year_Challange.png")

        self.post()


    def post(self):
        wait(2)



class PeachAction(Action):
    I_MenuPeaches  = Pattern("M_Menu_Peaches.png").similar(0.89)

    l_peach_inPopupWin = Location(678, 408)

    def Do(self):
        if not Action.Do(self,self.I_MenuPeaches):
            return False
        # wait
        wait(1)

        # pick peach
        click(l_peach_inPopupWin)


        self.post()

    def post(self):
        wait(1)

