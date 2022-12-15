from pyautogui import *
import pyautogui
import time

time.sleep(2)

# num of each sticker to be filled by user
sticker_count_dict = {
'leg_team' : 0,
'leg_aut' : 0,
'chal_team' : 0,
'chal_aut' : 0,
'cont_team' : 0,
'cont_aut' : 0,
'champ_aut' : 0}

# positions of all elements
leg_parent_pos =[735,870]
chal_parent_pos = [955,870]
cont_parent_pos = [1185,870]
champ_parent_pos = [1400,850]
leg_team_pos = [940,920]
leg_aut_pos = [1150,920]
chal_team_pos = [1170,920]
chal_aut_pos = [1340,920]
cont_team_pos = [1330,920]
cont_aut_pos = [1520,920]
champ_aut_pos = [1560,920]

dropdown_menu_pos = [1187,1035]
scroll_down_pos = [1232,1003]
num_pos_dict = {
'num_1_pos' : [1200,610],
'num_2_pos' : [1200,650],
'num_3_pos' : [1200,690],
'num_4_pos' : [1200,730],
'num_5_pos' : [1200,770],
'num_6_pos' : [1200,810],
'num_7_pos' : [1200,850],
'num_8_pos' : [1200,890],
'num_9_pos' : [1200,930],
'num_10_pos' : [1200,970]}
price_btn_pos = [1290,1040]


def click(point):
    pyautogui.moveTo(point[0], point[1])
    pyautogui.click(x=point[0], y=point[1])

def getParent(sticker_name):
    if "leg" in sticker_name:
        return leg_parent_pos
    elif "chal" in sticker_name:
        return chal_parent_pos
    elif "cont" in sticker_name:
        return cont_parent_pos
    elif "champ" in sticker_name:
        return champ_parent_pos

def getPos(sticker_name):
    if "aut" in sticker_name:
        if "leg" in sticker_name:
            return leg_aut_pos
        elif "chal" in sticker_name:
            return chal_aut_pos
        elif "cont" in sticker_name:
            return cont_aut_pos
        elif "champ" in sticker_name:
            return champ_aut_pos
    elif "team" in sticker_name:
        if "leg" in sticker_name:
            return leg_team_pos
        elif "chal" in sticker_name:
            return chal_team_pos
        elif "cont" in sticker_name:
            return cont_team_pos

def clickCount(sticker_count):
    if sticker_count <= 10:
        click(list(num_pos_dict.values())[sticker_count - 1])
    elif sticker_count > 10:
        sticker_count = sticker_count - 10
        click(scroll_down_pos)
        time.sleep(0.1)
        click(list(num_pos_dict.values())[sticker_count - 1])

def waitFor(image):
    found_img = None
    while found_img == None:
        found_img = pyautogui.locateOnScreen(image)
        if pyautogui.locateOnScreen("img/add_funds.png") != None:
            break
                        
def buy(sticker_name,num_stickers):
    time.sleep(0.1)
    click(getParent(sticker_name))
    time.sleep(0.1)
    click(getPos(sticker_name))
    time.sleep(0.1)
    click(dropdown_menu_pos)
    time.sleep(0.1)
    clickCount(num_stickers)
    time.sleep(0.1)
    click(price_btn_pos)
    waitFor("img/authorize.png")
    pyautogui.move(-23,-55)
    pyautogui.click('img/authorize.png')
    waitFor("img/continue.png")
    pyautogui.press('esc')
    print("bought:\t",num_stickers)
    return

#do for every type of sticker
#repeat while x!=0 do x>20? do 20 buy else do x buy
for sticker_name in sticker_count_dict:
    sticker_count = sticker_count_dict[sticker_name]
    print(sticker_name,":" ,sticker_count)
    while sticker_count != 0:
        if sticker_count >= 20:
            sticker_count = sticker_count - 20 
            buy(sticker_name,20)
        else:
            buy(sticker_name,sticker_count)
            sticker_count = 0

print("STICKERS BOUGHT")
