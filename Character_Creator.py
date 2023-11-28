
import tkinter as tk
from tkinter import ttk
import random
from turtle import title
from PIL import Image, ImageTk
from Character_Sheet import ARMOR_CLASS, HIT_POINTS, MODIFIER
import time



    

  
       
       
        
root = tk.Tk()


      
def RETURN_ENTRY():
    global player
    """Gets and prints the content of the entry"""
        
    player = name.get()
    print("Player name: ",player)
    char_name["text"] = f"Character: {player}"
    name.after(1000, RETURN_ENTRY)
        
        
def STR_ROLL():
    global str_mod
    roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
    str_mod = MODIFIER(roll)
    str_stat["text"] = f"{roll}  Modifier: {str_mod}"
        
def DEX_ROLL():
    global dex_mod
    roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
    if player_class == "Fighter":
        roll = roll + 2
    dex_mod = MODIFIER(roll)
    dex_stat["text"] = f"{roll}  Modifier: {dex_mod}"
    
def CON_ROLL():
    global con_mod
    roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
    con_mod = MODIFIER(roll)
    con_stat["text"] = f"{roll}  Modifier: {con_mod}"
        
def INT_ROLL():
    global int_mod
    roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
    int_mod = MODIFIER(roll)
    int_stat["text"] = f"{roll}  Modifier: {int_mod}"
        
def WIS_ROLL():
    global wis_mod
    roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
    wis_mod = MODIFIER(roll)
    wis_stat["text"] = f"{roll}  Modifier: {wis_mod}"
       
def CHA_ROLL():
    global cha_mod
    roll = random.randint(1,6) + random.randint(1,6)  + random.randint(1,6)
    cha_mod = MODIFIER(roll)
    cha_stat["text"] = f"{roll}  Modifier: {cha_mod}"
   
def HELP_SCREEN():
    help_window = tk.Tk()
    help_window.geometry("700x700")
    help_window.title("How to make a character")
    help_message = tk.Message(help_window, font= ('Times New Roman', 18), text= "This is the instructions on how to make a character\n Do this then that.\n Then this then that.")
    help_message.pack()
    help_window.mainloop()
    
def RETURN_RACE():
    global player_race
    player_race = race_choice.get()
    print("Player Race: ",player_race)
    race_label["text"] = f"Race: {player_race}"
    race_label.after(1000, RETURN_RACE)
   
def RETURN_CLASS():
    global player_class
    player_class = class_choice.get()
    print("Player Class: ",player_class)
    class_label["text"] = f"Class: {player_class}"
    class_label.after(1000, RETURN_CLASS)
    
def RETURN_LEVEL():
    global player_level
    global hp_level
    player_level = level_choice.get()
    hp_level = int(player_level) 
    print("Player Level: ",player_level)
    level_label["text"] = f"Level: {player_level}"
    level_label.after(1000, RETURN_LEVEL)
      
def RETURN_HP():
    player_hp = HIT_POINTS(player_class, con_mod, hp_level)
    hp_label["text"] = f"Hit Points: {player_hp}"
    print(f"Player HP: {player_hp}")
    
def RETURN_AC():
    player_ac = ARMOR_CLASS(dex_mod)
    ac_label["text"] = f"Armor Class: {player_ac}"
    print(f"Player AC: {player_ac}")
    print(dex_mod)
    print(con_mod)
    ac_label.after(1000, RETURN_AC)

con_mod = 0    
dex_mod = 0
d6_img = ImageTk.PhotoImage(Image.open("download.png").resize((30,30)))
root.geometry("900x900")
root.title("Character Creator")
        
menu_bar = tk.Menu(root)
root.config(menu= menu_bar)
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="New", menu= file_menu)
file_menu.add_command(label= "Quit", command=root.quit)
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label= "Help", menu= help_menu)
help_menu.add_command(label= "How to make a character", command= HELP_SCREEN)

header = tk.Label(root, text= "WIP CHARACTER CREATOR", font= ('Times New Roman', 18))
header.pack()
        
name_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
char_name = tk.Label(name_frame, font= ('Times New Roman', 12), text=f"Character name: " )
char_name.pack(pady= 5)
       
name = tk.Entry(name_frame)
name.pack(padx= 30, pady= 10)
#name.bind('<Return>', RETURN_ENTRY)
RETURN_ENTRY()
       
stat_block_frame = tk.Frame(root, relief= "ridge", borderwidth=5 )
stats = tk.Label(stat_block_frame, text= "Ability Scores", font= ('Times New Roman', 16))
stats.pack()
       
stat_roll_frame = tk.Frame(stat_block_frame)
str_roll = tk.Button(stat_roll_frame, image= d6_img, command= STR_ROLL)
str_roll.pack(pady=10)
dex_roll = tk.Button(stat_roll_frame, image= d6_img, command= DEX_ROLL)
dex_roll.pack(pady= 10)
con_roll = tk.Button(stat_roll_frame, image= d6_img, command= CON_ROLL)
con_roll.pack(pady= 10)
int_roll = tk.Button(stat_roll_frame, image= d6_img, command= INT_ROLL)
int_roll.pack(pady= 10)
wis_roll = tk.Button(stat_roll_frame, image= d6_img, command= WIS_ROLL)
wis_roll.pack(pady= 10)
cha_roll = tk.Button(stat_roll_frame, image= d6_img, command= CHA_ROLL)
cha_roll.pack(pady= 10)
       
stat_name_frame = tk.Frame(stat_block_frame)
str_label = tk.Label(stat_name_frame, text= "Strength", font= ('Times New Roman', 15))
str_label.pack(pady=15)
dex_label = tk.Label(stat_name_frame, text= "Dexterity", font= ('Times New Roman', 15))
dex_label.pack(pady=15)
con_label = tk.Label(stat_name_frame, text= "Constitution", font= ('Times New Roman', 15))
con_label.pack(pady=15)
int_label = tk.Label(stat_name_frame, text= "Intelegince", font= ('Times New Roman', 15))
int_label.pack(pady=15)
wis_label = tk.Label(stat_name_frame, text= "Wisdom", font= ('Times New Roman', 15))
wis_label.pack(pady=15)
cha_label = tk.Label(stat_name_frame, text= "Charisma", font= ('Times New Roman', 15))
cha_label.pack(pady=15)
       
stat_label_frame =tk.Frame(stat_block_frame)       
str_stat = tk.Label(stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
str_stat.pack(pady=15)
dex_stat = tk.Label(stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
dex_stat.pack(pady=15)
con_stat = tk.Label(stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
con_stat.pack(pady=15)
int_stat = tk.Label(stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
int_stat.pack(pady=15)
wis_stat = tk.Label(stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
wis_stat.pack(pady=15)
cha_stat = tk.Label(stat_label_frame, text= "0 Modifier: 0", font= ('Times New Roman', 15))
cha_stat.pack(pady=15)
       
race_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
race_label = tk.Label(race_frame, text= "Race:", font= ('Times New Roman', 12))
race_label.pack()
race = tk.StringVar
race_choice = ttk.Combobox(race_frame, width= 10, textvariable= race)
race_choice['values'] = ("Human", "Dwarf", "Elf", "Gnome")
race_choice.current(0)
race_choice.pack()
RETURN_RACE()

class_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
class_label = tk.Label(class_frame, text= "Class: ", font= ('Times New Roman', 12))
class_label.pack()
class_var = tk.StringVar()
class_choice = ttk.Combobox(class_frame, width= 10, textvariable=class_var)
class_choice['values'] = ("Fighter", "Rogue", "Sorcerer")
class_choice.current(0)
class_choice.pack()
RETURN_CLASS()

level_frame = tk.Frame(root, relief= "ridge", borderwidth=5)
level_label = tk.Label(level_frame, text= "Level: ", font= ('Times New Roman', 12))
level_label.pack()
level = tk.StringVar()
level_choice = ttk.Combobox(level_frame, width=10, textvariable= level)
level_choice["values"] = (1,2,3)
level_choice.current(0)
level_choice.pack()
RETURN_LEVEL()

hp_frame = tk.Frame(root, relief="ridge", borderwidth=6)
hp_label =tk.Label(hp_frame, text= "Hit Points: ",font= ('Times New Roman', 18))
hp_label.pack()
hp_button = tk.Button(hp_frame, text= "Roll HP", font= ('Times New Roman', 12), command= RETURN_HP)
hp_button.pack()

ac_frame = tk.Frame(root, relief="ridge",borderwidth=5)
ac_label =tk.Label(ac_frame, text= "Armor Class: ",font= ('Times New Roman', 18))
ac_label.pack()
RETURN_AC()



name_frame.place(x=0, y=75)
stat_block_frame.place(x=0, y=260)
stat_roll_frame.pack(side= tk.RIGHT)
stat_label_frame.pack(padx=50, side= tk.RIGHT)
stat_name_frame.pack(side= tk.RIGHT)
race_frame.place(x=200, y=75)
class_frame.place(x=0, y=170)
level_frame.place(x= 200, y=170)
hp_frame.place(x=300, y=170)
ac_frame.place(x=450, y=170)

       
       








root.mainloop()
        

