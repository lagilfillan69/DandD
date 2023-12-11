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
    #DM can interconnect will all users and request them to roll, it can project images to the users
    # game maps are live on screen and show where everyone is individually 
    # DM can control certain aspects of what is happening to the players like dispell hit points based on enemies 

import random as rd


class Player_Run:

#basic user stats that the user will input
  Level = 0
  Hit_Points = 0
  Max_Hit_Points = 0
  Cantrip_Slots = 0
  Spell_Slots = 0
  Class = ""
  Race = ""


 # allows user to select wether or not they want to play with dice
  Dice = False = 0;


    __init__():
        




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
            roll = rd.randrange(1,dicetype)
            return roll
