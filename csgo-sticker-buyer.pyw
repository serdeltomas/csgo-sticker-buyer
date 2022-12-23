from pyautogui import *
from tkinter import *
import pyautogui
import time
import threading

DELAY_WHEN_BUYING = 0.1

def loading(full,now):
    now_perc = 100.0*(1.0*now/full)
    now_perc = '{:05.2f}'.format(float(now_perc))
    print(now_perc + "%")
    result = " " + now_perc + "% ▕"
    now_perc_quart = float(now_perc)/5
    full_blocks = int(now_perc_quart // 1)
    now_perc_quart = now_perc_quart-full_blocks
    for x in range(0,full_blocks):
        result = result + "█"
    if now_perc_quart>=0.125:
        halfblock = 1
    else:
        halfblock = 0
    if now_perc_quart>=0.875:
        result = result + "▉"
    elif now_perc_quart>=0.75:
        result = result + "▊"
    elif now_perc_quart>=0.625:
        result = result + "▋"
    elif now_perc_quart>=0.5:
        result = result + "▌"
    elif now_perc_quart>=0.375:
        result = result + "▍"
    elif now_perc_quart>=0.25:
        result = result + "▎"
    elif now_perc_quart>=0.125:
        result = result + "▏"
    for x in range(0,20-full_blocks-halfblock):
        result = result + "▔"
    result = result + "▏ "
    return result

def recalculate_on_edit(*args):
    try:
        sumofall.set(int(spin11.get()) + int(spin12.get()) + int(spin13.get()) + int(spin14.get()) + int(spin15.get()) + int(spin16.get()) + int(spin17.get()))
        if int(sumofalltxt.cget("text")) > 1000:
            tip.configure(bg="red", fg="#2d2d30", text=" ! ! ! too many items, your inventory will overflow ! ! ! ")
            btn.configure(state='disabled', bg='#252526')
        else:
            tip.configure(bg="#2d2d30", fg="#2d2d30", text="")
            btn.configure(state='normal', bg="#007ACC")
    except:
        sumofall.set("bad value")
 
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
        time.sleep(DELAY_WHEN_BUYING)
        click(list(num_pos_dict.values())[sticker_count - 1])

def waitFor(image):
    found_img = None
    time_start = time.perf_counter()
    while found_img == None:
        found_img = pyautogui.locateOnScreen(image)
        if pyautogui.locateOnScreen("img/add_funds.png") != None:
            tip.configure(bg="orange", fg="#2d2d30", text=" ! run stopped, add more funds to your steam wallet ! ")
            return False
        time_now = time.perf_counter()
        if (time_now - time_start) > 10:
            tip.configure(bg="orange", fg="#2d2d30", text=(" ! run stopped, no image found - " + image + " ! "))
            return False
    return True
    
def show_spins(is_show):
    if is_show == True:
        spin11.configure(state='normal')
        spin12.configure(state='normal')
        spin13.configure(state='normal')
        spin14.configure(state='normal')
        spin15.configure(state='normal')
        spin16.configure(state='normal')
        spin17.configure(state='normal')
    elif is_show == False:
        spin11.configure(state='disabled')
        spin12.configure(state='disabled')
        spin13.configure(state='disabled')
        spin14.configure(state='disabled')
        spin15.configure(state='disabled')
        spin16.configure(state='disabled')
        spin17.configure(state='disabled')
    
def buy(sticker_name,num_stickers):
    time.sleep(DELAY_WHEN_BUYING)
    click(getParent(sticker_name))
    time.sleep(DELAY_WHEN_BUYING)
    click(getPos(sticker_name))
    time.sleep(DELAY_WHEN_BUYING)
    click(dropdown_menu_pos)
    time.sleep(DELAY_WHEN_BUYING)
    clickCount(num_stickers)
    time.sleep(DELAY_WHEN_BUYING)
    click(price_btn_pos)
    if waitFor("img/authorize.png")==False:
        return False
    pyautogui.move(-23,-55)
    pyautogui.click('img/authorize.png')
    if waitFor("img/continue.png")==False:
        return False
    pyautogui.press('esc')
    print("bought:\t",num_stickers)
    return True

#do for every type of sticker
#repeat while x!=0 do x>20? do 20 buy else do x buy
def main_prog():
    # num of each sticker to be filled by user
    sticker_count_dict = {
    'leg_team' : int(spin11.get()),
    'leg_aut' : int(spin12.get()),
    'chal_team' : int(spin13.get()),
    'chal_aut' : int(spin14.get()),
    'cont_team' : int(spin15.get()),
    'cont_aut' : int(spin16.get()),
    'champ_aut' : int(spin17.get())}
    
    all_count = int(sumofalltxt.cget("text"))
    now_count = 0
    
    if waitFor("img/rio_2022.png")==False:
        return False
    
    for sticker_name in sticker_count_dict:
        sticker_count = sticker_count_dict[sticker_name]
        print(sticker_name,":" ,sticker_count)
        while sticker_count != 0:
            if sticker_count >= 20:
                sticker_count = sticker_count - 20 
                if buy(sticker_name,20) == False:
                    return False
                now_count = now_count + 20
            else:
                if buy(sticker_name,sticker_count) == False:
                    return False
                now_count = now_count + sticker_count
                sticker_count = 0
            tip.configure(text=loading(all_count,now_count))
    print("CAPSULES BOUGHT: ",all_count)
    return True
    
def click_start_btn():
    show_spins(False)
    btn.configure(state='disabled', bg='#252526')
    tip.configure(bg="black",fg ="#8A8A8A", text=loading(100,0))
    if main_prog()==True:
        time.sleep(1)
        tip.configure(bg="green",fg ="#2d2d30", text="  Done, Restart app if you want to buy more  ")    
    btn.configure(text='Restart app')
    

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

#gui window
window = Tk()

window.title("csgo-sticker-buyer")
window.geometry('335x307')
window.configure(bg='#2d2d30')

titleframe = Frame(window, bg ="#1e1e1e")
titleframe.grid(row=0, column=0, columnspan=2, sticky='ew')
lbl00 = Label(titleframe, text="Rio 2022 Capsule Type", font=(20), bg="#1e1e1e", fg="#8A8A8A")
lbl00.grid(column=0, row=0, pady=10, padx= 30)
lbl10 = Label(titleframe, text="Count", font=(20), bg="#1e1e1e", fg="#8A8A8A")
lbl10.grid(column=1, row=0, pady=10, padx= 20)

lbl01 = Label(window, text="Legends Sticker Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl01.grid(column=0, row=1)
lbl02 = Label(window, text="Legends Autograph Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl02.grid(column=0, row=2)
lbl03 = Label(window, text="Challengers Sticker Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl03.grid(column=0, row=3)
lbl04 = Label(window, text="Challengers Autograph Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl04.grid(column=0, row=4)
lbl05 = Label(window, text="Contenders Sticker Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl05.grid(column=0, row=5)
lbl06 = Label(window, text="Contenders Autograph Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl06.grid(column=0, row=6)
lbl07 = Label(window, text="Champions Autograph Capsule", bg="#2d2d30", fg="#8A8A8A")
lbl07.grid(column=0, row=7)

spin11txt = IntVar(window,"0")
spin11 = Spinbox(window, from_=0, to=1000, textvariable=spin11txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin11.grid(column=1, row=1, pady=2)
spin12txt = IntVar(window,"0")
spin12 = Spinbox(window, from_=0, to=1000, textvariable=spin12txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin12.grid(column=1, row=2)
spin13txt = IntVar(window,"0")
spin13 = Spinbox(window, from_=0, to=1000, textvariable=spin13txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin13.grid(column=1, row=3, pady=2)
spin14txt = IntVar(window,"0")
spin14 = Spinbox(window, from_=0, to=1000, textvariable=spin14txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin14.grid(column=1, row=4)
spin15txt = IntVar(window,"0")
spin15 = Spinbox(window, from_=0, to=1000, textvariable=spin15txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin15.grid(column=1, row=5, pady=2)
spin16txt = IntVar(window,"0")
spin16 = Spinbox(window, from_=0, to=1000, textvariable=spin16txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin16.grid(column=1, row=6)
spin17txt = IntVar(window,"0")
spin17 = Spinbox(window, from_=0, to=1000, textvariable=spin17txt, width=10,fg="white",bg="#454545", buttonbackground="#000000",disabledbackground="#252526")
spin17.grid(column=1, row=7, pady=2)

spin11txt.trace('w', recalculate_on_edit)
spin12txt.trace('w', recalculate_on_edit)
spin13txt.trace('w', recalculate_on_edit)
spin14txt.trace('w', recalculate_on_edit)
spin15txt.trace('w', recalculate_on_edit)
spin16txt.trace('w', recalculate_on_edit)
spin17txt.trace('w', recalculate_on_edit)

lbl08 = Label(window, text="Sum of all = ", bg="#2d2d30", fg="#8A8A8A")
lbl08.grid(column=0, row=8, pady=5, sticky=E)
sumofall = IntVar(window,"0")
sumofalltxt = Label(window, width=10,textvariable=sumofall, bg="#454545", fg="#8A8A8A")
sumofalltxt.grid(column=1, row=8)

tip = Label(window, bg="#2d2d30", fg="#2d2d30", font=("Lucida Sans Unicode",8))
tip.grid(row=9, columnspan = 2, pady=5)

#click start button
btn = Button(window, text="Start", bg="#007ACC", fg="#2d2d30", command=threading.Thread(target=click_start_btn).start, font=(20), width=34)
btn.grid(columnspan=2, row=11, padx=10, sticky=W+E+N+S)

window.mainloop()

