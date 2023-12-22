# different types of races

    # Dragonborn, Dwarf, Elf, Gnome, HalfElf, Halfing, HalfOrc, Human, Tiefling

#different types of classes
    # Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladinm Ranger, Rouge, Sourcer, Warlock, Wizard

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
        

        #add in safe guard for either ties or out of bounds numbers 

        #getting user input on the distrubution of ability scores
        #this is really clunky, how can we make this a little more automated?
        print("Please Rank The Follow Traits from Most Important [6] to least important [1]/n")
        print('Strength, Dexterity, Consitution, Intellegence, Wisdom, Charisma/n')
        Strength_Position = input("On a scale of 1 to 6, Strength is : ")
        Dexterity_Position = input("On a scale of 1 to 6, Dexterity is : ")
        Consitution_Position = input("On a scale of 1 to 6, Consitution is : ")
        Intellegence_Position = input("On a scale of 1 to 6, Intellegence is : ")
        Wisdom_Position = input("On a scale of 1 to 6, Wisdom is : ")
        Charisma_Position = input("On a scale of 1 to 6, Charisma is : ")

        Ability_Ranking = []
        Ability_Ranking[Strength_Position] = 'Strength'
        Ability_Ranking[Dexterity_Position] = 'Dexterity'
        Ability_Ranking[Consitution_Position] = 'Consitution'
        Ability_Ranking[Intellegence_Position] = 'Intellegence'
        Ability_Ranking[Wisdom_Position] = 'Wisdom'
        Ability_Ranking[Charisma_Position] = 'Charisma'
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
            self.Ability_Scores[Ability_Ranking[i]] =  Ability_Numbers[i]
        
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

        #modifiers, for now will be generic based on the main 6 skill modifiers, however, once other class traits are determined, they will change

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
         


        #saving throws are a dice roll used to reduce damage on your character and is a modifier to a dice value
        # has to be calculate after modifications
        #this is the generic, will change once the class functions are called
        self.Saving_Throws = dict()
        self.Saving_Throws['Strength'] = self.Modifiers['Strength']
        self.Saving_Throws['Dexterity'] = self.Modifiers['Dexterity']
        self.Saving_Throws['Intellegence'] = self.Modifiers['Intellegence']
        self.Saving_Throws['Wisdom'] = self.Modifiers['Wisdom']
        self.Saving_Throws['Charisma'] = self.Modifiers['Charisma'] 


        
        #This will eventually be a switch case but for now we are assuming that our player is only a barbarian
        self.Barbarian()
        
        #NEED USER INPUT FOR DETERMING OTHER MODIFIERS
        #FOR EXAMPLE BARBARIAN 
        # CHOOSES 2  Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival

        #hit points 
        self.Max_Hit_Points = self.Hit_Dice[Class] + self.Modifiers['Consitution']
        
        #Armor class is determined by the type of armor a character wears, this requires a little more leg work so we are gonna treat this as a generic feature and assume
        #all of our characters are not wearing armor
        self.Armor_Class = 10 + self.Modifiers['Dexterity']

        #adding spell casting abilites as add magical classes

        
      
    
    
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
        self.Speed = 30
        #plus 2 strength
        #plus 1 charisma

    def Dwarf(self):
        self.Ability_Scores['Consitution'] += 2
        self.Speed = 25

    def Elf(self):
        self.Ability_Scores['Dexterity'] += 2
        #plus 2 dexterity

        self.Speed = 30

    def Gnome(self) :
        #plus 2 intel
        self.Ability_Scores['Intellegence'] += 2
        self.Speed = 25


    def HalfElf(self, ability1, ability2) :
        #plus 2 charisma 
        # plus 1 to two otherf abilties
        self.Ability_Scores['Charisma'] += 2
        self.Ability_Scores[ability1] += 1
        self.Ability_Scores[ability2] += 1
        self.Speed = 30

    def Halfling(self):
        self.Ability_Scores['Dexterity'] += 2
        #+2 deterity 
        self.Speed = 25
    
    def HalfOrc(self):
        #+2 strength
        #+1 consitution
        self.Ability_Scores['Strength'] +=2
        self.Ability_Scores['Consitution'] += 1
        self.Speed = 30
    def Human(self):
        self.Ability_Scores['Strength'] +=1
        self.Ability_Scores['Consitution'] +=1
        self.Ability_Scores['Dexterity'] +=1
        self.Ability_Scores['Intellegence'] +=1
        self.Ability_Scores['Charisma'] +=1
        self.Ability_Scores['Wisdom'] +=1
        #+1 to all ability scores
        self.Speed = 30
    def Tiefling(self):
        self.Ability_Scores['Charisma'] += 2
        self.Ability_Roll['Intellegence'] += 1
        self.speed = 30

#####CLASS RELATED FUNCTIONS
  # Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladinm Ranger, Rouge, Sourcer, Warlock, Wizard

    def Barbarian(self):

        # modifing ability enhancements
        print("Please Choose 2 abilties to enhance : Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival /n")
        Choice1 = input("Choice 1 : ")
        while(Choice1 != 'Animal Handling' | 'Athletics' | 'Intimidation' | 'Nature' | 'Perception'):
            print("Error! Incorrect Input. Please try again. Remember, Case matters")
            print("Please Choose 2 abilties to enhance : Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival /n")
            Choice1 = input("Choice 1 : ")
        Choice2 = input("Choice 2 : ")
        while(Choice2 != 'Animal Handling' | 'Athletics' | 'Intimidation' | 'Nature' | 'Perception'):
            print("Error! Incorrect Input. Please try again. Remember, Case matters")
            print("Please Choose 2 abilties to enhance : Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival /n")
            Choice2 = input("Choice 2 : ")
        while(Choice1 == Choice2):
            print("Your first and second choice cannot be the same, try again")
            while(Choice2 != 'Animal Handling' | 'Athletics' | 'Intimidation' | 'Nature' | 'Perception'):
                print("Error! Incorrect Input. Please try again. Remember, Case matters")
                print("Please Choose 2 abilties to enhance : Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival /n")
                Choice2 = input("Choice 2 : ")

        self.Modifiers[Choice1] += 2
        self.Modifiers[Choice2] += 2
        self.Saving_Throws['Strength'] += 2
        self.Saving_Throws['Consitution'] += 2



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

        
    def Level_Up(self):
        #empty function for now
        #will give the ability for players to increase certain traits