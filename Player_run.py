import tkinter as tk
from tkinter import ttk
from Class_Race_Set_Up import Player_Define


LARGEFONT =("Verdana", 35)

Race = ''
Class = ''

class D_and_D_App(tk.Tk) :
   
    def __init__(self, *args, **kwargs) :
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        #creating a container 
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #initialzing frames to an empty array
        self.frames = {}

        # iterating through differnt pages

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")


        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        #selection varibles
        self.Race = tk.StringVar()
        self.Class = tk.StringVar()

        #creating TK frame
        tk.Frame.__init__(self, parent)
        title_label = ttk.Label(self, text = 'Please Select A Race :', font = 'Calibri 24')
        title_label.pack()

        #creating widgets to hold buttons
        race_top = ttk.Frame(master = self)
        race_lower = ttk.Frame(master = self)
        class_top = ttk.Frame(master = self)
        class_lower = ttk.Frame(master = self)
        
        #creating selection buttons for race
        DB = ttk.Button(master = race_top, text = 'DragonBorn', command = self.set_dragonborn)
        ELF = ttk.Button(master = race_top, text = 'Elf', command = self.set_elf)
        HL = ttk.Button(master = race_top, text = 'Halfling', command = self.set_halfling)
        HE = ttk.Button(master = race_top, text = 'HalfElf', command = self.set_halfelf)
        GN = ttk.Button(master = race_top, text = 'Gnome', command = self.set_gnome)
        HO = ttk.Button(master = race_lower, text = 'HalfOrc', command = self.set_halforc)
        HM = ttk.Button(master = race_lower, text = 'Human', command = self.set_human)
        TF = ttk.Button(master = race_lower, text = 'Tiefling', command = self.set_tief)
        DW = ttk.Button(master = race_lower, text = 'Dwarf', command = self.set_dwarf)
        
        #packing buttonbs for race
        DB.pack(side='left')
        ELF.pack(side='left')
        HL.pack(side='left')
        HE.pack(side='left')
        GN.pack(side='left')
        HO.pack(side='left')
        HM.pack(side='left')
        TF.pack(side='left')
        TF.pack(side='left')
        DW.pack(side='left')
        race_top.pack()
        race_lower.pack()

        # output of class selection
        race_output = ttk.Frame(master=self)
        Race_pre_label = ttk.Label(master = race_output, text = 'Race Selected: ',font =  'Calibri 16')
        Race_label = ttk.Label(master = race_output,
            text = 'Race :',
            font =  'Calibri 16',
            textvariable= self.Race) 
        Race_pre_label.pack(side='left')
        Race_label.pack(side = 'left')
       
        race_output.pack(pady=10)

        # label for class selection
        title_label = ttk.Label(self, text = 'Please Select A Class :', font='Calibri 24')
        title_label.pack() 

        #creating selection button for class
        BB = ttk.Button(master = class_top, text = 'Barbarian', command = self.set_barbarian)
        BB.pack(side = 'top')
        class_top.pack()

        #Class output
        class_output = ttk.Frame(master=self)
        Class_pre_label = ttk.Label(master=class_output,text = 'Class Selected : ', font = 'Calibri 16')
        Class_label = ttk.Label(master = class_output,
            text = '',
            font =  'Calibri 16',
            textvariable= self.Class) 
        Class_pre_label.pack(side = 'left')
        Class_label.pack(side = 'left')
        class_output.pack(pady=10)

        #transition to next page 
        Finish = ttk.Button(self, text ="Create Character",
							command = lambda : controller.show_frame(Page1))
        Finish.pack()
        Race = self.Race
        Class = self.Class
        
	

    def set_dragonborn(self):
        self.Race.set('DragonBorn')
	
    def set_elf(self):
        self.Race.set('Elf')
        
    def set_halfling(self): 
        self.Race.set('Halfling')
	
    def set_gnome(self):
        self.Race.set('Gnome')
        
    def set_halforc(self):
        self.Race.set('HalfOrc')
        
    def set_halfelf(self):
        self.Race.set('HalfElf')
        
    def set_human(self):
        self.Race.set('Human')
        
    def set_tief(self):
        self.Race.set('Teifling')
        
    def set_dwarf(self):
        self.Race.set('Dwarf')

    def set_barbarian(self):
        self.Class.set("Barbarian")



class Page1(tk.Frame): 
    # right now we are only assuming the creation of a barbarian creature

    

    def __init__(self,parent,controller):

        self.Prof1 = ""
        self.Prof2 = ""

        Char = Player_Define(Class,Race)
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Chose two profiencies : ", font = LARGEFONT)
        
        select_top = ttk.Frame(master = self)
        AH= ttk.Button(master = select_top, text = "Animal Handling" , command = self.set_prof("Animal Handling") )
        At = ttk.Button(master = select_top, text = "Athletics", command = )
        Int = ttk.Button(master = select_top, text = "Intimidation", command = )
        HE = ttk.Button(master = select_top, text = 'Delete', command = self.set_prof(""))
        
    
        # pack this
        hitdice = ttk.Label(self, text = "Hit Dice : " & str(Char.Get_Hit_Points()))




		# button to show frame 2 with text
		# layout2
        button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
        button2 = ttk.Button(self, text ="C",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
    def set_proficency(self,new_prof):
        if (len(self.Prof1) != 0) :
            self.Prof2 = new_prof
        elif(len(self.Prof1) == 0) :
            self.Prof1 = new_prof      




# third window frame page2
class Page2(tk.Frame): 
	def __init__(self, parent, controller):
                
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Page 1",
							command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by 
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = D_and_D_App()
app.mainloop()




import tkinter as tk
from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master):
        self.frame1 = Frame(root, width=300, height=300)
        self.frame1.pack()
        self.reg_txt = ttk.Label(root, text='page1')
        self.reg_txt.place(x=88, y=30)
class app2:
    def __init__(self, master):
        self.frame2 = Frame(root, width=300, height=300)
        self.reg_txt2 = ttk.Label(root, text='page2')
        self.reg_txt2.place(x=88, y=30)
        self.frame2.pack()
    
root = Tk()
a = app(root)
a = app2(root)
root.mainloop()