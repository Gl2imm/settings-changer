import os
import shutil
import webbrowser
import tkinter as tk
from tkinter import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


ws = Tk()
ws.title('Cfg Changer  ||  By: @Djurik')
#ws.geometry('350x190')
ws.resizable(False, False)
ws.iconbitmap(resource_path("Eagle_33892.ico"))

window_width = 350
window_height = 180
ws.config(bg='#000000') #F2B90C

# get the screen dimension
screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
ws.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# Background
bg= tk.PhotoImage(file=resource_path("bg.png"))
labe_bg = Label( ws, image = bg)
labe_bg.place(x = 0, y = 0)

# configure the grid
ws.columnconfigure(0, weight=2)
ws.columnconfigure(1, weight=1)
ws.columnconfigure(2, weight=2)
ws.columnconfigure(3, weight=1)
ws.rowconfigure(0, weight=2)
ws.rowconfigure(1, weight=2)
ws.rowconfigure(2, weight=2)
ws.rowconfigure(3, weight=1)
ws.rowconfigure(4, weight=1)


message3 = tk.Label(ws, text="Select cofig and press Transfer", bg="#FFFFFF", width="50")
message3.grid(column=0, row=3, columnspan=4, sticky=tk.S, padx=5, pady=5)

# backup current config
try:
    with open("Profiles/Original_profile.cfg", 'r') as file:
        file = file.read()
except OSError as e:
    if e.errno == 2:
        shutil.copyfile(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "Profiles/Original_profile.cfg")
        message = tk.Label(ws, text="Original CFG has been Backed up (Profiles/Original_profile.cfg)", bg="#FFFFFF", width="50")
        #message.pack()
        #message.place(x=0,y=130)
        message.grid(column=0, row=3, columnspan=4, sticky=tk.S, padx=5, pady=5)


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
#dropdown.pack(expand=True)
#dropdown.place(x=110,y=30)
dropdown.grid(column=0, row=0, columnspan=4, sticky=tk.W, padx=27, pady=5)



def restore():
    shutil.copyfile("Profiles/Original_profile.cfg", os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg")
    message1 = tk.Label(ws, text="Original CFG has been Restored...", bg="#FFFFFF", width="50")
    #message1.pack()
    #message1.place(x=0,y=130)
    message1.grid(column=0, row=3, columnspan=4, sticky=tk.S, padx=5, pady=5)

def save():
    shutil.copyfile(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "Profiles/Saved_profile.cfg")
    message1 = tk.Label(ws, text="Current CFG has been Saved (Profiles/Saved_profile.cfg)", bg="#FFFFFF", width="50")
    #message1.pack()
    #message1.place(x=0,y=130)
    message1.grid(column=0, row=3, columnspan=4, sticky=tk.S, padx=5, pady=5)

def transfer():
    a_file = open(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "r")
    list_of_lines = a_file.readlines()
    a_file.close()

    shutil.copyfile(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "Profiles/My_Profile.cfg")

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
    list_of_lines[59] = new_cfg[59] #Look Deadzone
    list_of_lines[60] = new_cfg[60] #Movement Deadzone
    list_of_lines[61] = new_cfg[61] #Response Curve
    list_of_lines[66] = new_cfg[66] #Trigger Deadzones
    a_file.close()

    a_file = open(os.environ['USERPROFILE'] + "\Saved Games\Respawn\Apex\profile\profile.cfg", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

    message = tk.Label(ws, text=variable.get() + " - Transfer Complete...", bg="#FFFFFF", width="50")
    #message.pack()
    #message.place(x=0,y=130)
    message.grid(column=0, row=3, columnspan=4, sticky=tk.S, padx=5, pady=5)


# Transfer button
#transf_image= tk.PhotoImage(file='./assets/transfer.png')
transfer_button = tk.Button(
    ws,
    text='Transfer Settings',
    relief=RAISED,
    #image=transf_image,
    #compound=tk.LEFT,
    cursor="hand2",
    command=transfer,
)


#transfer_button.pack()
#transfer_button.place(x=60,y=90)
transfer_button.grid(column=0, row=1, columnspan=2, sticky=tk.S, padx=5, pady=5)


#transfer Button Color
def on_enter(e):
    transfer_button['background'] = '#FF9900'

def on_leave(e):
    transfer_button['background'] = 'SystemButtonFace'

transfer_button.bind("<Enter>", on_enter)
transfer_button.bind("<Leave>", on_leave)


# Save button
#rest_image= tk.PhotoImage(file='./assets/restore.png')
save_button = tk.Button(
    ws,
    text='Save Current .cfg',
    #image=rest_image,
    #compound=tk.LEFT,
    cursor="hand2",
    command=save
)
save_button.grid(column=2, row=1, columnspan=2, sticky=tk.S, padx=5, pady=5)

#Save Button Color
def on_enter(e):
    save_button['background'] = '#FF9900'

def on_leave(e):
    save_button['background'] = 'SystemButtonFace'

save_button.bind("<Enter>", on_enter)
save_button.bind("<Leave>", on_leave)



# Restore button
#rest_image= tk.PhotoImage(file='./assets/restore.png')
restore_button = tk.Button(
    ws,
    text='Restore Original .cfg',
    #image=rest_image,
    #compound=tk.LEFT,
    cursor="hand2",
    command=restore
)
#restore_button.pack()
#restore_button.place(x=200,y=90)
restore_button.grid(column=0, row=2, columnspan=4, sticky=tk.S, padx=5, pady=5)


#Restore Button Color
def on_enter(e):
    restore_button['background'] = '#FF9900'

def on_leave(e):
    restore_button['background'] = 'SystemButtonFace'

restore_button.bind("<Enter>", on_enter)
restore_button.bind("<Leave>", on_leave)


# Discord Link
def link(url):
    webbrowser.open_new(url)

dc_image= tk.PhotoImage(file=resource_path("dc.png"))
link1 = Label(ws, text=" Join XIM Settings Discord (unofficial)", image=dc_image, compound=tk.LEFT, fg="white", bg="#000000", cursor="hand2")
#link1.pack()
link1.bind("<Button-1>", lambda e: link("https://discord.gg/rZAHr9BJw7"))
#link1.place(x=20, y=156)
link1.grid(column=0, row=4, columnspan=3, sticky=tk.SW, padx=5, pady=5)

#Link Color
def on_enter(e):
    link1['foreground'] = '#F2B90C'

def on_leave(e):
    link1['foreground'] = 'white'

link1.bind("<Enter>", on_enter)
link1.bind("<Leave>", on_leave)


ver = tk.Label(ws, text="v1.1", font=("Arial", 8), fg="white", bg="#000000", cursor="hand2")
ver.bind("<Button-1>", lambda e: link("https://github.com/Gl2imm/settings-changer"))
ver.grid(column=3, row=4, sticky=tk.S, padx=5, pady=5)

#Link Color
def on_enter(e):
    ver['foreground'] = '#F2B90C'

def on_leave(e):
    ver['foreground'] = 'white'

ver.bind("<Enter>", on_enter)
ver.bind("<Leave>", on_leave)

# infinite loop 
ws.mainloop()
