import os
import shutil
import webbrowser
import tkinter as tk
from tkinter import *


ws = Tk()
ws.title('From Djurik')
#ws.geometry('350x190')
ws.resizable(False, False)
ws.iconbitmap('./assets/Eagle_33892.ico')

window_width = 350
window_height = 180
ws.config(bg='#F2B90C')

# get the screen dimension
screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
ws.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# backup current config
try:
    with open("Profiles/My_profile.cfg", 'r') as file:
        file = file.read()
except OSError as e:
    if e.errno == 2:
        shutil.copyfile(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "Profiles/My_profile.cfg")
        message = tk.Label(ws, text="Original CFG has been Backed up (Profiles - My_profile.cfg)", bg="#F2B90C", width="50")
        message.pack()
        message.place(x=0,y=130)


cfg_list = os.listdir('Profiles/')


def display_selected(choice):
    choice = variable.get()
    print(choice)


cfgs = cfg_list


# setting variable for Integers
variable = StringVar()
variable.set("Select Config")


# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *cfgs,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)
dropdown.place(x=110,y=30)


def restore():
    shutil.copyfile("Profiles/My_profile.cfg", os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg")
    message1 = tk.Label(ws, text="Original CFG has been Restored...", bg="#F2B90C", width="50")
    message1.pack()
    message1.place(x=0,y=130)

def transfer():
    a_file = open(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "r")
    list_of_lines = a_file.readlines()
    a_file.close()

    shutil.copyfile(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "Profiles/My_Profile.cfg")

    '''
    username = input("Enter username:")
    username = "Djurik"
    '''

    a_file = open("Profiles/" + variable.get(), "r")
    new_cfg = a_file.readlines()
    

    list_of_lines[15] = new_cfg[15]
    list_of_lines[16] = new_cfg[16]
    list_of_lines[17] = new_cfg[17]
    list_of_lines[18] = new_cfg[18]
    list_of_lines[19] = new_cfg[19]
    list_of_lines[20] = new_cfg[20]
    list_of_lines[21] = new_cfg[21]
    list_of_lines[22] = new_cfg[22]
    list_of_lines[28] = new_cfg[28] #Senses
    list_of_lines[29] = new_cfg[29] #Senses ADS
    list_of_lines[39] = new_cfg[39]
    list_of_lines[40] = new_cfg[40]
    list_of_lines[41] = new_cfg[41]
    list_of_lines[42] = new_cfg[42]
    list_of_lines[43] = new_cfg[43]
    list_of_lines[44] = new_cfg[44]
    list_of_lines[45] = new_cfg[45]
    list_of_lines[46] = new_cfg[46]
    list_of_lines[47] = new_cfg[47]
    list_of_lines[48] = new_cfg[48]
    list_of_lines[49] = new_cfg[49]
    list_of_lines[50] = new_cfg[50] #ALC On/Off
    list_of_lines[51] = new_cfg[51]
    list_of_lines[52] = new_cfg[52]
    list_of_lines[53] = new_cfg[53]
    list_of_lines[54] = new_cfg[54]
    list_of_lines[55] = new_cfg[55]
    list_of_lines[56] = new_cfg[56]
    list_of_lines[57] = new_cfg[57]
    list_of_lines[59] = new_cfg[59] #Look Deadzone
    list_of_lines[60] = new_cfg[60] #Movement Deadzone
    list_of_lines[61] = new_cfg[61] #Response Curve
    list_of_lines[66] = new_cfg[66] #Trigger Deadzones
    a_file.close()

    a_file = open(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

    message = tk.Label(ws, text="Transfer Complete...", bg="#F2B90C", width="50")
    message.pack()
    message.place(x=0,y=130)

'''
    state="disabled"

'''

# Transfer button
transfer_button = tk.Button(
    ws,
    text='Transfer Settings',
    command=transfer,
)


transfer_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
transfer_button.place(x=60,y=90)


# Restore button
restore_button = tk.Button(
    ws,
    text='Restore Original .cfg',
    command=restore
)
restore_button.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
restore_button.place(x=200,y=90)

# Discord Link
def discord(url):
    webbrowser.open_new(url)

link1 = Label(ws, text="Join XIM Settings Discord (unofficial)", fg="blue", bg="#F2B90C", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: discord("https://discord.gg/rZAHr9BJw7"))
link1.place(x=10, y=160)


# infinite loop 
ws.mainloop()

