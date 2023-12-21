# different types of races



#different types of classes

#function to convert actual spelling of class to numberical value to allow 
#set up to be easier 

from dice_roll import Dice


class Player_Define :


    Hit_Dice = {'Barbarian' : 12, 'Bard' : 8, 'Cleric' : 8, 'Druid' : 8, 'Fighter' : 10, 'Monk' : 8, 
                'Paladin' : 10, 'Ranger' : 10, 'Rouge' : 8, 'Sorcerer' : 6, 'Warlock' : '8', 'Wizard' : 6}
    
    Class_Modifiers = {}
    Race_Modifiers = {'Dragonborn' : {}, 'Dwarf' : {}, 'Elf' : {}, 'Gnome' : {}, 'HalfElf' : {}, 'Halfling' : {}, 'HalfOrc' : {}, 'Human' : {}, 'Tiefling' : {}}

    Race_Modifier_Data = { ('Dragonborn',  'Strength') : 0,
                           ('Dragonborn',  'Dexterity') : 0,
                           ('Dragonborn',  'Consitution') : 0,
                           ('Dragonborn',  'Intellegence') : 0,
                           ('Dragonborn',  'Wisdom') : 0,
                           ('Dragonborn',  'Charisma') : 0,


                           
                           
                           
                           
                           
                           }
    
    
    def __init__(self,Class,Race):
        #class and race for internal use
        self.Class = Class
        self.Race = Race
       #pre establish dictionary for ability scores and hit dice
        self.Ability_Scores = dict()
        
        
        # have user rank their traits from most important to least        
        # list should come out like...
        remove_later_list = ['Strength','Dexterity','Consitution','Intellegence','Wisdom','Charisma']
        #where the least important trait is listed first, and most important trait is listed last

        # getting randomize ability score numbers
        Ability_Numbers = []
        for i in range(0,3):
            Ability_Numbers[i] = self.Ability_Roll()
        #sort from lowest to highest
        Ability_Numbers.sort()

        self.Ability_Scores = dict()
        # assigning ability scores based on preferences
        for j in range(0,5) :
            self.Ability_Scores[remove_later_list[i]] =  Ability_Numbers[i]
        
        #add race adjustments
        match Race: 
            case 'Dragonborn':
                self.Dragonborn()
            case 'Dwarf' :
                self.Dwarf()
            case 'Elf' :
                self.Elf()
            case 'Gnome':
                self.Gnome()
            case 'HalfElf' :
                self.HalfElf(Ability_Numbers[0], Ability_Numbers[1])
            case 'Halfling' :
                self.Halfling
            case 'HalfOrc' :
                self.HalfOrc()
            case 'Human' :
                self.Human()
            case 'Tiefling':
                self.Tiefling()
        
        
        #now using the ability scores we can calculate the ability modifiers


        #create dicitonary to find 50 million modieiers
        self.Modifiers = dict()

        # strength based modifications
        #add ifs to calculte based on class
        str_mod = self.Calculate_Modifier_Value(self.Ability_Scores['Strength'])
        self.Modifiers['Strength'] = str_mod
        self.Modifiers['Athlectics'] = str_mod
     
        #deterixty based modication
        dex_mod = self.Calculate_Modifier_Value(self.Ability_Scores['Dexterity'])
        self.Modifiers['Dexterity'] = dex_mod
        self.Modifiers['Acrobatics'] = dex_mod
        self.Modifiers['Sleight of Hand'] = dex_mod
        self.Modifiers['Stealth'] = dex_mod
        
        #consitution based modifications
        con_mod = self.Calculate_Modifier_Value(self.Ability_Scores['Consitution'])
        self.Modifiers['Consitution'] = con_mod

        #Intellegency based modification
        int_mod = self.Calculate_Modifier_Value(self.Ability_Scores['Intellegence'])
        self.Modifiers['Intellegence'] = int_mod
        self.Modifiers['Arcana'] = int_mod
        self.Modifiers['History'] = int_mod
        self.Modifiers['Nature'] = int_mod
        self.Modifiers['Religion'] = int_mod
        self.Modifiers['Investigation'] = int_mod

        #wisdom based modofication
        wis_mod = self.Calculate_Modifier_Value(self.Ability_Scores['Wisdom'])
        self.Modifiers['Wisdom'] = wis_mod
        self.Modifiers['Animal_Handling'] = wis_mod
        self.Modifiers['Insight'] = wis_mod
        self.Modifiers['Medicine'] = wis_mod
        self.Modifiers['Perception'] = wis_mod
        self.Modifiers['Survival_Bonus'] = wis_mod
    
        #charisma based modification
        char_mod = self.Calculate_Modifier_Value(self.Ability_Scores['Charisma'])
        self.Modifiers['Charisma'] = char_mod
        self.Modifiers['Deception'] = char_mod
        self.Modifiers['Intimidation'] = char_mod
        self.Modifiers['Performance'] = char_mod
        self.Modifiers['Persuasion'] = char_mod
         
        #hit points 
        self.Max_Hit_Points = self.Hit_Dice[Class] + self.Modifiers['Consitution']
        #need user input on this?
        self.Armor_Class = 0

        #spell casters only
        self.Spell_Casting_Ability = 0;
        self.Spell_Save_DC = 0;
        self.Spell_Attack_Bonus = 0;
        
        #random stuff
        self.Speed = 0;
        self.Initative = 0;
    
        #saving throws - based on class
        Saving_Throws = dict()
        #self.Strength_Saving_Throw = 0;
        #self.Dexterity_Saving_Throw = 0;
        #sekfConsitution_Saving_Throw  = 0;
        #Intellegence_Saving_Throw = 0;
        #Wisdom_Saving_Throw = 0;
        #Charisma_Saving_Throw  = 0; 
    
    
    #roll 4 times and combine the highest three
    def Ability_Roll(self):
        ability = []
        for i in range(0,3):  
            ability[i] = Dice.roll_dice(dice_type = 6)
        ability.sort()
        return(ability[1]+ability[2]+ability[3])
    


    # Different Race Modifications -- might get rid of these, they are too small
    def Dragonborn(self):
        self.Ability_Scores['Strength'] += 2
        self.Ability_Scores['Charisma'] += 1
        #plus 2 strength
        #plus 1 charisma

    def Dwarf(self):
        self.Ability_Scores['Consitution'] += 2

    def Elf(self):
        self.Ability_Scores['Dexterity'] += 2
        #plus 2 dexterity

    def Gnome(self) :
        #plus 2 intel
        self.Ability_Scores['Intellegence'] += 2

    def HalfElf(self, ability1, ability2) :
        #plus 2 charisma 
        # plus 1 to two otherf abilties
        self.Ability_Scores['Charisma'] += 2
        self.Ability_Scores[ability1] += 1
        self.Ability_Scores[ability2] += 1

    def Halfling(self):
        self.Ability_Scores['Dexterity'] += 2
        #+2 deterity 
    
    def HalfOrc(self):
        #+2 strength
        #+1 consitution
        self.Ability_Scores['Strength'] +=2
        self.Ability_Scores['Consitution'] += 1
    
    def Human(self):
        self.Ability_Scores['Strength'] +=1
        self.Ability_Scores['Consitution'] +=1
        self.Ability_Scores['Dexterity'] +=1
        self.Ability_Scores['Intellegence'] +=1
        self.Ability_Scores['Charisma'] +=1
        self.Ability_Scores['Wisdom'] +=1
        #+1 to all ability scores

    def Tiefling(self):
        self.Ability_Scores['Charisma'] += 2
        self.Ability_Roll['Intellegence'] += 1

        #and modify modifiers

        
        #calculation ability modifiers 

    def Calculate_Modifier_Value(self,score) :
        if score == 1 : 
            return -5
        elif score == 2 or score == 3:
            return -4
        elif score == 4 or score == 5:
            return -3
        elif score == 6 or score == 7:
            return -2 
        elif score == 8 or score == 9:
            return -1 
        elif score == 10 or score ==11:
            return 0
        elif score == 12 or score == 13 :
            return 1
        elif score == 14 or score == 15 :
            return 2
        elif score == 16 or score == 17:
            return 3
        elif score == 18 or score == 19:
            return 4
        elif score == 20 or score == 21 :
            return 5
        elif score == 22 or score == 23 :
            return 6
        elif score == 24 or score == 25:
            return 7
        elif score == 26 or score == 27:
            return 8
        elif score == 28 or score == 29:
            return 9
        elif score == 30 :
            return 10
        
    def Get_Modifiers(self) :
        #add safe guard if race and class arent chosen
        return self.Modifiers
    
    def Get_Ability_Scores(self) :
        #add safe guard if race and class arent chose
        return self.Ability_Scores

        


# nested loop code 
#taken from stack overflow

class Vividict(dict):
    def __missing__(self, key):
        value = self[key] = type(self)() # retain local pointer to value
        return value                     # faster to return than dict lookup
    

#usage code

#vividict = Vividict()
#for (state, county, occupation), number in data.items():
    #vividict[state][county][occupation] = number
