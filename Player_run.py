# going to create a basic file where a user can keep track of there stats 

#scope for now 
    # user is able to set up there charater, and user the dice roll function to calculate runs 
    # user will have the ability to roll for different things like "intellegence" and get automatic scoring
    # user will be able to load stats from previously saved file
    # user will be able to "Level Up", this is done manually for now

#scope later
    # user will be able to play based on race, subclasses of the file will help run the game from a level upstandpoint
    # user will have the GUI interface that allows them to run things with the click of a button
    
#scope last
    # sever hosting ability
    #DM can interconnect will all users and request them to roll, it can project images to the users
    # game maps are live on screen and show where everyone is individually 
    # DM can control certain aspects of what is happening to the players like dispell hit points based on enemies 

import random as rd

#from Class_Race_Set_Up import Player_Define
import tkinter as tk
from tkinter import ttk



def set_dragborn():

    Race.set('DragonBorn')

def set_elf():
    Race.set('Elf')
    
def set_halfling():
    Race.set('Halfling')
    
def set_gnome():
    Race.set('Gnome')
    
def set_halforc():
    Race.set('HalfOrc')
    
def set_halfelf():
    Race.set('HalfElf')

def set_human():
    Race.set('Human')
    
def set_tief():
    Race.set('Teifling')
    
def set_dwarf():
    Race.set('Dwarf')



#establishing Tk window
window = tk.Tk()
#give the window TK as name
window.title('D and D Player Run')
#establish size of window
window.geometry('500x300')

#creating widget
title_label = ttk.Label(master = window, text = 'Please Select A Race : ', font= 'Calibri 24')
title_label.pack()


#input field example
input_frame = ttk.Frame(master=window)
lower_input_frame = ttk.Frame(master=window)


#buttons containing different races

DrgBorn = ttk.Button(master = input_frame, text = 'DragonBorn', command = set_dragborn)
Elf = ttk.Button(master = input_frame, text = 'Elf', command = set_elf)
Halfling = ttk.Button(master = input_frame, text = 'Halfing', command = set_halfling)
HalfElf = ttk.Button(master = input_frame, text = 'Half-Elf', command = set_halfelf)
Gnome = ttk.Button(master = lower_input_frame, text = 'Gnome', command = set_gnome)
HalfOrc = ttk.Button(master = lower_input_frame, text = 'Half-Orc', command = set_halforc)
Human = ttk.Button(master = lower_input_frame, text = 'Human', command = set_human)
Tiefling = ttk.Button(master = lower_input_frame, text = 'Tiefling', command = set_tief)
Dwarf = ttk.Button(master = lower_input_frame, text = 'Dwarf', command = set_dwarf)



#puts the entry field and button inside input frame box
DrgBorn.pack(side = 'left')
Elf.pack(side = 'left')
Halfling.pack(side = 'left')
HalfElf.pack(side = 'left')

Gnome.pack(side = 'left')
HalfOrc.pack(side = 'left')
Human.pack(side = 'left')
Tiefling.pack(side = 'left')
Dwarf.pack(side = 'left')

#puts input frame box in overall window
input_frame.pack(pady = 10)
lower_input_frame.pack()

#output

Race = tk.StringVar()
output_label = ttk.Label(
    master = window,
    text = 'Race :',
    font = 'Calibri 24',
    textvariable= Race) 
                       
output_label.pack(pady = 5)


#where we run the mainloop of the function
window.mainloop()
