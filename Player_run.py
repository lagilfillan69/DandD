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

from Class_Race_Set_Up import Player_Define
import tkinter as tk
from tkinter import ttk

#establishing Tk window
window = tk.TK()
#give the window TK as name
window.titles('D and D Player Run')
#establish size of window
window.geometry('300x150')

#creating widget
title_label = ttk.Label(master = window, text = "D and D", font = 'Calibri 24 bold')
title_label.pack()

#input field example
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Create Character', command = function_name)

#puts the entry field and button inside input frame box
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')

#puts input frame box in overall window
input_frame.pack(pady = 10)

#output
output_label = ttk.Label(master = window)
output_label.pack(pady = 5)





#where we run the mainloop of the function
window.mainloop()




class Player_Run:

    def Character_Create():
        print("Please enter your chosen race")




 # allows user to select wether or not they want to play with dice
  Dice = False;






#randomize dice function for each



    def roll_dice(Disadvantage = False, Advantage = False, dice_type = 20):
        if Disadvantage == True : # lower dice gets returned
            roll1 = rd.randrange(1,dice_type)
            roll2 = rd.randrange(1,dice_type)
            if roll1 < roll2 :
                return roll1
            else :
                return roll2
            

        elif Advantage == True : #higher roll gets returned 
            roll1 = rd.randrange(1,dice_type)
            roll2 = rd.randrange(1,dice_type)
            if roll1 > roll2 :
                return roll1
            else :
                return roll2
            
        else : #regular 1 dice roll
            roll = rd.randrange(1,dice_type)
            return roll
