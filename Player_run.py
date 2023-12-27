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
'''
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


'''

import tkinter as tk
from tkinter import ttk




LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		Race = tk.StringVar()
		tk.Frame.__init__(self, parent)
		title_label = ttk.Label(self, text = 'Please Select A Race : ', font= 'Calibri 24')
		title_label.pack() 
		input_frame = ttk.Frame(self)
		lower_input_frame = ttk.Frame(master=self)
		DrgBorn = ttk.Button(master = input_frame, text = 'DragonBorn', command = self.set_dragborn)
		Elf = ttk.Button(master = input_frame, text = 'Elf', command = self.set_elf)
		Halfling = ttk.Button(master = input_frame, text = 'Halfing', command = self.set_halfling)
		HalfElf = ttk.Button(master = input_frame, text = 'Half-Elf', command = self.set_halfelf)
		Gnome = ttk.Button(master = lower_input_frame, text = 'Gnome', command = self.set_gnome)
		HalfOrc = ttk.Button(master = lower_input_frame, text = 'Half-Orc', command = self.set_halforc)
		Human = ttk.Button(master = lower_input_frame, text = 'Human', command = self.set_human)
		Tiefling = ttk.Button(master = lower_input_frame, text = 'Tiefling', command = self.set_tief)
		Dwarf = ttk.Button(master = lower_input_frame, text = 'Dwarf', command = self.set_dwarf)
		DrgBorn.pack(side = 'left')
		Elf.pack(side = 'left')
		Halfling.pack(side = 'left')
		HalfElf.pack(side = 'left')
		Gnome.pack(side = 'left')
		HalfOrc.pack(side = 'left')
		Human.pack(side = 'left')
		Tiefling.pack(side = 'left')
		Dwarf.pack(side = 'left')
		input_frame.pack(pady = 10)
		lower_input_frame.pack()
		self.Race = tk.StringVar()
		output_label = ttk.Label(master = self,
            text = 'Race :',
            font =  'Calibri 24',
            textvariable= self.Race) 
		output_label.pack(pady = 5)

		button1 = ttk.Button(self, text ="Page 1",
		command = lambda : controller.show_frame(Page1))
	
		# putting the button in its place by
		# using grid
		button1.pack(padx = 10, pady = 10)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Page 2",
		command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by
		# using grid
		button2.pack(padx = 10, pady = 10)
		
	def set_dragborn(self):
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


		


# second window frame page1 
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="StartPage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place 
		# by using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button2 = ttk.Button(self, text ="Page 2",
							command = lambda : controller.show_frame(Page2))
	
		# putting the button in its place by 
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)




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
app = tkinterApp()
app.mainloop()


