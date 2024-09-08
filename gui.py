
from pathlib import Path
from threading import Thread
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from time import sleep
import pandas as pd
import os
import datetime as dt
from notifypy import Notify
from pygame import mixer 
mixer.init() 
isfirst_time=False
# Loading the song 
mixer.music.load("Timeout.mp3") 
  
# Setting the volume 
mixer.music.set_volume(10) 
notification = Notify()
notification.title = "Timeout"
notification.icon='images.png'
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
game_data=pd.DataFrame({'game_name':['start'],'price':[0],'time':['start']})
if not(os.path.isfile('game.csv')):
    pd.DataFrame({'game_name':['start'],'price':[0],'time':['start']}).to_csv('game.csv')
    isfirst_time=True
else:
    game_data=pd.read_csv('game.csv')
    print(game_data)
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def one():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "one"
    notification.send()
    mixer.music.play() 
    sleep(2)
def start_one():
    global game_data
    t=Thread(target=one)
    t.start()
    x=pd.DataFrame({'game_name':'little_road','price':[150],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x],)
def three():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "one"
    notification.send()
    mixer.music.play() 
    sleep(2)
def start_three():
    global game_data
    t=Thread(target=three)
    t.start()
    x=pd.DataFrame({'game_name':'little_road','price':[150],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x],)
def two():
    sleep(600)
    print('ok')
    notification.message = "Board game"
    notification.send()
    mixer.music.play() 
    sleep(2)
def start_two():
    global game_data
    t=Thread(target=two)
    t.start()
    x=pd.DataFrame({'game_name':'little_road','price':[150],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x],)
def Board_game():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Board game"
    notification.send()
    mixer.music.play() 
    sleep(2)
def start_Board_game():
    global game_data
    t=Thread(target=Board_game)
    t.start()
    x=pd.DataFrame({'game_name':'little_road','price':[150],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x],)
def little_road():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Little road"
    notification.send()
    mixer.music.play() 
    sleep(2)
def start_little_road():
    global game_data
    t=Thread(target=little_road)
    t.start()
    x=pd.DataFrame({'game_name':'little_road','price':[150],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x],)
def little_war():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Little war"
    notification.send()

    mixer.music.play() 
    sleep(2)
def start_little_war():
    global game_data
    t=Thread(target=little_war)
    t.start()
    x=pd.DataFrame({'game_name':'little_war','price':[200],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])
def Hovercraft():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Hovercraft"
    notification.send()

    mixer.music.play() 
    sleep(2)
def start_Hovercraft():
    global game_data
    t=Thread(target=Hovercraft)
    t.start()
    x=pd.DataFrame({'game_name':'Hovercraft','price':[200],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])
def RC():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "RC climber"
    notification.send()
    
    mixer.music.play() 
    sleep(2)
def start_RC():
    global game_data
    t=Thread(target=RC)
    t.start()
    x=pd.DataFrame({'game_name':'RC_climber','price':[200],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])
def VR():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "VR"
    notification.send()
    
    mixer.music.play() 
    sleep(2)
def start_VR():
    global game_data
    t=Thread(target=VR)
    t.start()
    x=pd.DataFrame({'game_name':'VR','price':[100],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])
def human_soccer():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Human soccer"
    notification.send()
    
    mixer.music.play() 
    sleep(2)
def start_human_soccer():
    global game_data
    t=Thread(target=human_soccer)
    t.start()
    x=pd.DataFrame({'game_name':'human_soccer','price':[300],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])
def machine_soccer():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Machine soccer"
    notification.send()
    
    mixer.music.play() 
    sleep(2)
def start_machine_soccer():
    global game_data
    t=Thread(target=machine_soccer)
    t.start()
    x=pd.DataFrame({'game_name':'machine_soccer','price':[200],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])
def robo_war():
    x=float(input('enter the timer: '))
    sleep(x)
    print('ok')
    notification.message = "Robo war"
    notification.send()
    
    mixer.music.play() 
    sleep(2)
def start_robo_war():
    global game_data
    t=Thread(target=robo_war)
    t.start()
    x=pd.DataFrame({'game_name':'robo_war','price':[300],'time':[str(dt.datetime.now().hour)+' : '+str(dt.datetime.now().minute)+' : '+(str(dt.datetime.now().second))]})
    game_data=pd.concat([game_data,x])


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=start_VR,
    relief="flat"
)
button_1.place(
    x=1088.0,
    y=153.0,
    width=350.0,
    height=164.0196075439453
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=start_robo_war,
    relief="flat"
)
button_2.place(
    x=5.0,
    y=153.0,
    width=350.0,
    height=171.06741333007812
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=start_machine_soccer,
    relief="flat"
)
button_3.place(
    x=5.0,
    y=396.0,
    width=350.0,
    height=159.6875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=start_human_soccer,
    relief="flat"
)
button_4.place(
    x=5.0,
    y=624.0,
    width=350.0,
    height=166.39344787597656
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=start_Hovercraft,
    relief="flat"
)
button_5.place(
    x=1085.0,
    y=400.0,
    width=350.0,
    height=152.45632934570312
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=start_little_war,
    relief="flat"
)
button_6.place(
    x=575.0,
    y=154.0,
    width=350.0,
    height=161.5
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=start_RC,
    relief="flat"
)
button_7.place(
    x=575.0,
    y=628.0,
    width=350.0,
    height=164.50677490234375
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=start_little_road,
    relief="flat"
)
button_8.place(
    x=1085.0,
    y=631.0,
    width=350.0,
    height=161.870849609375
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=start_Board_game,
    relief="flat"
)
button_9.place(
    x=577.0,
    y=396.0,
    width=350.0,
    height=155.26870727539062
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=start_one,
    relief="flat"
)
button_10.place(
    x=5.0,
    y=860.0,
    width=350.0,
    height=163.73825073242188
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=start_three,
    relief="flat"
)
button_11.place(
    x=1088.0,
    y=860.0,
    width=350.0,
    height=162.7906951904297
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=start_two,
    relief="flat"
)
button_12.place(
    x=577.0,
    y=862.0,
    width=350.0,
    height=159.11740112304688
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=5.0,
    y=0.0,
    width=1435.0,
    height=92.0
)
window.resizable(False, False)
window.mainloop()
game_list=['robo_war','machine_soccer','human_soccer','VR','Hovercraft','little_war','little_road']
game_data['game_name']=game_data['game_name'].replace(to_replace=game_list,value=range(len(game_list)))
game_data.sort_values(['game_name','time'],ascending=True,inplace=True)
game_data['game_name']=game_data['game_name'].replace(value=game_list,to_replace=range(len(game_list)))
if (isfirst_time): 
    game_data.index=range(len(game_data))
game_data.drop(game_data[game_data['game_name']=='start'].index,inplace=True)
game_data=pd.concat([game_data.drop(game_data[game_data['game_name']=='total_price'].index),pd.DataFrame({'game_name':['total_price'],'price':[game_data['price'].sum()],'time':['end']})])

game_data.to_csv('game.csv',index=False)