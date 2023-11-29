



import tkinter as tk
from tkinter import END, INSERT, ttk 
import random
from PIL import Image, ImageTk
from Character_Sheet import ARMOR_CLASS, HIT_POINTS, MODIFIER, CHARACTER_FEAT



    
class CHARACTER_CREATOR:
    def __init__(self, root):
        self.root = root
        
        #root window creation
        
        root.geometry("900x900")
        root.title("Character Creator")
    
        #sets all modifiers to 0 and allows them to be accessable for use in other moduales

        self.str_mod = 0
        self.con_mod = 0    
        self.dex_mod = 0
        self.int_mod = 0
        self.wis_mod = 0
        self.cha_mod = 0

        #images

        self.d6_img = ImageTk.PhotoImage(Image.open("download.png").resize((30,30))) #cover image for the buttons for rolling stats

    
        #Control to bring up the help screen 
   
        def HELP_SCREEN():
            self.help_window = tk.Tk()
            self.help_window.geometry("700x700")
            self.help_window.title("How to make a character")
            self.help_message = tk.Message(self.help_window, font= ('Times New Roman', 18), text= "This is the instructions on how to make a character\n Do this then that.\n Then this then that.")
            self.help_message.pack()
            self.help_window.mainloop()
   

        #menu bar
        
        self.menu_bar = tk.Menu(root)
        root.config(menu= self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="New", menu= self.file_menu)
        self.file_menu.add_command(label= "Quit", command=root.quit)
        self.help_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label= "Help", menu= self.help_menu)
        self.help_menu.add_command(label= "How to make a character", command= HELP_SCREEN)
        
        

        #main page header

        self.header = tk.Label(root, text= "WIP CHARACTER CREATOR", font= ('Times New Roman', 18))
        self.header.pack()

        #character name entry  
          
        def RETURN_ENTRY():
            global player 
            player = self.name.get()
            print("Player name: ",player)
            self.char_name["text"] = f"Character: {player}"
            self.name.after(1000, RETURN_ENTRY)
        
        #Character name entry
        
        self.name_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.char_name = tk.Label(self.name_frame, font= ('Times New Roman', 12), text=f"Character name: " )
        self.char_name.pack(pady= 5)
       
        self.name = tk.Entry(self.name_frame)
        self.name.pack(padx= 30, pady= 10)

        RETURN_ENTRY() #engages the auto updating for name label
        
        """
        Modules for rolling the individual stats and gaining modifiers for the stat block
        """
  
        def STR_ROLL():
            global str_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human":
                self.roll += 1
            if self.player_race == "Dragonborn" or "Half-Orc":
                self.roll +=2
            self.str_mod = MODIFIER(self.roll)
            self.str_stat["text"] = f"{self.roll}  Modifier: {self.str_mod}"
        
        def DEX_ROLL():
            global dex_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or "Half-Elf":
                self.roll += 1
            if self.player_class == "Elf" or "Halfling":
                self.roll += 2
            self.dex_mod = MODIFIER(self.roll)
            self.dex_stat["text"] = f"{self.roll}  Modifier: {self.dex_mod}"
    
        def CON_ROLL():
            global con_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or "Gnome" or "Half-Elf" or "Half-Orc":
                self.roll += 1
            if self.player_race == "Dwarf":
                self.roll += 2
            self.con_mod = MODIFIER(self.roll)
            self.con_stat["text"] = f"{self.roll}  Modifier: {self.con_mod}"
        
        def INT_ROLL():
            global int_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or "Elf" or "Tiefling":
                self.roll += 1
            if self.player_race == "Gnome":
                self.roll += 2
            self.int_mod = MODIFIER(self.roll)
            self.int_stat["text"] = f"{self.roll}  Modifier: {self.int_mod}"
        
        def WIS_ROLL():
            global wis_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or "Dwarf":
                self.roll += 1
            self.wis_mod = MODIFIER(self.roll)
            self.wis_stat["text"] = f"{self.roll}  Modifier: {self.wis_mod}"
       
        def CHA_ROLL():
            global cha_mod
            self.roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
            if self.player_race ==  "Human" or "Dragonborn" or "Halfling":
                self.roll += 1
            if self.player_race == "Half-Elf" or "Tiefling":
                self.roll += 2
            self.cha_mod = MODIFIER(self.roll)
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

        """
        Modules return individual player selections. Race/Class/Level all add information to the features block
        """

        def RETURN_RACE():
            global player_race
            self.player_race = self.race_choice.get()
            print("Player Race: ",self.player_race)
            self.race_label["text"] = f"Race: {self.player_race}"
            self.race_label.after(1000, RETURN_RACE)
   
        def RETURN_CLASS():
            global player_class
            self.player_class = self.class_choice.get()
            print("Player Class: ",self.player_class)
            self.class_label["text"] = f"Class: {self.player_class}"
            self.class_label.after(1000, RETURN_CLASS)
    
        def RETURN_LEVEL():
            global player_level
            global hp_level
            self.player_level = self.level_choice.get()
            self.hp_level = int(self.player_level) 
            print("Player Level: ",self.player_level)
            self.level_label["text"] = f"Level: {self.player_level}"
            self.level_label.after(1000, RETURN_LEVEL)
      
        def RETURN_HP():
            self.player_hp = HIT_POINTS(self.player_class, self.con_mod, self.hp_level)
            self.hp_label["text"] = f"Hit Points: {self.player_hp}"
            print(f"Player HP: {self.player_hp}")
    
        def RETURN_AC():
            self.player_ac = ARMOR_CLASS(self.dex_mod)
            self.ac_label["text"] = f"Armor Class: {self.player_ac}"
            print(f"Player AC: {self.player_ac}")
            print(self.dex_mod)
            print(self.con_mod)
            self.ac_label.after(1000, RETURN_AC)
    
        def RETURN_FEAT():
            self.feat_text.config(state= 'normal')
            self.feat_text.delete(1.0,END)
            self.feat_text.insert(END, CHARACTER_FEAT(self.player_race, self.player_class, None, self.player_level))
            self.feat_text.config(state= 'disabled')
            self.feat_text.after(1000, RETURN_FEAT)
        
        #Race Selection
       
        self.race_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.race_label = tk.Label(self.race_frame, text= "Race:", font= ('Times New Roman', 12))
        self.race_label.pack()
        self.race = tk.StringVar
        self.race_choice = ttk.Combobox(self.race_frame, width= 10, textvariable= self.race)
        self.race_choice['values'] = ("Human", "Dwarf", "Elf", "Gnome", "Halfling", "Half-Elf", "Half-Orc", "Tiefling", "Dragonborn")
        self.race_choice.current(0)
        self.race_choice.pack()
        RETURN_RACE()

        #Class Selection

        self.class_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.class_label = tk.Label(self.class_frame, text= "Class: ", font= ('Times New Roman', 12))
        self.class_label.pack()
        self.class_var = tk.StringVar()
        self.class_choice = ttk.Combobox(self.class_frame, width= 10, textvariable=self.class_var)
        self.class_choice['values'] = ("Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard")
        self.class_choice.current(0)
        self.class_choice.pack()
        RETURN_CLASS()

        #Level Selection (1-3)
        self.level_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
        self.level_label = tk.Label(self.level_frame, text= "Level: ", font= ('Times New Roman', 12))
        self.level_label.pack()
        self.level = tk.StringVar()
        self.level_choice = ttk.Combobox(self.level_frame, width=10, textvariable= self.level)
        self.level_choice["values"] = (1,2,3)
        self.level_choice.current(0)
        self.level_choice.pack()
        RETURN_LEVEL()

        #Hit Points

        self.hp_frame = tk.Frame(root, relief="ridge", borderwidth=6)
        self.hp_label =tk.Label(self.hp_frame, text= "Hit Points: ",font= ('Times New Roman', 18))
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
        self.feat_text = tk.Text(self.feat_frame, height=18.3, width=50, font=('Times New Roman', 12), state= "disabled")
        RETURN_FEAT()
        self.feat_text.pack()

        #Frame Packing and Placing

        self.name_frame.place(x=0, y=75)
        self.stat_block_frame.place(x=0, y=260)
        self.stat_roll_frame.pack(side= tk.RIGHT)
        self.stat_label_frame.pack(padx=50, side= tk.RIGHT)
        self.stat_name_frame.pack(side= tk.RIGHT)
        self.race_frame.place(x=200, y=75)
        self.class_frame.place(x=0, y=170)
        self.level_frame.place(x= 200, y=170)
        self.hp_frame.place(x=300, y=170)
        self.ac_frame.place(x=450, y=170)
        self.feat_frame.place(x=450, y=260)


if __name__=="__main__":
    root = tk.Tk()
    my_gui = CHARACTER_CREATOR(root)
    root.mainloop()
    
