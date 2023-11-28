import json
import tkinter as tk
import random

def Player_Sheet(name, race, player_Class, str_Stat, dex_Stat, con_Stat, int_Stat, win_Stat, cha_Stat, aC, speed):

    """
    Player Stats
    """
    name = ""
    race = ""
    player_Class = ""
    str_Stat = 0
    dex_Stat = 0
    con_Stat = 0
    int_Stat = 0
    win_Stat = 0
    cha_Stat = 0
    aC = 0
    speed = 0
    
    global character_Sheet
    character_Sheet = {"Name": name, "Race": race, "Class": player_Class, "Str": str_Stat, "Dex": dex_Stat, "Con": con_Stat, "Int": int_Stat, "Wis": win_Stat, "Cha": cha_Stat,
                      "AC": aC, "Speed": speed }
    

def MODIFIER(roll):
    mod = -5
    for count in range(1,20,2):
        if roll == count or roll == count - 1:
            print(type(mod))
            return mod
        mod +=1
        
def HIT_POINTS(player_class, con_mod = None, level = None):
    if player_class == "Fighter":
        roll_total = 0
        for count in range(level):
            roll = random.randint(1,10)
            roll_total = roll + roll_total
            print(roll)
            print(roll_total)
            count+=1
        hp = roll_total + (con_mod * level) 
        print(hp)
        return hp
        
def  ARMOR_CLASS(dex= None):
    player_ac = 10 + dex
    return player_ac

def Save_Character():
    file_Name = input("Enter Save Name\n")
    with open(file_Name + ".json", 'w') as f:
        json.dump(character_Sheet, f)
        

if __name__=="__main__":
   while True:
    choice = input("mod test (mod/hp)")
    while choice == "mod":
        roll = int(input("roll"))
        print(MODIFIER(roll))
    while choice == "hp":
        player_class = input("player class")
        con_mod = int(input("con mod"))
        level = int(input("level"))
        print(HIT_POINTS(player_class, con_mod, level))
    
        
        
    
