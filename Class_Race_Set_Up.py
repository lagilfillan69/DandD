# different types of races



#different types of classes

#function to convert actual spelling of class to numberical value to allow 
#set up to be easier 

from dice_roll import Dice

class Player_Define :
    #turn these into dictonaries
    
    Ability_Scores = dict()
    
    def __init__(self,Class,Race):
        Class = Class
        Race = Race
       
        #ability scores

        #turn these into dictonaries
        Ability_Scores = dict()

        Strength_Score = 0
        Dexterity_Score = 0
        Consitution_Score = 0
        Intellegence_Score = 0
        Wisdom_Score = 0
        Charisma_Score = 0
        Perception_Score = 0


        #throw bonuses
        Strength_Modifier = 0;
        Dexterity_Modifier = 0;
        Consitution_Modifier = 0;
        Intellegence_Modifier = 0;
        Wisdom_Modifier = 0;
        Charisma_Modifier = 0;
        Consitution_Modifier = 0;
       
        #action modifieres
        Acrobatics_Modifier = 0;
        Animal_Handling_Modifier = 0;
        Arcana_Modifier = 0;
        Athletics_Modifier = 0;
        Deception_Modifier = 0;
        History_Modifier = 0;
        Insight_Modifier = 0;
        Intimidation_Modifier = 0;
        Investigation_Modifier = 0;
        Medicine_Modifier = 0;
        Nature_Modifier = 0;
        Perception_Modifier = 0;
        Performance_Modifier = 0;
        Persuasion_Modifier = 0;
        Religion_Modifier = 0;
        Sleight_of_Hand_Modifier = 0;
        Stealth_Bonus = 0;
        Survival_Bonus = 0;


        #hit points 
        Max_Hit_Points = 0
        Armor_Class = 0;

        #spell casters only
        Spell_Casting_Ability = 0;
        Spell_Save_DC = 0;
        Spell_Attack_Bonus = 0;
        
        #random stuff
        Speed = 0;
        Initative = 0;
    
        #saving throws 
        Strength_Saving_Throw = 0;
        Dexterity_Saving_Throw = 0;
        Consitution_Saving_Throw  = 0;
        Intellegence_Saving_Throw = 0;
        Wisdom_Saving_Throw = 0;
        Charisma_Saving_Throw  = 0; 
    
    

    def Abililty_Roll(self):
        ability = []
        for i in range(0,3):  
            ability[i] = Dice.roll_dice(dice_type = 6)
        ability.sort()
        return(ability[1]+ability[2]+ability[3])
    

    def Tiefling(self):
        #add tiefling description 

        Speed = 30 # tiefling speed

        # set ability scores

        Ability_Scores['Strength'] = Abililty_Roll()

        Strength_Score =  Abililty_Roll()
        Dexterity_Score = Abililty_Roll()
        Consitution_Score = Abililty_Roll()
        Intellegence_Score = Abilility_Roll() + 1
        Wisdom_Score = Ability_Roll()
        Charisma_Score = Abilility_Roll() + 2
        Perception_Score = Abilility_Roll()

        #calculation ability modifiers 




