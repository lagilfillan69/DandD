import random as rd

class Dice :
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
