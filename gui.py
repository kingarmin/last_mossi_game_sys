
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



from pathlib import Path
from threading import Thread
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,StringVar,Label
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
delay=0
game_data=pd.DataFrame({'game_name':['start'],'price':[0],'time':['start']})
if not(os.path.isfile('game.csv')):
    pd.DataFrame({'game_name':['start'],'price':[0],'time':['start']}).to_csv('game.csv')
    isfirst_time=True
else:
    game_data=pd.read_csv('game.csv')
    print(game_data)

def x(game):
    import tkinter as tk
    from tkinter import ttk
    import time
    def start_progress():
        global delay
        progress.start()
        timer_time=delay
        # Simulate a task that takes time to complete
        for i in range(101):
        # Simulate some work
            time.sleep(timer_time/100)  
            progress['value'] = i
            # Update the GUI
            root.update()  
        progress.stop()
    root = tk.Tk()
    root.title(game)
    # Create a progressbar widget
    progress = ttk.Progressbar(root, length=300,mode="determinate")
    progress.pack()

    # Button to start progress
    start_progress()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def set_delay_five():
    global delay
    delay=300
def set_delay_ten():
    global delay
    delay=600
def set_delay_15():
    global delay
    delay=900
def set_delay_20():
    global delay
    delay=1200



def get_entry_value(event):
    global delay
    delay = float(entry_1.get())*60
    print("Entry value:", delay)
def open_excel():
    os.system('game.csv')
def one():
    t=Thread(target=x,args=['one'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Three'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Two'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Board_game'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Little_road'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Little_war'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Hover_craft'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['RC_climber'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['VR'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Human_soccer'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Machine_soccer'])
    t.start()
    sleep(delay)
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
    t=Thread(target=x,args=['Robo_war'])
    t.start()
    sleep(delay)
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

window.geometry("1440x850")
window.configure(bg = "#FFFFFF")

window.title('Mositto')
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 850,
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
    x=1240.0,
    y=97.0,
    width=200.0,
    height=93.7254867553711
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
    y=94.0,
    width=200.0,
    height=97.7528076171875
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
    y=196.0,
    width=200.0,
    height=91.25
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
    y=290.0,
    width=200.0,
    height=95.08197021484375
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
    x=1240.0,
    y=196.0,
    width=200.0,
    height=87.11790466308594
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
    x=626.0,
    y=97.0,
    width=200.0,
    height=92.28571319580078
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
    x=626.0,
    y=290.0,
    width=200.0,
    height=94.00386810302734
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
    x=1240.0,
    y=287.0,
    width=200.0,
    height=92.49762725830078
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
    x=626.0,
    y=195.0,
    width=200.0,
    height=88.7249755859375
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
    y=390.0,
    width=200.0,
    height=93.56471252441406
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
    x=1240.0,
    y=385.0,
    width=200.0,
    height=93.02325439453125
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
    x=626.0,
    y=390.0,
    width=200.0,
    height=90.92423248291016
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=open_excel,
    relief="flat"
)
button_13.place(
    x=5.0,
    y=0.0,
    width=1435.0,
    height=92.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    720.0,
    507.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=0.0,
    y=490.0,
    width=1440.0,
    height=33.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=set_delay_ten,
    relief="flat"
)
button_14.place(
    x=443.0,
    y=530.0,
    width=200.0,
    height=95.68106079101562
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=set_delay_15,
    relief="flat"
)
button_15.place(
    x=728.0,
    y=530.0,
    width=200.0,
    height=98.02631378173828
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=set_delay_20,
    relief="flat"
)
button_16.place(
    x=1013.0,
    y=535.0,
    width=200.0,
    height=93.37748718261719
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=set_delay_five,
    relief="flat"
)
button_17.place(
    x=155.0,
    y=530.0,
    width=200.0,
    height=88.90469360351562
)
entry_1.bind("<Return>",get_entry_value)
window.resizable(False, False)
window.mainloop()
game_list=['robo_war','machine_soccer','human_soccer','VR','Hovercraft','little_war','little_road']
game_counter_list=['robo_war_count','machine_soccer_count','human_soccer_count','VR_count','Hovercraft_count','little_war_count','little_road_count']
game_data['game_name']=game_data['game_name'].replace(to_replace=game_list,value=range(len(game_list)))
game_data.sort_values(['game_name','time'],ascending=True,inplace=True)
game_data['game_name']=game_data['game_name'].replace(value=game_list,to_replace=range(len(game_list)))
if (isfirst_time): 
    game_data.index=range(len(game_data))
game_data.drop(game_data[game_data['game_name']=='start'].index,inplace=True)
game_data=pd.concat([game_data.drop(game_data[game_data['game_name']=='total_price'].index),pd.DataFrame({'game_name':['total_price'],'price':[game_data['price'].sum()],'time':['end']})])
game_data=game_data.drop(game_data[game_data['game_name'].isin(game_counter_list)].index)
alpha=game_data['game_name'].value_counts()
xx=alpha.index.tolist()
for i in range(len(xx)):
    xx[i]=xx[i].replace(xx[i],xx[i]+'_count')
beta=pd.DataFrame({'game_name':xx , 'price':alpha.to_list() })
game_data=pd.concat([game_data,beta])
game_data.drop(game_data[game_data['game_name']=='total_price_count'].index,inplace=True)
game_data.to_csv('game.csv',index=False)