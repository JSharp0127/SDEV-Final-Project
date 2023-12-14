"""
Author: John Sharp
File: SharpJohnFinalProject.py

This program is made to allow an user to create a Dungeons and Dragons charcter in a quick and easy manner.
The user imputs a name in to the name entry field, chooses selections from the drop down menues, and uses the provided buttons to control the app. 
Since the only thing the user manually inplements is the character name no major validation is used. 


"""


import tkinter as tk #used for GUI creation
from tkinter import BOTH, CENTER, END, INSERT, TOP, YES, ttk, messagebox as mb #used for GUI creation
import random #random number generation
from PIL import Image, ImageTk #brings imgs into GUI interface
from Character_Sheet import ARMOR_CLASS, HIT_POINTS, MODIFIER, CHARACTER_FEAT, CHARACTER_IMAGE, SKILLS, Player_Sheet, LOAD_CHARACTER #modular functions
from text import GLOSSARY, HELP_TEXT, SPLASH_TEXT



   #class for application 
class CHARACTER_CREATOR:
    def __init__(self, root):
        self.root = root
        
        #root window creation
        
        root.geometry("900x850")
        root.title("Character Creator")
        root.iconbitmap('dice_ico.ico')
       
    
        #sets all stats to 0 and allows them to be accessable for use in other moduales

        self.str_mod = 0
        self.con_mod = 0    
        self.dex_mod = 0
        self.int_mod = 0
        self.wis_mod = 0
        self.cha_mod = 0
        self.str_main = 0
        self.dex_main = 0
        self.con_main = 0
        self.int_main = 0
        self.wis_main = 0
        self.cha_main = 0
        self.player = ""
        self.player_race = ""
        self.player_class = ""
        self.player_level = ""
        self.player_hp = ""
        

        #images

        self.d6_img = ImageTk.PhotoImage(Image.open("dice6.png").resize((35,35))) #cover image for the buttons for rolling stats
        #self.tiamat = ImageTk.PhotoImage(Image.open("dragon.png"))

    
        #Control to bring up the help screen 
   
        def HELP_SCREEN():
            self.help_window = tk.Toplevel()
            self.help_window.geometry("1000x800")
            self.help_window.title("How to make a character")
            self.tiamat = ImageTk.PhotoImage(Image.open("dragon.png").resize((750,200)))
            self.help_img = tk.Label(self.help_window, image= self.tiamat)
            self.help_text = HELP_TEXT()
            self.help_message = tk.Text(self.help_window, font= ('Times New Roman', 16))
            self.help_message.insert(END, self.help_text)
            self.help_message.config(state="disabled")
            self.help_button = tk.Button(self.help_window, text="OK",height=3,width=20, font= ('Times New Roman',  12), command= self.help_window.destroy)
            self.help_img.pack(side=TOP)
            self.help_message.pack()
            self.help_button.pack()
            self.help_window.mainloop()
        
        def GLOSSARY_SCREEN():
            self.gloss_window = tk.Toplevel()
            self.gloss_window.geometry("700x700")
            self.gloss_window.title("GLOSSARY")
            self.book = ImageTk.PhotoImage(Image.open("book.jpg").resize((750,200)))
            self.gloss_img = tk.Label(self.gloss_window, image= self.book)
            self.gloss_text = GLOSSARY()
            self.gloss_message = tk.Text(self.gloss_window,width= 50,height=15, font= ('Times New Roman', 18))
            self.gloss_message.insert(END, self.gloss_text)
            self.gloss_message.config(state="disabled")
            self.gloss_button = tk.Button(self.gloss_window, text="OK",height=3,width=20, font= ('Times New Roman',  12), command= self.gloss_window.destroy)
            self.gloss_img.pack(side=TOP)
            self.gloss_message.pack()
            self.gloss_button.pack()
            self.gloss_window.mainloop()
   

        #main page header

        self.header = tk.Label(root, text= "Easy 5e Character Creator", font= ('Times New Roman', 18))
        self.header.pack()

        #character name entry  (calls itself ever sec to allow name to auto update)
          
        def RETURN_ENTRY():
            global player 
            self.player = self.name.get()
            #print("Player name: ",self.player)
            self.char_name["text"] = f"Character: {self.player}"
            self.name.after(1000, RETURN_ENTRY)
        
        #Character name entry
        
        self.name_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.char_name = tk.Label(self.name_frame, font= ('Times New Roman', 12), text=f"Character name: " )
        self.char_name.pack(pady= 5)
       
        self.name = tk.Entry(self.name_frame)
        self.name.pack(padx= 30, pady= 10)

        RETURN_ENTRY() #engages the auto updating for name label
        
        
       #Modules for rolling the individual stats and gaining modifiers for the stat block
        
  
        def STR_ROLL():
            global str_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human":
                self.roll += 1
            if self.player_race == "Dragonborn" or self.player_race == "Half-Orc":
                self.roll +=2
            self.str_mod = MODIFIER(self.roll)
            self.str_main = self.roll
            self.str_stat["text"] = f"{self.roll}  Modifier: {self.str_mod}"
        
        def DEX_ROLL():
            global dex_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or self.player_race == "Half-Elf":
                self.roll += 1
            if self.player_class == "Elf" or self.player_race == "Halfling":
                self.roll += 2
            self.dex_mod = MODIFIER(self.roll)
            self.dex_main = self.roll
            self.dex_stat["text"] = f"{self.roll}  Modifier: {self.dex_mod}"
    
        def CON_ROLL():
            global con_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or self.player_race == "Gnome" or self.player_race == "Half-Elf" or self.player_race == "Half-Orc":
                self.roll += 1
            if self.player_race == "Dwarf":
                self.roll += 2
            self.con_mod = MODIFIER(self.roll)
            self.con_main = self.roll
            self.con_stat["text"] = f"{self.roll}  Modifier: {self.con_mod}"
        
        def INT_ROLL():
            global int_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or self.player_race == "Elf" or self.player_race == "Tiefling":
                self.roll += 1
            if self.player_race == "Gnome":
                self.roll += 2
            self.int_mod = MODIFIER(self.roll)
            self.int_main = self.roll
            self.int_stat["text"] = f"{self.roll}  Modifier: {self.int_mod}"
        
        def WIS_ROLL():
            global wis_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or self.player_race == "Dwarf":
                self.roll += 1
            self.wis_mod = MODIFIER(self.roll)
            self.wis_main = self.roll
            self.wis_stat["text"] = f"{self.roll}  Modifier: {self.wis_mod}"
       
        def CHA_ROLL():
            global cha_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or self.player_race == "Dragonborn" or self.player_race == "Halfling":
                self.roll += 1
            if self.player_race == "Half-Elf" or self.player_race == "Tiefling":
                self.roll += 2
            self.cha_mod = MODIFIER(self.roll)
            self.cha_main = self.roll
            self.cha_stat["text"] = f"{self.roll}  Modifier: {self.cha_mod}"
        

        #Stat Block Frame
       
        self.stat_block_frame = tk.Frame(root, relief= "ridge", borderwidth=5 )
        self.stats = tk.Label(self.stat_block_frame, text= "Ability Scores", font= ('Times New Roman', 16))
        self.stats.pack()

        #Stat Buttons
       
        self.stat_roll_frame = tk.Frame(self.stat_block_frame)
        self.str_roll = tk.Button(self.stat_roll_frame, image= self.d6_img,  command= STR_ROLL)
        self.str_roll.pack(pady=10)
        self.dex_roll = tk.Button(self.stat_roll_frame, image= self.d6_img,  command= DEX_ROLL)
        self.dex_roll.pack(pady= 10)
        self.con_roll = tk.Button(self.stat_roll_frame, image= self.d6_img,  command= CON_ROLL)
        self.con_roll.pack(pady= 10)
        self.int_roll = tk.Button(self.stat_roll_frame, image= self.d6_img,  command= INT_ROLL)
        self.int_roll.pack(pady= 10)
        self.wis_roll = tk.Button(self.stat_roll_frame, image= self.d6_img,  command= WIS_ROLL)
        self.wis_roll.pack(pady= 10)
        self.cha_roll = tk.Button(self.stat_roll_frame, image= self.d6_img,  command= CHA_ROLL)
        self.cha_roll.pack(pady= 10)

        #Stat Lablels
       
        self.stat_name_frame = tk.Frame(self.stat_block_frame)
        self.str_label = tk.Label(self.stat_name_frame, text= "Strength", font= ('Times New Roman', 15))
        self.str_label.pack(pady=15)
        self.dex_label = tk.Label(self.stat_name_frame, text= "Dexterity", font= ('Times New Roman', 15))
        self.dex_label.pack(pady=15)
        self.con_label = tk.Label(self.stat_name_frame, text= "Constitution", font= ('Times New Roman', 15))
        self.con_label.pack(pady=15)
        self.int_label = tk.Label(self.stat_name_frame, text= "Intelegince", font= ('Times New Roman', 15))
        self.int_label.pack(pady=15)
        self.wis_label = tk.Label(self.stat_name_frame, text= "Wisdom", font= ('Times New Roman', 15))
        self.wis_label.pack(pady=15)
        self.cha_label = tk.Label(self.stat_name_frame, text= "Charisma", font= ('Times New Roman', 15))
        self.cha_label.pack(pady=15)

        #Stat Modifiers Labels that update to show modifiers number
       
        self.stat_label_frame =tk.Frame(self.stat_block_frame)       
        self.str_stat = tk.Label(self.stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
        self.str_stat.pack(pady=15)
        self.dex_stat = tk.Label(self.stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
        self.dex_stat.pack(pady=15)
        self.con_stat = tk.Label(self.stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
        self.con_stat.pack(pady=15)
        self.int_stat = tk.Label(self.stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
        self.int_stat.pack(pady=15)
        self.wis_stat = tk.Label(self.stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
        self.wis_stat.pack(pady=15)
        self.cha_stat = tk.Label(self.stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
        self.cha_stat.pack(pady=15)

        
        #Modules return individual player selections. Race/Class/Level all add information to the features block
        #Most auto-update but RETURN_HP and RETURN_FEAT need to be manually controled so they do not override themselves constantly
        

        def RETURN_RACE():
            global player_race
            self.player_race = self.race_choice.get()
            #print("Player Race: ",self.player_race)
            self.race_label["text"] = f"Race: {self.player_race}"
            self.race_label.after(1000, RETURN_RACE)
   
        def RETURN_CLASS():
            global player_class
            self.player_class = self.class_choice.get()
            #print("Player Class: ",self.player_class)
            self.class_label["text"] = f"Class: {self.player_class}"
            self.class_label.after(1000, RETURN_CLASS)
    
        def RETURN_LEVEL():
            global player_level
            global hp_level
            self.player_level = self.level_choice.get()
            self.hp_level = int(self.player_level) 
            #print("Player Level: ",self.player_level)
            self.level_label["text"] = f"Level: {self.player_level}"
            self.level_label.after(1000, RETURN_LEVEL)
      
        def RETURN_HP():    
            global player_hp    
            self.player_hp = HIT_POINTS(self.player_class, self.con_mod, self.hp_level, self.player_race)
            self.hp_label["text"] = f"Hit Points: {self.player_hp}"
            #print(f"Player HP: {self.player_hp}")
    
        def RETURN_AC():
            self.player_ac = ARMOR_CLASS(self.dex_mod, self.player_class, self.con_mod, self.wis_mod, self.player_level)
            self.ac_label["text"] = f"Armor Class: {self.player_ac}"
            #print(f"Player AC: {self.player_ac}")
            #print(self.dex_mod)
            #print(self.con_mod)
            self.ac_label.after(1000, RETURN_AC)
    
        def RETURN_FEAT():
            self.feat_text.config(state= 'normal')
            self.feat_text.delete(1.0,END)
            self.spell_mod = None
            if self.player_class == "Bard" or self.player_class == "Paladin" or self.player_class == 'Sorcerer' or self.player_class == "Warlock":
                self.spell_mod = self.cha_mod
            if self.player_class == "Cleric" or self.player_class == "Druid" or self.player_class == "Monk" or self.player_class == "Ranger":
                self.spell_mod = self.wis_mod
            if self.player_class == "Wizard":
                self.spell_mod = self.int_mod
            self.feat_text.insert(END, CHARACTER_FEAT(self.player_race, self.player_class, None, self.player_level, self.spell_mod))
            self.feat_text.config(state= 'disabled')
            
       
        def RETURN_SKILL():
            self.skill_text.config(state= 'normal')
            self.skill_text.delete(1.0,END)
            self.skill_text.insert(END, SKILLS(self.str_mod, self.dex_mod, self.con_mod, self.int_mod, self.wis_mod, self.cha_mod, self.player_class, self.player_level))
            self.skill_text.config(state= 'disabled')
            self.skill_text.after(1000, RETURN_SKILL)

        
        
        #Race Selection
       
        self.race_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.race_label = tk.Label(self.race_frame, text= "Race:", font= ('Times New Roman', 12))
        self.race_label.pack()
        self.race = tk.StringVar
        self.race_choice = ttk.Combobox(self.race_frame, width= 10, textvariable= self.race, state='readonly')
        self.race_choice['values'] = ("Human", "Dwarf", "Elf", "Gnome", "Halfling", "Half-Elf", "Half-Orc", "Tiefling", "Dragonborn")
        self.race_choice.current(0)
        self.race_choice.pack()
        RETURN_RACE()

        #Class Selection

        self.class_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.class_label = tk.Label(self.class_frame, text= "Class: ", font= ('Times New Roman', 12))
        self.class_label.pack()
        self.class_var = tk.StringVar()
        self.class_choice = ttk.Combobox(self.class_frame, width= 20, font= ('Times New Roman', 12) , textvariable=self.class_var, state='readonly')
        self.class_choice['values'] = ("Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")
        self.class_choice.current(0)
        self.class_choice.pack()
        RETURN_CLASS()

        #Level Selection (1-3)
        self.level_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.level_label = tk.Label(self.level_frame, text= "Level: ", font= ('Times New Roman', 12))
        self.level_label.pack()
        self.level = tk.StringVar()
        self.level_choice = ttk.Combobox(self.level_frame, width=10, textvariable= self.level, state='readonly')
        self.level_choice["values"] = (1,2,3)
        self.level_choice.current(0)
        self.level_choice.pack()
        RETURN_LEVEL()

        #Hit Points

        self.hp_frame = tk.Frame(root, relief="ridge", borderwidth=6)
        self.hp_label =tk.Label(self.hp_frame, text= "Hit Points:   ",font= ('Times New Roman', 18))
        self.hp_label.pack()
        self.hp_button = tk.Button(self.hp_frame, text= "Roll HP", font= ('Times New Roman', 12), command= RETURN_HP)
        self.hp_button.pack()

        #Armor Class, Label auto updates with currents AC based on dex_mod and modual

        self.ac_frame = tk.Frame(root, relief="ridge",borderwidth=5)
        self.ac_label =tk.Label(self.ac_frame, text= "Armor Class: ",font= ('Times New Roman', 18))
        self.ac_label.pack()
        RETURN_AC()

        #Features Frame

        self.feat_frame = tk.Frame(root, relief="ridge", borderwidth=5)
        self.feat_label = tk.Label(self.feat_frame, text= "Features:", font=('Times New Roman', 12))
        self.feat_label.pack()
        self.feat_text = tk.Text(self.feat_frame, height=18.3, width=60, font=('Times New Roman', 12), state= "disabled")
        self.feat_button = tk.Button(self.feat_frame, text= "Press for Features:", font=('Times New Roman', 12), command=RETURN_FEAT)
        self.feat_button.pack()
        self.feat_text.pack()
        
        #Character Picture

        def SET_CHAR_IMAGE():
            self.race_img = CHARACTER_IMAGE(self.player_race)
            self.char_img = ImageTk.PhotoImage(Image.open(self.race_img).resize((200,200)))
            self.char_img_label.config(image= self.char_img)
            self.char_img_label.pack()
            self.char_img_label.after(1000, SET_CHAR_IMAGE)            

        self.char_img_frame = tk.Frame(root,  relief="ridge", borderwidth=5)
        self.char_img_label = tk.Label(self.char_img_frame)
        SET_CHAR_IMAGE()
        
        #Skills
        self.skills_frame = tk.Frame(root, relief="ridge", borderwidth=5)
        self.skill_label = tk.Label(self.skills_frame, text= "Skills: ", font= ('Times New Roman', 12))
        self.skill_label.pack()
        self.skill_text = tk.Text(self.skills_frame, width=108, font=('Times New Roman', 12), state='disable')
        RETURN_SKILL()
        self.skill_text.pack()
        
        #Resets sheet back to the start conditions        

        def NEW_SHEET():
            self.str_mod = 0
            self.dex_mod = 0
            self.con_mod = 0
            self.int_mod = 0
            self.wis_mod = 0
            self.cha_mod = 0
            self.str_stat["text"] = f"0  Modifier: {self.str_mod}"
            self.dex_stat["text"] = f"0  Modifier: {self.dex_mod}"
            self.con_stat["text"] = f"0  Modifier: {self.con_mod}"
            self.int_stat["text"] = f"0  Modifier: {self.int_mod}"
            self.wis_stat["text"] = f"0  Modifier: {self.wis_mod}"
            self.cha_stat["text"] = f"0  Modifier: {self.cha_mod}"
            self.hp_label["text"] = f"Hit Points: "
            self.name.delete(0,END)
            self.level_choice.current(0)
            self.race_choice.current(0)
            self.class_choice.current(0)
            self.feat_text.config(state= 'normal')
            self.feat_text.delete(1.0,END)
            self.feat_text.config(state= 'disabled')
        
        #Saves the currect sheet into a json file
            
        def SAVE_SHEET():
            Player_Sheet(self.player, self.player_race, self.player_class, self.player_hp, self.player_level, self.str_main, self.dex_main, self.con_main, self.int_main, self.wis_main, self.cha_main)
            self.save_window = tk.Tk()
            self.save_window.geometry('350x100')
            self.save_window.title("Save Character Sheet")
            self.save_msg = tk.Message(self.save_window,width= 300 , text= "Character Saved Using Character Name", font=('Times New Roman',12))
            self.save_ok_button = tk.Button(self.save_window, text= "OK", font=('Times New Roman', 12), command= self.save_window.destroy)
            self.save_msg.pack()
            self.save_ok_button.pack()
            

        #Loads from the given name matching a json file

        def LOADING():
            self.load_name = self.load_entry.get()
            self.sheet = LOAD_CHARACTER(self.load_name)
            #print(self.sheet)
            self.list_stats = list(self.sheet.values())
            #print(self.list_stats[0])
            self.name.insert(END,self.list_stats[0])
            self.race_choice.set(self.list_stats[1])
            self.class_choice.set(self.list_stats[2])
            self.player_hp = self.list_stats[9]
            self.hp_label["text"] = f"Hit Points: {self.player_hp}"
            self.level_choice.set(self.list_stats[10])
            self.str_main = int(self.list_stats[3])
            #print(self.str_main)
            self.dex_main = int(self.list_stats[4])
            self.con_main = int(self.list_stats[5])
            self.int_main = int(self.list_stats[6])
            self.wis_main = int(self.list_stats[7])
            self.cha_main = int(self.list_stats[8])
            self.roll = self.str_main
            self.str_mod = MODIFIER(self.roll)
            self.str_stat["text"] = f"{self.roll}  Modifier: {self.str_mod}"
            self.roll = self.dex_main
            self.dex_mod = MODIFIER(self.roll)
            self.dex_stat["text"] = f"{self.roll}  Modifier: {self.dex_mod}"
            self.roll = self.con_main
            self.con_mod = MODIFIER(self.roll)
            self.con_stat["text"] = f"{self.roll}  Modifier: {self.con_mod}"
            self.roll = self.int_main
            self.int_mod = MODIFIER(self.roll)
            self.int_stat["text"] = f"{self.roll}  Modifier: {self.int_mod}"
            self.roll = self.wis_main
            self.wis_mod = MODIFIER(self.roll)
            self.wis_stat["text"] = f"{self.roll}  Modifier: {self.wis_mod}"
            self.roll = self.cha_main
            self.cha_mod = MODIFIER(self.roll)
            self.cha_stat["text"] = f"{self.roll}  Modifier: {self.cha_mod}"
            
            

        def LOAD_SHEET():
            self.load_window = tk.Tk()
            self.load_window.geometry('350x100')
            self.load_window.title("Load Character Sheet")
            self.load_msg = tk.Message(self.load_window,width= 300 , text= "Please enter character name:", font=('Times New Roman',12))
            self.load_entry = tk.Entry(self.load_window)
            self.load_ok_button = tk.Button(self.load_window, text= "LOAD", font=('Times New Roman', 12), command= LOADING)
            self.load_msg.pack()
            self.load_entry.pack()
            self.load_ok_button.pack()
            self.load_window.mainloop()
            
        def EXIT_SHEET():
            exit_choice = mb.askquestion("Exit Application", "Do you want to quit?")
            if exit_choice == "yes":
                root.destroy()
            else:
                mb.showinfo("Return", "Returing to App")
            
            
                


        #Options Menu (NEW/SAVE/LOAD)
        self.option_frame = tk.Frame(root, relief="ridge", borderwidth=5)
        self.button_frame1 = tk.Frame(self.option_frame)
        self.button_frame2 = tk.Frame(self.option_frame)
        self.new_button = tk.Button(self.button_frame1, text= "NEW", font=('Times New Roman', 12), height=2, width=7, command= NEW_SHEET) #returns sheet back to start conditions
        self.save_button = tk.Button(self.button_frame2, text= "SAVE", font=('Times New Roman', 12), height=2, width=7, command= SAVE_SHEET) #saves current sheet into a json file
        self.load_button = tk.Button(self.button_frame2, text= "LOAD", font=('Times New Roman', 12), height=2, width=7, command=LOAD_SHEET) #loads json file into current sheet
        self.test1_button = tk.Button(self.button_frame1, text= "EXIT", font=('Times New Roman', 12), height=2, width=7, command=EXIT_SHEET)
        self.test2_button = tk.Button(self.button_frame2, text= "TEST2", font=('Times New Roman', 12), height=2, width=7)
        self.test3_button = tk.Button(self.button_frame2, text= "TEST3", font=('Times New Roman', 12), height=2, width=7)
        self.new_button.pack()
        self.save_button.pack()
        self.load_button.pack()
        self.test1_button.pack()
        #self.test2_button.pack()
        #self.test3_button.pack()
        

        #menu bar
        
        self.menu_bar = tk.Menu(root)
        root.config(menu= self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu= self.file_menu)
        self.file_menu.add_command(label= "New", command=NEW_SHEET)
        self.file_menu.add_command(label= "Save", command=SAVE_SHEET)
        self.file_menu.add_command(label= "Load", command=LOAD_SHEET)
        self.file_menu.add_command(label= "Exit", command=EXIT_SHEET)
        self.help_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label= "Help", menu= self.help_menu)
        self.help_menu.add_command(label= "How to make a character", command= HELP_SCREEN)
        self.help_menu.add_command(label= "Glossay", command= GLOSSARY_SCREEN)
       
        
         
        #Frame Packing and Placing

        self.name_frame.place(x=0, y=75)
        self.stat_block_frame.place(x=0, y=260)
        self.stat_roll_frame.pack(side= tk.RIGHT)
        self.stat_label_frame.pack(padx=50, side= tk.RIGHT)
        self.stat_name_frame.pack(side= tk.RIGHT)
        self.race_frame.place(x=200, y=75)
        self.class_frame.place(x=0, y=170)
        self.level_frame.place(x= 200, y=170)
        self.hp_frame.place(x=325, y=75)
        self.ac_frame.place(x=300, y=170)
        self.feat_frame.place(x=380, y=260)
        self.char_img_frame.place(x=650, y=40)
        self.skills_frame.place(x=0, y=700, height= 100)
        self.option_frame.place(x=480, y=75)
        self.button_frame1.pack(side= tk.LEFT)
        self.button_frame2.pack(side = tk.RIGHT)

#Introduction splash screen (Brief how-to, update log)

def SPLASH_SCREEN():
            splash_window = tk.Tk()
            splash_window.geometry("1000x700")
            splash_window.title("Welcome to Easy 5e Character Creator")
            splash_text = SPLASH_TEXT()
            splash_frame = tk.Frame(splash_window, relief="ridge", borderwidth=5)
            splash_message = tk.Text(splash_frame, font= ('Times New Roman', 16))
            splash_message.insert(END, splash_text)
            splash_message.config(state='disabled')
            splash_button = tk.Button(splash_frame, text="OK",height=3,width=20, font= ('Times New Roman',  12), command= splash_window.destroy)
            splash_frame.pack()
            splash_message.pack()
            splash_button.pack()
            splash_window.mainloop()


#Main function and loop

if __name__=="__main__":
    root = tk.Tk()
    my_gui = CHARACTER_CREATOR(root)
    SPLASH_SCREEN()
    root.mainloop()
    
